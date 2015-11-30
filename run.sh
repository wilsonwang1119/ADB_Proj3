#!/bin/bash

# Author: Youhan Wang(yw2663@columbia.edu)
# Usage: sh run.sh <INTEGRATED-DATASET> <min_sup> <min_conf>

python ADB_proj3.py "${1}" "${2}" "${3}" output.txt