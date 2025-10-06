#!/usr/bin/env python3

import re


def extract_last(filename, pattern):
    p = re.compile(pattern)
    for line in reversed(open(filename).readlines()):
        m = p.search(line.rstrip())
        if m:
            return m.group(1)
