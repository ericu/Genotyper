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
    sys.argv[:] = [name] + argv
    return args

def computeCross(c0, c1):
  gametes0 = gameteSetsFromChromosome(c0)
  gametes1 = gameteSetsFromChromosome(c1)
  offspring = crossGameteSets(gametes0, gametes1)
  sortedChromosome = [sortGenesDominantFirst(c) for c in offspring]
  phenotypes = [phenotypeFromGenotype(g) for g in offspring]
  return {
    "gametes0": gametes0,
    "gametes1": gametes1,
    "genotypes": sortedChromosome,
    "phenotypes": phenotypes,
    "genotypeHistogram": histogram(sortedChromosome),
    "phenotypeHistogram": histogram(phenotypes),
  }

def main():
  args = _get_args()
  if args.c1:
    results = computeCross(args.c0, args.c1)
    print(results)
  else:
    print('Potential gametes for ', args.c0, ': ', gameteSetsFromChromosome(args.c0))

if __name__ == "__main__":
    main()
