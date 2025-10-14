#!/usr/bin/env python3

input = 'AABb'

def gametesFromChromosomes(c):
  print('c', c)
  if len(c) < 0 or len(c) % 2 != 0:
    raise 'Invalid chromosome length.'
  if len(c) == 0:
    return ['']
  a0, a1, rest = c[0], c[1], c[2:]
  tails = gametesFromChromosomes(rest)
  return [a0+tail for tail in tails] + [a1+tail for tail in tails]
print(gametesFromChromosomes(input))
