import collections
def check_water(water_graph,depth):
    pass

H ,W = map(int,input().split())
graph = [['?' for _ in range(W)] for _ in range(H)]
steps = [(0,1),(0,-1),(1,0),(-1,0)]
waters = []
depth_prev = -1

for i in range(H):
    row = input()
    for j in range(W):
        graph[i][j] = row[j]
        if row[j] == 'S':
            start = (i,j)
        elif row[j] == 'D':
            goal = (i,j)
        elif row[j] == '*':
            waters.append((i,j))

queue = collections.deque([[start,0]])
flag = True
visited = [start]
while queue:

    pos,depth = queue.popleft()
    i, j = pos

    if depth == depth_prev:
        pass
    else:
        new_waters = []
        for water in waters:
            wi,wj = water
            for wstep in steps:
                wdi,wdj = wstep
                wni,wnj = wi+wdi,wj+wdj
                if 0<=wni<H and 0<=wnj<W and graph[wni][wnj] == '.' and (wni,wnj) not in waters:
                    new_waters.append((wni,wnj))
                    graph[wni][wnj] = '*'
        waters = new_waters

    for step in steps:
        di, dj = step
        ni, nj = i + di, j + dj
        if 0<=ni<H and 0<=nj<W:
            if (ni,nj) not in visited and graph[ni][nj] == "." :
                visited.append((ni,nj))
                queue.append([(ni,nj),depth+1])

            elif graph[ni][nj] == 'D':
                print(depth+1)
                flag = False
                queue = []
                break
    depth_prev = depth

if flag:
    print('KAKTUS')
