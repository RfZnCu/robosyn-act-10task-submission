# RoboSynChallenge ACT submission — 10 tasks

This repository is the reproducibility entry point for one RoboSynChallenge evaluation request covering all 10 required tasks. Model weights are hosted in public Hugging Face repositories; this GitHub repository contains the policy adapter, task-to-checkpoint mapping, and the exact interface used at evaluation time.

## Checkpoints

| Task | Hugging Face checkpoint | Selected policy | Local validation summary |
|---|---|---|---|
| `drawer_open_place` | [RfZnCu/robosyn-act-drawer-open-place](https://huggingface.co/RfZnCu/robosyn-act-drawer-open-place) | failure-driven stage 5 | 40/100 on standard random, seeds 3–4 |
| `handle_basket` | [RfZnCu/robosyn-act-handle-basket](https://huggingface.co/RfZnCu/robosyn-act-handle-basket) | targeted 8k | 138/250 on standard random, five seeds |
| `item_assembly` | [RfZnCu/robosyn-act-item-assembly](https://huggingface.co/RfZnCu/robosyn-act-item-assembly) | trained 10k | 60/100 local evaluation |
| `items_handover` | [RfZnCu/robosyn-act-items-handover](https://huggingface.co/RfZnCu/robosyn-act-items-handover) | emergency safe-v1 2k | submission candidate; limited paired smoke test |
| `click_bell` | [RfZnCu/robosyn-act-click-bell](https://huggingface.co/RfZnCu/robosyn-act-click-bell) | official ACT | retained after candidate screening |
| `table_rearrangement` | [RfZnCu/robosyn-act-table-rearrangement](https://huggingface.co/RfZnCu/robosyn-act-table-rearrangement) | official ACT | 18/20 screening; candidate gain below threshold |
| `manipulate_pipette` | [RfZnCu/robosyn-act-manipulate-pipette](https://huggingface.co/RfZnCu/robosyn-act-manipulate-pipette) | selected packaged checkpoint | packaged and checksum-verified |
| `mixer_operating` | [RfZnCu/robosyn-act-mixer-operating](https://huggingface.co/RfZnCu/robosyn-act-mixer-operating) | selected packaged checkpoint | packaged and checksum-verified |
| `sample_loading` | [RfZnCu/robosyn-act-sample-loading](https://huggingface.co/RfZnCu/robosyn-act-sample-loading) | official ACT | official baseline retained; no extra training |
| `water_pouring` | [RfZnCu/robosyn-act-water-pouring](https://huggingface.co/RfZnCu/robosyn-act-water-pouring) | selected 4k | 39/50 local formal evaluation |

Every Hugging Face snapshot contains `model.safetensors`, `config.json`, and `train_config.json` and can be loaded by `lerobot.policies.act.modeling_act.ACTPolicy.from_pretrained`.

## Policy interface

All ten checkpoints use the same LeRobot ACT interface:

- state input: 14-dimensional dual-arm joint and gripper state (`robot/qpos`);
- image inputs: `cam_high`, `cam_left_wrist`, and `cam_right_wrist`, RGB 640×480;
- action output: 14-dimensional absolute dual-arm joint and gripper command;
- output chunk size: 50;
- robot-side execution chunk: 8 actions;
- gripper threshold: 0.05;
- no joint, gripper, or end-effector delta output.

The adapter is in [`policy/act`](policy/act). Set `checkpoint_path` in [`policy/act/deploy_policy.yml`](policy/act/deploy_policy.yml) to the downloaded snapshot for the task being evaluated.

## Download and run

```python
from huggingface_hub import snapshot_download

TASK = "drawer_open_place"  # replace with any task in model_manifest.json
checkpoint_path = snapshot_download(f"RfZnCu/robosyn-act-{TASK.replace('_', '-')}")
```

Then run the official RoboSynChallenge evaluator with this repository's adapter and the selected `checkpoint_path`. The exact repository IDs and immutable revisions are recorded in [`model_manifest.json`](model_manifest.json).

## Training and model selection summary

The strongest task-specific models were produced by failure-driven and semantic-targeted ACT fine-tuning. `drawer_open_place` used successful expert trajectories reconstructed around failed states plus replay data. `handle_basket` emphasized milk-grasp alignment and basket-handle grasp/lift transitions. `water_pouring` uses the selected 4k checkpoint. Tasks whose short fine-tuning candidates failed to clear the paired-selection threshold retain the official ACT checkpoint instead of submitting a regression.

Training data came from the official RoboSynChallenge simulated demonstrations and additional successful simulated expert trajectories generated in the official environments. No private real-robot data is claimed.

## Reproducibility and integrity

- Pin the immutable revisions in `model_manifest.json` for evaluation.
- Corresponding `config.json` and `train_config.json` files are mirrored under `models/<task>/`.
- The large weight files are hosted only on Hugging Face, not duplicated in GitHub.
- The submission uses the official task success criteria and standard random environments.

## License

The model repositories declare Apache-2.0. RoboSynChallenge code, datasets, and assets remain subject to their upstream licenses.
