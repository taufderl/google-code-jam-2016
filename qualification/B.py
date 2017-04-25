#!/usr/bin/env python3

import sys
import re

done_case = re.compile(r'^\++$')
one = re.compile(r'^\-+\+*$')
two = re.compile(r'^\++\-+$')

def maneuver(stack, n):
  assert(n<=len(stack))
  assert(n>0)
  r = stack[:n][::-1]
  r = r.replace('-', 'X')
  r = r.replace('+', '-')
  r = r.replace('X', '+')
  reverse = r + stack[n:]
  return reverse

def shortest(stack):
  if done_case.match(stack):
    return 0
  elif one.match(stack):
    return 1
  elif two.match(stack):
    return 2
  else:
    if stack.endswith('+'): # if last one is already +, ignore
      #print("R", stack, stack[:-1])
      return shortest(stack[:-1])
    if stack.startswith('-'): # -..+..-
      i = len(stack)#stack.find('+')
      new = maneuver(stack, i)
      #print("M", stack, "<%i>"%i,new)
      return 1 + shortest(maneuver(stack, i))
    else: # +....-
      i = stack.find('-')
      new = maneuver(stack, i)
      #print("M", stack, "<%i>"%i,new)
      return 1 + shortest(maneuver(stack, i))
    sys.exit()

    """ based on first on didn't work
    if stack.startswith('-'):
      i = stack.find('+')
      new = maneuver(stack, i)
      print("M", stack, new, i)
      return 1 + shortest(maneuver(stack, i))
    else:
      #print("STACK", stack)
      i = stack.rfind('-') # find last '-'
      new = maneuver(stack, i+1)
      print("M", stack, new, i+1)
      return 1 + shortest(maneuver(stack, i+1))
    """
    """ # try all didn't work
    for n in range(2, len(stack)):
      changed = maneuver(stack, n)
      if not changed == stack:
        #print("changed", changed, n)
        return 1 + shortest(changed)
"""

def calculate(data):
  #print(data)
  r = shortest(data)
  #print(data, r)
  return r
  

def process(filename):
  data = []
  with open(filename, 'r') as infile:
    data = infile.readlines()
  count, data = int(data[0]), [x.strip() for x in data[1:]]
  i = 0
  results = []
  while i < count:
    results.append(calculate(data[i]))
    i += 1
  #print(results)
  return results


def out(filename, results):
   for i, v in enumerate(results):
      print("Case #{}: {}".format(i+1, v))


def main():
  filename = 'B-large-practice.in'
  #filename = 'B-small-practice.in'
  r = process(filename)
  out(filename, r)


if __name__ == '__main__':
  main()
