# Evaluation instructions

This repository supplies the participant ACT policy adapter and launchers for all
ten RoboSynChallenge tasks. It does not replace the organizer-provided simulator,
task assets, dependencies, or evaluator.

## Runtime preparation

Install these participant files into the organizer-provided RoboSynChallenge
checkout while retaining its existing `scripts/eval_policy.py`,
`policy/inference_timing.py`, simulator, and task configuration files:

```bash
SUBMISSION=/absolute/path/to/robosyn-act-10task-submission
RUNTIME=/absolute/path/to/official/RoboSynChallenge
mkdir -p "$RUNTIME/policy/act"
cp "$SUBMISSION/policy/act/deploy_policy.py" "$RUNTIME/policy/act/"
cp "$SUBMISSION/policy/act/deploy_policy.yml" "$RUNTIME/policy/act/"
cp "$SUBMISSION/policy/act/__init__.py" "$RUNTIME/policy/act/"
cp "$SUBMISSION/policy/act/eval.sh" "$RUNTIME/policy/act/"
cp "$SUBMISSION/policy/act/run_eval.py" "$RUNTIME/policy/act/"
cp "$SUBMISSION/policy/eval.sh" "$RUNTIME/policy/"
cp "$SUBMISSION/model_manifest.json" "$RUNTIME/"
cd "$RUNTIME"
```

Use the Python environment prepared for the ACT policy, including
`huggingface_hub`, LeRobot, Torch, NumPy, and the official simulator
dependencies. The launcher installs or upgrades nothing.

## Command

The launcher follows the official ACT positional argument order:

```bash
bash policy/act/eval.sh TASK random auto 0 --headless True
```

`policy/eval.sh` is an equivalent entry point. `auto` downloads
`model.safetensors` and `config.json` from the exact immutable revision in
`model_manifest.json`. A local checkpoint directory containing those two files
may replace `auto`. The fourth positional argument selects the visible GPU.
Additional evaluator overrides must use `--key value` pairs.

Inspect a task mapping and generated command without downloading a checkpoint or
starting the simulator:

```bash
bash policy/act/eval.sh water_pouring random auto 0 --dry-run --headless True
```

The submitted adapter uses `act_step: 10`. This value is recorded consistently in
the YAML, manifest, and submission documentation. The checkpoint's internal
`n_action_steps` is a separate LeRobot policy setting.
