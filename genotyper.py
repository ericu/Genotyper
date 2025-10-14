#!/usr/bin/env python3

input = 'AABb'

characters = [c for c in input]
firsts = characters[0::2]
seconds = characters[1::2]

options = [x for x in zip(firsts, seconds)]
print('input', options)
def handle(options):
  if len(options) < 1:
    raise 'ouch'
  (h0, h1) = options[0]
  if len(options) > 1:
    tail = options[1:]
    children = handle(tail)
    print('children', children)
    return [h0+child for child in children] + [h1+child for child in children]
  else:
    return [h0, h1]
print(handle(options))

