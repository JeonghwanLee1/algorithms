import collections
H ,W = map(int,input().split())
graph = [['?' for _ in range(W)] for _ in range(H)]
waters = []
steps = [(0,1),(0,-1),(1,0),(-1,0)]
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

queue = collections.deque([start])
while queue:
    for water in waters:
        i, j = water
        for step in steps:
            di,dj = step
            ni,nj = i+di,j+dj
            if 0<=ni<H and 0<=nj<W:
                water.append((ni,nj))

    pos = queue.popleft()






    









    
    




