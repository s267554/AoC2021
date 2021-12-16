import time
import numpy as np

with open('input.txt') as input_file:
    m = [[int(cell) for cell in line] for line in input_file.read().splitlines()]


rows, cols = len(m), len(m[0])

tables = []
t = 0
big_table = [[0]*cols*5 for _ in range(cols*5)]
def map_table(table):
  return [[(cell + i+j if cell +i+j< 10 else (cell+i+j)%10+1) for cell in row] for row in table]

for i in range(cols*5):
  for j in range(cols*5):
    cell = m[i%cols][j%cols]
    value = cell + i//cols+j//cols if cell +i//cols+j//cols< 10 else (cell+i//cols+j//cols)%10+1
    big_table[i][j] = value

m = big_table

max_val = cols * 5

t1 = time.perf_counter()


distmap=np.ones((max_val, max_val), dtype=int)*np.Infinity
distmap[0][0]=0
originmap=np.ones((max_val, max_val), dtype=int)*np.nan
visited=np.zeros((max_val, max_val), dtype=bool)
finished = False
x, y= 0, 0
count=0

#Loop Dijkstra until reaching the target cell
while not finished:
  # move to x+1][y
  if x < max_val-1:
    if distmap[x+1][y]>m[x+1][y]+distmap[x][y] and not visited[x+1][y]:
      distmap[x+1][y]=m[x+1][y]+distmap[x][y]
      originmap[x+1][y]=np.ravel_multi_index((x, y),  (max_val, max_val))
  # move to x-1][y
  if x>0:
    if distmap[x-1][y]>m[x-1][y]+distmap[x][y] and not visited[x-1][y]:
      distmap[x-1][y]=m[x-1][y]+distmap[x][y]
      originmap[x-1][y]=np.ravel_multi_index((x, y), (max_val, max_val))
  # move to x][y+1
  if y < max_val-1:
    if distmap[x][y+1]>m[x][y+1]+distmap[x][y] and not visited[x][y+1]:
      distmap[x][y+1]=m[x][y+1]+distmap[x][y]
      originmap[x][y+1]=np.ravel_multi_index((x, y), (max_val, max_val))
  # move to x][y-1
  if y>0:
    if distmap[x][y-1]>m[x][y-1]+distmap[x][y] and not visited[x][y-1]:
      distmap[x][y-1]=m[x][y-1]+distmap[x][y]
      originmap[x][y-1]=np.ravel_multi_index((x, y), (max_val, max_val))

  visited[x][y]=True
  dismaptemp=distmap
  dismaptemp[np.where(visited)]=np.Infinity
  # now we find the shortest path so far
  minpost=np.unravel_index(np.argmin(dismaptemp), np.shape(dismaptemp))
  x, y=minpost[0], minpost[1]
  if x==max_val-1 and y==max_val-1:
    finished=True
  count=count+1

#Start backtracking to plot the path  
mattemp=m
x, y=max_val-1, max_val-1
path=[]
mattemp[int(x)][int(y)]=np.nan

while x>0.0 or y>0.0:
  path.append((x, y))
  xxyy=np.unravel_index(int(originmap[int(x)][int(y)]), (max_val, max_val))
  x, y=xxyy[0], xxyy[1]
  mattemp[int(x)][int(y)]=np.nan
path.append([int(x)][int(y)])

t2 = time.perf_counter()
print(t2 - t1, "seconds")
print('The path length is: '+ str(distmap[max_val-1][max_val-1]))
