import collections
def print_graph(graph):
    for layer in graph:
        print()
        print()
        for row in layer:
            print()
            for elem in row:
                print(elem,end=" ")
num_goal = 0
M, N, H = map(int,input().split())
graph = []
starts = []
for z in range(H):
    layer = []
    for y in range(N):
        row = input().split()
        for x,elem in enumerate(row):
            if elem == "1":
                starts.append(((z,y,x),1))
                num_goal+=1
            elif elem == "0":
                num_goal+=1
        layer.append(row)
    graph.append(layer)

steps = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
queue = collections.deque(starts)
num = len(starts)
flag = False
depth = 0
visited = starts
while queue:
    if num_goal == num:
        flag = True
        print(depth)
        break

    pos,depth = queue.popleft()
    z,y,x = pos

    for step in steps:
        dx,dy,dz = step
        nx,ny,nz = dx+x,dy+y,dz+z

        if 0<=nx<M and 0<=ny<N and 0<=nz<H and graph[nz][ny][nx] == '0':
            graph[nz][ny][nx] = '1'
            queue.append(((nz,ny,nx),depth+1))
            num+=1

if not flag:
    print(-1)



