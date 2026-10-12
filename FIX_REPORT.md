# Evaluation launcher correction

The previous immutable source submission
`1fc98948af2d04c0ae7667cdabbb1d3d97b9b41a` contained the ACT adapter and YAML
but omitted the evaluation launchers and package export required by the official
evaluator.

This correction adds:

1. `policy/eval.sh`, the top-level participant entry point;
2. `policy/act/eval.sh`, using the official ACT positional arguments;
3. `policy/act/run_eval.py`, resolving each task's immutable checkpoint and
   invoking the organizer-provided evaluator;
4. `policy/act/__init__.py`, exporting `get_model`, `eval`, and `reset_model`;
5. `EVALUATION.md` and `TASK_COMMANDS.md`, documenting installation and every
   task mapping.

The correction also replaces the checkpoint mapping with the final ACT_SEU_MAI
models. Each Hugging Face repository contains the two files required at runtime:
`model.safetensors` and `config.json`. Every checkpoint and the corrected GitHub
source are pinned to immutable full commit revisions.

No simulator, task environment, organizer evaluator, or dependency package is
included or modified. No model performance claim is introduced by this launcher
correction.
