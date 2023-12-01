from __future__ import annotations

import argparse
import os.path
import re

import pytest

import support


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()
    sum_ = 0
    wut = re.compile(r'^[a-zA-Z]*(\d)')
    for line in lines:
        line = line.strip()
        if line == '':
            continue

        t = wut.match(line)
        t2 = wut.match(line[::-1])
        if (t is not None) and (t2 is not None):
            sum_ += int(t.groups()[0] + t2.groups()[0])
    return sum_


INPUT_S = '''\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
'''
EXPECTED = 142


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
