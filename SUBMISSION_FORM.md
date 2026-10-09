# Official submission form values

Create two separate model-registry entries and two separate evaluation submissions.

## Model registry

### Drawer open place

- Base model name: `ACT drawer_open_place failure-driven stage5`
- Checkpoint link: `https://huggingface.co/RfZnCu/robosyn-act-drawer-open-place/tree/5da263ee0c026b5104f59ef977a1f7cfed1ea0d6`
- Code link: use the URL of this GitHub repository after publishing it

### Handle basket

- Base model name: `ACT handle_basket targeted 8k`
- Checkpoint link: `https://huggingface.co/RfZnCu/robosyn-act-handle-basket/tree/a73522f0f1c041f4a7b8395797d3fad3cca85c0b`
- Code link: use the URL of this GitHub repository after publishing it

## Evaluation protocol (both models)

- Ranked: checked
- Training data source: official simulated data; disclose additional simulated expert trajectories where the form permits details
- State inputs: joints and gripper
- EEF pose input: unchecked
- Image inputs: `cam_high`, `cam_left_wrist`, `cam_right_wrist`
- Output joints: enabled, delta unchecked
- Output gripper: enabled, delta unchecked
- Output EEF pose: unchecked
- `output_chunk_size`: `50`
- Gripper threshold: `0.05`
- `execution_chunk_size`: `8`

## Suggested descriptions

### Drawer open place

Short description:

> LeRobot ACT policy fine-tuned with failure-driven successful expert demonstrations and historical replay. It consumes dual-arm joint/gripper state and three RGB views, and emits absolute joint/gripper action chunks.

Technical notes:

> Load with ACTPolicy.from_pretrained. Input state is robot/qpos (14D). Image keys are cam_high, cam_left_wrist, and cam_right_wrist. Output is a 14D absolute joint/gripper action. Output chunk size is 50 and robot-side execution chunk size is 8.

### Handle basket

Short description:

> LeRobot ACT policy fine-tuned on 300 targeted official simulated demonstrations emphasizing milk-grasp alignment and basket-handle grasp/lift behavior. It consumes dual-arm joint/gripper state and three RGB views.

Technical notes:

> Load with ACTPolicy.from_pretrained. Input state is robot/qpos (14D). Image keys are cam_high, cam_left_wrist, and cam_right_wrist. Output is a 14D absolute joint/gripper action. Output chunk size is 50 and robot-side execution chunk size is 8.

## Final check before submitting

1. Open both pinned Hugging Face links in a logged-out/private browser and confirm they are publicly readable.
2. Confirm the GitHub repository is public.
3. Confirm each Hugging Face repository contains `model.safetensors`, `config.json`, and `train_config.json`.
4. Register both models first, then submit one evaluation request for each task/model.
5. Do not upload local datasets, videos, SSH keys, passwords, access tokens, or training logs containing secrets.
