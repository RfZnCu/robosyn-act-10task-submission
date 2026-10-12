"""Resolve a manifest-pinned checkpoint and invoke the official evaluator."""

import argparse
import json
import os
from pathlib import Path
import re
import shlex
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]


def main():
    manifest = json.loads((ROOT / "model_manifest.json").read_text(encoding="utf-8"))
    entries = {entry["task"]: entry for entry in manifest["models"]}
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("task", choices=sorted(entries))
    parser.add_argument("setting", choices=["random", "clear"])
    parser.add_argument("checkpoint", nargs="?", default="auto")
    parser.add_argument("gpu_id", nargs="?", default="0")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the pinned source and command without downloading or running.",
    )
    args, extra = parser.parse_known_args()

    if len(extra) % 2 or any(not key.startswith("--") for key in extra[::2]):
        parser.error("Extra evaluator options must be --key value pairs.")
    reserved = {
        "--task_name",
        "--setting",
        "--checkpoint_path",
        "--policy_name",
        "--config",
        "--overrides",
        "--model_name",
    }
    if reserved.intersection(extra[::2]):
        parser.error("Task, setting, checkpoint and adapter are selected by the launcher.")

    entry = entries[args.task]
    revision = entry["revision"]
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        parser.error("Manifest checkpoint revision must be a full commit hash.")
    source = f"https://huggingface.co/{entry['huggingface_repo']}/tree/{revision}"
    print(f"Task: {args.task}\nPinned checkpoint: {source}", flush=True)

    evaluator = ROOT / "scripts" / "eval_policy.py"
    if not args.dry_run:
        for required in [evaluator, ROOT / "policy" / "inference_timing.py"]:
            if not required.is_file():
                parser.error(
                    f"Missing official runtime file: {required}. "
                    "Install this participant policy into the organizer-provided "
                    "RoboSynChallenge checkout; see EVALUATION.md."
                )

    if args.checkpoint == "auto":
        if args.dry_run:
            checkpoint = f"<snapshot:{entry['huggingface_repo']}@{revision}>"
        else:
            from huggingface_hub import snapshot_download

            checkpoint = snapshot_download(
                repo_id=entry["huggingface_repo"],
                revision=revision,
                allow_patterns=manifest["required_files"],
            )
    else:
        checkpoint = str(Path(args.checkpoint).expanduser().resolve())
        print("Using an explicit local checkpoint directory.", flush=True)

    if not args.dry_run:
        missing = [
            name
            for name in manifest["required_files"]
            if not (Path(checkpoint) / name).is_file()
        ]
        if missing:
            parser.error(f"Incomplete checkpoint: missing {', '.join(missing)}")

    command = [
        sys.executable,
        str(evaluator),
        "--config",
        str(ROOT / "policy" / "act" / "deploy_policy.yml"),
        "--overrides",
        "--task_name",
        args.task,
        "--setting",
        args.setting,
        "--checkpoint_path",
        checkpoint,
        "--model_name",
        f"{args.task}-{revision[:12]}",
        *extra,
    ]
    print(f"CUDA_VISIBLE_DEVICES={args.gpu_id}", flush=True)
    print(shlex.join(command), flush=True)
    if args.dry_run:
        return 0

    environment = os.environ.copy()
    environment["CUDA_VISIBLE_DEVICES"] = args.gpu_id
    paths = [str(ROOT), str(ROOT / "policy")]
    embodichain = Path(
        environment.get("EMBODICHAIN_ROOT", str(ROOT.parent / "EmbodiChain"))
    )
    if embodichain.is_dir():
        paths.insert(0, str(embodichain))
    if environment.get("PYTHONPATH"):
        paths.append(environment["PYTHONPATH"])
    environment["PYTHONPATH"] = os.pathsep.join(paths)
    environment.setdefault("PYTHONWARNINGS", "ignore::UserWarning")
    environment["EMBODICHAIN_SIM_EXIT_PROCESS"] = "0"
    return subprocess.call(command, cwd=ROOT, env=environment)


if __name__ == "__main__":
    raise SystemExit(main())
