# RoboSynChallenge ACT submission — 10 tasks

This repository is the participant-policy entry point for one RoboSynChallenge
evaluation request covering all ten required tasks. The final ACT_SEU_MAI model
weights are hosted in public Hugging Face repositories. This repository contains
the policy adapter, immutable task-to-checkpoint manifest, and evaluation
launchers requested by the organizers.

## Tasks

The submission covers:

- `table_rearrangement`
- `click_bell`
- `water_pouring`
- `handle_basket`
- `items_handover`
- `drawer_open_place`
- `mixer_operating`
- `item_assembly`
- `manipulate_pipette`
- `sample_loading`

Every checkpoint repository contains the two files required for inference:
`model.safetensors` and `config.json`. The exact Hugging Face repositories and
immutable full commit revisions are recorded in
[`model_manifest.json`](model_manifest.json).

## Policy interface

All ten checkpoints use the same LeRobot ACT interface:

- state: 14-dimensional dual-arm joint and gripper state at `robot/qpos`;
- images: `cam_high`, `cam_left_wrist`, and `cam_right_wrist`;
- action: 14-dimensional absolute dual-arm joint and gripper command;
- policy output chunk size: 50;
- adapter execution step: 10;
- no joint, gripper, or end-effector delta output.

The adapter is in [`policy/act`](policy/act). It exports the three functions
required by the official evaluator: `get_model`, `eval`, and `reset_model`.

## Evaluation launcher

Install the participant files into the organizer-provided RoboSynChallenge
runtime as described in [`EVALUATION.md`](EVALUATION.md). Do not replace the
official simulator or evaluator.

Run a task with its manifest-pinned checkpoint:

```bash
bash policy/act/eval.sh click_bell random auto 0 --headless True
```

The equivalent top-level entry point is:

```bash
bash policy/eval.sh click_bell random auto 0 --headless True
```

Use `--dry-run` to inspect the immutable checkpoint and generated official
evaluator command without downloading a model or starting the simulator.

## Integrity

- All checkpoint revisions are immutable 40-character commit hashes.
- Large model weights are hosted only on Hugging Face and are not committed to
  GitHub.
- Task-local `config.json` files are mirrored under `models/<task>/`.
- The launchers use the organizer-provided runtime and do not alter the
  simulator, task environments, or evaluation script.

## License

The model repositories declare Apache-2.0. RoboSynChallenge code, datasets, and
assets remain subject to their upstream licenses.
