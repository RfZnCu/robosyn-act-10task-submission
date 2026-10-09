# RoboSynChallenge ACT Submission

This repository documents two ACT policies submitted to RoboSynChallenge:

| Task | Hugging Face checkpoint | Revision | Reported simulation result |
|---|---|---|---|
| `drawer_open_place` | [RfZnCu/robosyn-act-drawer-open-place](https://huggingface.co/RfZnCu/robosyn-act-drawer-open-place) | `5da263ee0c026b5104f59ef977a1f7cfed1ea0d6` | 40/100 (40%) on standard `random`, seeds 3 and 4 |
| `handle_basket` | [RfZnCu/robosyn-act-handle-basket](https://huggingface.co/RfZnCu/robosyn-act-handle-basket) | `a73522f0f1c041f4a7b8395797d3fad3cca85c0b` | 138/250 (55.2%) on standard `random`, seeds 3, 4, 5, 6 and 8 |

The model weights are intentionally stored on Hugging Face rather than duplicated in GitHub. Pin the revisions above for reproducible evaluation.

## Policy interface

Both policies use the same ACT interface:

- architecture: LeRobot ACT with a ResNet-18 visual backbone;
- state input: 14-dimensional dual-arm joint and gripper state (`robot/qpos`);
- image inputs: `cam_high`, `cam_left_wrist`, and `cam_right_wrist`, RGB at 640 x 480;
- action output: 14-dimensional absolute dual-arm joint and gripper command;
- output chunk size: 50;
- robot-side execution chunk: 8 actions;
- gripper threshold declared for the submission portal: 0.05;
- no joint, gripper, or end-effector delta output.

The evaluation adapter and configuration are in [`policy/act`](policy/act). The adapter loads a local path or Hugging Face snapshot through `ACTPolicy.from_pretrained` and maps the RoboSyn observations to the three image keys plus `observation.state`.

## Download pinned checkpoints

```python
from huggingface_hub import snapshot_download

drawer_path = snapshot_download(
    repo_id="RfZnCu/robosyn-act-drawer-open-place",
    revision="5da263ee0c026b5104f59ef977a1f7cfed1ea0d6",
)

basket_path = snapshot_download(
    repo_id="RfZnCu/robosyn-act-handle-basket",
    revision="a73522f0f1c041f4a7b8395797d3fad3cca85c0b",
)
```

Each snapshot contains `model.safetensors`, `config.json`, and `train_config.json` in LeRobot `ACTPolicy.from_pretrained` format.

## Evaluation

Use the official RoboSynChallenge repository and replace `checkpoint_path` in `policy/act/deploy_policy.yml` with one of the downloaded directories. The submission uses the official success criterion and the standard `random` environment. No stronger gripper physics is required for the reported final results.

The portal field values for each model are listed in [`SUBMISSION_FORM.md`](SUBMISSION_FORM.md).

## Training summary

### Drawer open place

The final policy was trained with a failure-driven mixture of 512 successful expert trajectories: 312 demonstrations reconstructed from failed evaluation states and deterministic neighboring scenes, 100 targeted replay trajectories, and 100 general replay trajectories. Training continued in two 2,000-step phases. The first used policy/backbone learning rates of `1e-6`/`5e-7`; the second used `5e-7`/`5e-7`.

The final blind evaluation used two new seeds and produced 20/50 successes on seed 3 and 20/50 on seed 4. The initial reproduced result was 3/50 (6%) on seed 0. These are not paired samples, so the 6% to 40% comparison should be read as a before/after benchmark summary rather than a paired statistical estimate.

### Handle basket

The selected policy is the 8,000-step targeted checkpoint. It was initialized from the official ACT checkpoint and fine-tuned on 300 selected demonstrations emphasizing milk grasp alignment and basket-handle grasp/lift behavior, with policy/backbone learning rates of `2e-6`/`1e-5`.

On the paired `random_gripbalanced`, seed-0 evaluation, it achieved 32/50 (64%) versus 15/50 (30%) for the official ACT checkpoint. On the stricter standard `random` environment it achieved 138/250 (55.2%) over five seeds. Later candidate checkpoints were rejected because paired tests did not improve the 8k checkpoint.

## Data provenance

Training used the official RoboSynChallenge simulated demonstration data and additional simulated expert trajectories generated inside the official task environment. No private real-robot data is claimed.

## License

The model repositories currently declare Apache-2.0. RoboSynChallenge code and assets remain subject to their upstream licenses; consult the official repository before redistribution.
