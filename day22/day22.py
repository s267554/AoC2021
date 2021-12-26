import numpy as np
import itertools

input = open('input.txt').read()

def parse_input(input: str):
  list_op = input.split('\n')
  list_op = [x for x in list_op if len(x) > 0]

  res = []
  for op in list_op: 
    flag_str , cuboid_str = op.split()
    flag_str , cuboid_str

    flag = flag_str == 'on'

    list_start_end = [coord.split('=')[1].split('..') for coord in cuboid_str.split(',')]

    res.append((flag, list_start_end))

  return res

r = parse_input(input)

from typing import List


def range_intersec(a: List, b: List):

  if max(a[0], b[0]) > min(a[1], b[1]):
    return None

  res = max(a[0], b[0]), min(a[1], b[1])

  return res

def cuboid_intersec(a, b):

  xa_s, xa_e = a[0]
  ya_s, ya_e = a[1]
  za_s, za_e = a[2]

  xb_s, xb_e = b[0]
  yb_s, yb_e = b[1]
  zb_s, zb_e = b[2] 


  rx = range_intersec(a[0], b[0])
  ry = range_intersec(a[1], b[1])
  rz = range_intersec(a[2], b[2])

  if None in [rx, ry, rz]:
    return None

  return rx, ry, rz

def decompose_cuboid(cuboid, inters) -> List:

  rages = []
  for d in range(3):

    tmp = (
          (cuboid[d][0], inters[d][0]-1), 
          (inters[d][0], inters[d][1]),
          (inters[d][1]+1, cuboid[d][1])
    )

    tmp = tuple([(x,y) for x,y in tmp if x <= y])

    rages.append(tuple(tmp))

  list_cuboid = list(itertools.product(*rages))  

  return list_cuboid

def is_contained(bigger, smaller):
  for i in range(3):
    if smaller[i][0] < bigger[i][0] or smaller[i][1] > bigger[i][1]:
      return False
  return True

list_cuboid_on = []

for i, rr in enumerate(r):

  # print(f'i: {i}')

  flag = rr[0]
  list_start_end = rr[1]

  list_start_end = list_start_end

  x_s, x_e = list(map(int, list_start_end[0]))
  y_s, y_e = list(map(int, list_start_end[1]))
  z_s, z_e = list(map(int, list_start_end[2]))

  curr_cuboid = (x_s, x_e), (y_s, y_e), (z_s, z_e)
  # print(curr_cuboid)

  # print(len(list_cuboid_on))

  toAdd, toRemove = [], []

  for c in list_cuboid_on:
      inters = cuboid_intersec(c, curr_cuboid)
      
      if inters is not None:        
        decomposed = decompose_cuboid(c, inters)
        toAdd += [d for d in decomposed if not is_contained(curr_cuboid, d)]
        toRemove += [c]

  for rem in toRemove:
    list_cuboid_on.remove(rem)

  list_cuboid_on += toAdd

  if flag:
    list_cuboid_on.append(curr_cuboid)

s = 0
for c in list_cuboid_on:
  s += (c[0][1] - c[0][0]+1) * (c[1][1] - c[1][0]+1) * (c[2][1] - c[2][0]+1)

print(f"sol2 is {s}")