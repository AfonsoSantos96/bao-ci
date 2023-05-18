#!/bin/python3

# SPDX-License-Identifier: Apache-2.0
# Copyright (c) Bao Project and Contributors. All rights reserved

"""
Generating HIS metrics check
"""

import os
import sys

CYCLOMATIC_TRESHOLD = 10
METRIC_FAIL = 0

def process_metrics(filename):

    """Process each HIS metric."""

    process_complexity(filename)

def process_complexity(file):

    """Process McCabe Cyclomatic Complexity for each function in a file"""

    global METRIC_FAIL
    complexity = "pmccabe -c "
    lines = os.popen(complexity + str(file))
    lines = lines.read()
    sline = lines.split('\n')

    for num in range(len(sline)-1):
        fields = sline[num].split('\t')
        colony_count = int(fields[0])
        if colony_count > CYCLOMATIC_TRESHOLD:
            print("Complexity exceeded (max." + str(CYCLOMATIC_TRESHOLD) + "): "
                  + fields[0] + " at " + fields[5])
            METRIC_FAIL = 1

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        process_metrics(os.path.realpath(arg))

    if METRIC_FAIL:
        sys.exit(-1)
