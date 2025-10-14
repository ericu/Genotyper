#!/usr/bin/env python3

from collections import defaultdict

inputA = 'AABb'
inputB = 'aabB'

print('input', inputA, inputB)

def gameteSetsFromChromosome(c):
  if len(c) < 0 or len(c) % 2 != 0:
    raise 'Invalid chromosome length.'
  if len(c) == 0:
    return ['']
  a0, a1, tail = c[0], c[1], c[2:]
  tails = gameteSetsFromChromosome(tail)
  return [a0+tail for tail in tails] + [a1+tail for tail in tails]
print(gameteSetsFromChromosome(inputA))
print(gameteSetsFromChromosome(inputB))

def zygoteFromGametes(g0, g1):
  if len(g0) != len(g1):
    raise 'Mismatched chromosome lengths.'
  if len(g0) <= 0:
    return ''
  a0, g0Tail = g0[0], g0[1:]
  a1, g1Tail = g1[0], g1[1:]
  return a0 + a1 + zygoteFromGametes(g0Tail, g1Tail)

def crossGameteSets(s0, s1):
  return [zygoteFromGametes(g0, g1) for g1 in s1 for g0 in s0]

offspring = crossGameteSets(
  gameteSetsFromChromosome(inputA), gameteSetsFromChromosome(inputB))

def sortGenesDominantFirst(c):
  if len(c) < 0 or len(c) % 2 != 0:
    raise 'Invalid chromosome length.'
  if len(c) == 0:
    return ''

  a0, a1, tail = c[0], c[1], c[2:]
  if (a0.isupper()):
    return a0 + a1 + sortGenesDominantFirst(tail)
  return a1 + a0 + sortGenesDominantFirst(tail)
  
sorted = [sortGenesDominantFirst(c) for c in offspring]
print(sorted)

def histogram(items):
  h = defaultdict(int)
  for item in items:
    h[item] += 1
  return h

print(histogram(sorted))
