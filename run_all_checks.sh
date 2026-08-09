#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$ROOT/logs" "$ROOT/results" "$ROOT/data"
export PYTHONPATH="$ROOT/code${PYTHONPATH:+:$PYTHONPATH}"
LOG="$ROOT/logs/verification.log"
: > "$LOG"
run() {
  echo ">>> $*" | tee -a "$LOG"
  "$@" 2>&1 | tee -a "$LOG"
}
run python3 "$ROOT/code/generate_witnesses.py"
run python3 "$ROOT/code/verify_witnesses.py"
run python3 "$ROOT/code/independent_edge_list_check.py"
run python3 "$ROOT/code/verify_upper_bound.py"
run python3 "$ROOT/code/adversarial_mutation_tests.py"
if command -v g++ >/dev/null 2>&1; then
  run "$ROOT/replay_search.sh"
else
  echo "SKIP: g++ unavailable; proof checks completed, discovery replay omitted" | tee -a "$LOG"
fi
echo "ALL CORE CHECKS PASSED" | tee -a "$LOG"
