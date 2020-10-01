N,M = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(input())
start = (0,0)
goal = (N-1,M-1)
steps = ((1,0),(-1,0),(0,1),(0,-1))

queue = [(start,0,True)]
visited = []
result = []
flag = True

if M==N and M==1:
    print(1)
    queue = []
    flag = False

while queue:
    pos,depth,count = queue.pop()
    i,j = pos
    if pos == goal:
        print(depth+1)
        flag = False
        break

    for step in steps:
        di,dj = step
        ni,nj = i+di,j+dj
        if 0<=ni<N and 0<=nj<M and (ni,nj) not in visited:
            if graph[ni][nj] == '0':
                queue.append(((ni,nj),depth+1,count))
                visited.append((ni,nj))
            elif graph[ni][nj] == '1' and count:
                queue.append(((ni,nj),depth+1,False))
                visited.append((ni,nj))

if flag:
    print(-1)