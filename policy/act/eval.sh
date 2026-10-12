#!/usr/bin/env bash
# Official argument order: task setting checkpoint_path gpu_id [extra options].
# Use 'auto' for checkpoint_path to download the manifest-pinned snapshot.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ -z "${PYTHON_BIN:-}" && -x "$SCRIPT_DIR/.venv/bin/python" ]]; then
    PYTHON_BIN="$SCRIPT_DIR/.venv/bin/python"
else
    PYTHON_BIN="${PYTHON_BIN:-python}"
fi

exec "$PYTHON_BIN" "$SCRIPT_DIR/run_eval.py" "$@"
