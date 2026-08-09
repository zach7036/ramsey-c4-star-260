#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$ROOT/logs" "$ROOT/results"
BIN="$ROOT/results/search_polarity_deletion_all"
g++ -O3 -std=c++17 -Wall -Wextra -pedantic "$ROOT/code/search_polarity_deletion.cpp" -o "$BIN"
for seed in 2601 2602 2603 2604; do
  OUT="$ROOT/results/replay_seed${seed}_all.json"
  LOG="$ROOT/logs/replay_seed${seed}_all.log"
  {
    echo "command: results/search_polarity_deletion_all 17 31 16 $seed 30000000 results/replay_seed${seed}_all.json 1"
    "$BIN" 17 31 16 "$seed" 30000000 "$OUT" 1
    python3 - "$ROOT" "$seed" "$OUT" <<'PY'
import json, pathlib, sys
root = pathlib.Path(sys.argv[1])
seed = sys.argv[2]
out = pathlib.Path(sys.argv[3])
expected = json.loads((root / 'data' / f'deleted_points_seed{seed}.json').read_text())
actual = json.loads(out.read_text())
assert actual == expected, (actual, expected)
print(f'PASS: seed {seed} exactly reproduced its archived deletion list')
PY
  } 2>&1 | tee "$LOG"
done
