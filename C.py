#!/usr/bin/env python3

import sys
from collections import OrderedDict

def is_prime(n):
  if n<=1:
    return False
  elif n<=3:
    return True
  elif n%2 == 0 or n%3 == 0:
    return False
  i = 5
  while i * i <= n:
    if n%i == 0 or n%(i+2) == 0:
      return False
    i += 6
  return True


def get_divisor(n):
  if n<=1:
    return n
  elif n<=3:
    return 3
  elif n%3 == 0: 
    return 3 
  elif n%4 == 0:
    return 4
  i = 5
  while i * i <= n:
    if n%i == 0: 
      return i 
    if n%(i+2) == 0:
      return i+2
    i += 6
  return False


def binary_is_prime(binary, base):
  n = int(binary, base)
#  print(base, n, is_prime(n))
  return is_prime(n)

def get_base_divisor(binary, base):
  n = int(binary, base)
  return get_divisor(n)


def is_jamcoin(binary):
  if not binary.startswith('1') or not binary.endswith('1'):
    return False
  return all([not binary_is_prime(binary, x) for x in range(2,11)])


def get_jamcoin_divisors(binary):
  if not binary.startswith('1') or not binary.endswith('1'):
    return False
  divisors = [get_base_divisor(binary, base) for base in range(2,11)]
  if all(divisors):
    return divisors
  else:
    return False


def calculate(data):
  # TODO here is room to do the work
  N, J = data
  N, J = int(N), int(J)
  #print(N, J)
  results = []
  i  = 2**N
  end = 2**(N+1)-1
  while i<end and len(results)<J:
    i += 1
    b = "{0:b}".format(i)
    d = get_jamcoin_divisors(b)
    if d:
      r = [b] + d
      results.append(r)
      print(r)
      base = list(range(2,11))
      print("TEST:", b, [int(b, base[j])/d[j] for j in range(9)])
  return results
  

def process(filename):
  data = []
  with open(filename, 'r') as infile:
    data = infile.readlines()
  count, data = int(data[0]), [(int(x.split(' ')[0]), int(x.split(' ')[1])) for x in data[1:]]
  i = 0
  results = []
  while i < count:
    results.append(calculate(data[i]))
    i += 1
  #print(results)
  return results


def out(filename, results):
   for i, values in enumerate(results):
      print("Case #{}:".format(i+1))
      for i in values:
        print(' '.join([str(a) for a in i]))


def main():
  #filename = 'C-large-practice.in'
  filename = 'C-small-practice.in'
  r = process(filename)
  out(filename, r)


if __name__ == '__main__':
  main()
