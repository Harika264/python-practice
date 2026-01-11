#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = input().strip()

    # Count character frequencies
    count = Counter(s)

    # Sort by frequency (descending) then alphabetically
    sorted_chars = sorted(count.items(), key=lambda x: (-x[1], x[0]))

    # Print top 3
    for char, freq in sorted_chars[:3]:
        print(char, freq)
