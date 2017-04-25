#!/usr/bin/env python3

import sys
import re
import functools
import operator
import math

L_CHAR='0'
G_CHAR='1'

def transform_bad(original, C):
  art = list(original)
  K = len(art)
  for c in range(1,C):
    tmp = []
    for i in range(len(art)):
      if art[i] == L_CHAR:
        tmp.extend(list(original))
      elif art[i] == G_CHAR:
        tmp.extend(K*[G_CHAR])
    art = tmp
  return ''.join(art)

def transform(original, C):
  art = original
  K = len(art)
  for c in range(1,C):
    tmp = ''
    for i in range(len(art)):
      if art[i] == L_CHAR:
        tmp += original
      elif art[i] == G_CHAR:
        tmp += K*G_CHAR
    art = tmp
  return art

def generate_originals(K):
  results = []
  for i in range(2**K):
    results.append("{:0{}b}".format(i, K))
  return results
    
def logical_and(a, b):
  return a&b

def calculate(data):
  K, C, S = data
  print(K, C, S)
  originals = generate_originals(K)
  print("Generated originals")
  #print(originals)
  for p in originals:
    print('<'+p+" == "+str(int(p, 2)))
  arts = []
  results = []
  for o in originals:
    art = transform(o, C)
    arts.append(art)
  without_gold = arts[0]
  with_gold_all = arts[1:]
  #print('>'+without_gold)
  for p in with_gold_all:
    print('<'+p+" == "+str(int(p, 2)))
  #print('<'+'\n<'.join(with_gold_all))
  # search for single tile solutions
  for i in range(K**C):
    if [x[i] for x in with_gold_all] == [G_CHAR] * len(with_gold_all):
      return str(i+1)
  # search for two tile solutions
  for i in range(K**C):
    for j in range(K**C):
      if [(int(x[i]) or int(x[j])) for x in with_gold_all] == [True] * len(with_gold_all):
        return ', '.join([str(i+1), str(j+1)])
  # search for more tile solutions...
      #TODO
  """
    r = functools.reduce(operator.and_, [int(x, 2) for x in with_gold_all])
    r.bit_length()
    s = "{0:0{}b}".format(r, len(without_gold))
    return s.index('1')+1
  """
  return 'IMPOSSIBLE'


def calculate_alt(data):
  K, C, S = data
  return ', '.join(str(x+1) for x in range(K))


def process(filename):
  data = []
  with open(filename, 'r') as infile:
    data = infile.readlines()
  count, data = int(data[0]), [[int(i) for i in x.split(' ')] for x in data[1:]]
  i = 0
  results = []
  while i < count:
    r = calculate_alt(data[i])
    print("Case #{}: {}".format(i+1, r))
    results.append(r)
    i += 1
  #print(results)
  return results


def out(filename, results):
   for i, v in enumerate(results):
      print("Case #{}: {}".format(i+1, v))


def main():
  filename = 'D-large-practice.in'
  filename = 'D-small-practice.in'
  #filename = 'D-my-practice.in'
  r = process(filename)
  #out(filename, r)


if __name__ == '__main__':
  main()
