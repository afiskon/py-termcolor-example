#!/usr/bin/env python3

import sys
from termcolor import colored


def file_to_list(fname):
    with open(fname, "r") as f:
        return [x.strip() for x in f.readlines()]


def make_colored(ch):
    chars = {
        "~": ("blue", []),
        ".": ("white", []),
        "#": ("green", []),
        "O": ("white", ["bold"]),
        "^": ("red", ["dark"]),
        "=": ("red", ["dark"]),
    }
    default = ("red", [])
    color, attrs = chars.get(ch, default)
    return colored(ch, color, attrs=attrs)


def main():
    if len(sys.argv) < 2:
        print("Usage: {} <infile>".format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    lines = file_to_list(sys.argv[1])
    for src_line in lines:
        dst_line = ""
        i = 0
        chnum = len(src_line)
        while i < chnum:
            ch = src_line[i]
            dst_line = dst_line + make_colored(ch)
            i += 1
        print(dst_line)

if __name__ == "__main__":
    main()
