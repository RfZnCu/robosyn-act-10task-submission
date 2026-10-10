# RoboSynChallenge portal values

Submit **one evaluation request covering all 10 tasks**. Partial-task requests are invalid.

## Suggested fields

- Artifact name: `RfZnCu ACT 10-task submission`
- Experiment name: `robosyn-act-10tasks-20261010`
- Short description: `Task-specific LeRobot ACT checkpoints for all ten RoboSynChallenge tasks, including failure-driven drawer and basket policies, a selected water-pouring checkpoint, and regression-gated official baselines.`
- Code repository: URL of this public GitHub repository
- Checkpoint source: the ten public Hugging Face repositories listed in `model_manifest.json`
- Training data source: `Official RoboSynChallenge simulated demonstrations plus successful simulated expert trajectories generated in the official task environments.`
- Ranked: enabled

## Interface fields

- State inputs: joints and gripper
- EEF pose input: disabled
- Image inputs: `cam_high`, `cam_left_wrist`, `cam_right_wrist`
- Output joints: enabled; delta disabled
- Output gripper: enabled; delta disabled
- Output EEF pose: disabled
- Output chunk size: `50`
- Execution chunk size: `8`
- Gripper threshold: `0.05`

## Run notes

Use `ACTPolicy.from_pretrained` to load the repository mapped to each task in `model_manifest.json`. Set `checkpoint_path` in `policy/act/deploy_policy.yml` to that local snapshot and run the official RoboSynChallenge evaluator. All checkpoints consume 14D `robot/qpos` plus RGB `cam_high`, `cam_left_wrist`, and `cam_right_wrist`, and emit 14D absolute joint/gripper action chunks. The request covers all ten tasks: drawer_open_place, handle_basket, item_assembly, items_handover, click_bell, table_rearrangement, manipulate_pipette, mixer_operating, sample_loading, and water_pouring.

## Final checks

1. All ten Hugging Face repositories are public and contain the three required files.
2. Replace every `main` revision in `model_manifest.json` with the immutable commit hash.
3. Confirm this GitHub repository is public.
4. Confirm the portal request contains all ten task mappings before clicking Submit.
5. Do not publish datasets, videos, SSH credentials, access tokens, or private logs.
