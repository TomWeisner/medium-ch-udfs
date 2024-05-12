#!/usr/bin/python3

import sys

if __name__ == '__main__':
    for line in sys.stdin:
        print(line.rstrip()[::-1], end='')
        sys.stdout.flush()
