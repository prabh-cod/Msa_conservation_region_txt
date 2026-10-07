#!/bin/bash
# T1-CANARY
set -e -u -o pipefail

mkdir -p /logs/verifier
mkdir -p /root/solution

if pytest -rA --ctrf /logs/verifier/ctrf.json /tests/test_outputs.py; then
    echo 1 > /logs/verifier/reward.txt
else
    echo 0 > /logs/verifier/reward.txt
fi