from __future__ import annotations

import argparse
import os.path
import re

import pytest

import support


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
DICKI = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def compute(s: str) -> int:
    lines = s.splitlines()
    sum_ = 0
    wut = re.compile(r'(zero|one|two|three|four|five|six|seven|eight|nine|\d)')
    wut2 = re.compile(
        r'(orez|enin|thgie|neves|xis|evif|ruof|eerht|owt|eno|\d)',
    )
    for line in lines:
        line = line.strip()

        l1 = wut.search(line)
        l2 = wut2.search(line[::-1])

        if (l1 is not None) and (l2 is not None):
            sum_ += int(
                DICKI.get((t := l1.groups()[0]), t)
                + DICKI.get((t2 := l2.groups()[0][::-1]), t2),
            )
    return sum_


INPUT_S = '''\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''
EXPECTED = 281


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
