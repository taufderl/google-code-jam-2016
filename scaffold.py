#!/usr/bin/env python3

import sys

def calculate(number):
  # TODO here is room to do the work
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
  process_file(filename)


if __name__ == '__main__':
  main()
