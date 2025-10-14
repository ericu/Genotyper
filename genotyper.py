#!/usr/bin/env python3

from collections import defaultdict
import argparse
import sys

def gameteSetsFromChromosome(c):
  if len(c) < 0 or len(c) % 2 != 0:
    raise "Invalid chromosome length."
  if len(c) == 0:
    return [""]
  a0, a1, tail = c[0], c[1], c[2:]
  tails = gameteSetsFromChromosome(tail)
  return [a0+tail for tail in tails] + [a1+tail for tail in tails]

def zygoteFromGametes(g0, g1):
  if len(g0) != len(g1):
    raise "Mismatched chromosome lengths."
  if len(g0) <= 0:
    return ""
  a0, g0Tail = g0[0], g0[1:]
  a1, g1Tail = g1[0], g1[1:]
  return a0 + a1 + zygoteFromGametes(g0Tail, g1Tail)

def crossGameteSets(s0, s1):
  return [zygoteFromGametes(g0, g1) for g1 in s1 for g0 in s0]

def sortGenesDominantFirst(c):
  if len(c) < 0 or len(c) % 2 != 0:
    raise "Invalid chromosome length."
  if len(c) == 0:
    return ""

  a0, a1, tail = c[0], c[1], c[2:]
  if (a0.isupper()):
    return a0 + a1 + sortGenesDominantFirst(tail)
  return a1 + a0 + sortGenesDominantFirst(tail)
  
def histogram(items):
  h = defaultdict(int)
  for item in items:
    h[item] += 1
  return h

def phenotypeFromGenotype(c):
  if len(c) < 0 or len(c) % 2 != 0:
    raise "Invalid chromosome length."
  if len(c) == 0:
    return ""
  a0, a1, tail = c[0], c[1], c[2:]
  if (a0.isupper()):
    return a0 + phenotypeFromGenotype(tail)
  return a1 + phenotypeFromGenotype(tail)

def _get_args():
    name = sys.argv[0]
    parser = argparse.ArgumentParser()
#    parser.add_argument(
#        "-u", "--unittest", help="run unit tests", action="store_true"
#    )
    parser.add_argument(
        "-t", "--test", help="run current test", action="store_true"
    )
    parser.add_argument(
        "c0", help="input chromosome",
    )
    parser.add_argument(
        "c1", nargs="?", help="second input chromosome"
    )
    args, argv = parser.parse_known_args()
    if len(argv) > 0:
      parser.print_help()
      sys.exit(-1)
    print(args, argv)
    sys.argv[:] = [name] + argv
    return args

def runTest():
  inputA = "AABb"
  inputB = "aabB"

  print("input", inputA, inputB)
  print(gameteSetsFromChromosome(inputA))
  print(gameteSetsFromChromosome(inputB))
  offspring = crossGameteSets(
    gameteSetsFromChromosome(inputA), gameteSetsFromChromosome(inputB))
  sorted = [sortGenesDominantFirst(c) for c in offspring]
  print(sorted)

  print(histogram(sorted))
  phenotypes = [phenotypeFromGenotype(g) for g in offspring]
  print("phenotypes", phenotypes)
  print(histogram(phenotypes))

def main():
  args = _get_args()
  print(args)
  if args.test:
    runTest()

if __name__ == "__main__":
    main()
