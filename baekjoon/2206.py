import collections
import sys

N,M = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(sys.stdin.readline())
start = (0,0)
goal = (N-1,M-1)
steps = ((1,0),(-1,0),(0,1),(0,-1))

queue = collections.deque([(start,set([start]),True)])
result = []
flag = False
while queue:
    pos,path,count = queue.popleft()
    i,j = pos
    if pos == goal:
        print(len(path))
        flag = True
        break
        continue

    for step in steps:
        di,dj = step
        ni,nj = i+di,j+dj
        if 0<=ni<N and 0<=nj<M and (ni,nj) not in path:
            if graph[ni][nj] == '0':
                new_path = path.copy()
                new_path.add((ni,nj))
                queue.append(((ni,nj),new_path,count))
            elif graph[ni][nj] == '1' and count:
                new_path = path.copy()
                new_path.add((ni, nj))
                queue.append(((ni,nj),new_path,False))

if not flag:
    print(-1)
#else:
#    result.sort(key=len)
#    print(len(result[0]))
