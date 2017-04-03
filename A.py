#!/usr/bin/env python3

import sys

def calculate(number):
  if number == 0:
    return 'INSOMNIA'
  i = 0
  digits = [False] * 10
  while not all(digits):
    i += number
    for d in str(i):
      digits[int(d)] = True
    if i/number > 10000000:
      return 'INSOMNIA'
  return i
  

def process_file(filename):
  data = []
  with open(filename, 'r') as infile:
    data = infile.readlines()
  count, data = int(data[0]), [int(x) for x in data]
  i = 1
  while i <= count:
    print("Case #{}: {}".format(i, calculate(data[i])))
    i += 1


def main():
  filename = 'A-large-practice.in'
  filename = 'A-small-practice.in'
  #filename = 'A-my-sample.in'
  process_file(filename)


if __name__ == '__main__':
  main()
