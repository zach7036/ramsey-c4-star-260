#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$ROOT/logs" "$ROOT/results"
BUILD="$ROOT/results/search_polarity_deletion"
OUT="$ROOT/results/replay_seed2603.json"
LOG="$ROOT/logs/search_replay.log"
g++ -O3 -std=c++17 -Wall -Wextra -pedantic \
  "$ROOT/code/search_polarity_deletion.cpp" -o "$BUILD"
{
  echo "command: results/search_polarity_deletion 17 31 16 2603 5000000 results/replay_seed2603.json 1"
  "$BUILD" 17 31 16 2603 5000000 "$OUT" 1
  python3 - "$ROOT" "$OUT" <<'PY'
import json, pathlib, sys
root = pathlib.Path(sys.argv[1])
out = pathlib.Path(sys.argv[2])
expected = json.loads((root / 'data' / 'deleted_points_seed2603.json').read_text())
actual = json.loads(out.read_text())
assert actual == expected, (actual, expected)
print('PASS: deterministic seed-2603 replay exactly reproduced the archived deletion list')
PY
} 2>&1 | tee "$LOG"
