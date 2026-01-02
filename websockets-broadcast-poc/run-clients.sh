#!/usr/bin/env bash
set -e

for i in {1..5}; do
  python3 src/client.py &
done

wait
echo "All clients finished"
