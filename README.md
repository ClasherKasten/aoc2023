advent of code 2023
===================

https://adventofcode.com/2023

### about

for 2023, I'm planning to implement in python

### timing

- comparing to these numbers isn't necessarily useful
- normalize your timing to day 1 part 1 and compare
- alternate implementations are listed in parens
- these timings are very non-scientific (sample size 1)

```console
$ find -maxdepth 1 -type d -name 'day*' -not -name day00 | sort | xargs --replace bash -xc 'python {}/part1.py {}/input.txt; python {}/part2.py {}/input.txt'
+ python ./day01/part1.py ./day01/input.txt
54601
> 1364 μs
+ python ./day01/part2.py ./day01/input.txt
54078
> 2250 μs
+ python ./day02/part1.py ./day02/input.txt
2101
> 866 μs
+ python ./day02/part2.py ./day02/input.txt
58269
> 1355 μs
```
