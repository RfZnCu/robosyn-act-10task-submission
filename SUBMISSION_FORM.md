# RoboSynChallenge correction response values

Use one corrected immutable GitHub commit URL for all ten tasks. Pair it with the
task-specific immutable Hugging Face URL listed in `TASK_COMMANDS.md`.

## Suggested fields

- Artifact name: `RfZnCu ACT_SEU_MAI 10-task submission`
- Experiment name: `robosyn-act-seu-mai-10tasks-20261012`
- Code repository: the corrected immutable GitHub tree URL
- Checkpoint source: the task-specific immutable Hugging Face tree URL
- Policy: LeRobot ACT
- State inputs: joints and gripper (`robot/qpos`)
- Image inputs: `cam_high`, `cam_left_wrist`, `cam_right_wrist`
- Output joints and gripper: enabled; delta disabled
- Output chunk size: `50`
- Adapter execution step: `10`

## Run notes

The repository supplies `policy/eval.sh` and `policy/act/eval.sh`. The launchers
resolve the selected task to its fixed Hugging Face revision and invoke the
organizer-provided `scripts/eval_policy.py`. The participant submission does not
replace or modify the official simulator or task environment.

## Final checks

1. Use the new full GitHub commit URL, not the moving `main` branch.
2. Use the matching task-specific Hugging Face revision URL.
3. Ensure all ten tasks are present in the correction response.
4. Do not include passwords, access tokens, private logs, or datasets.
