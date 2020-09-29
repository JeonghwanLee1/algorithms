# def print_graph(graph):
#     for row in graph:
#         print()
#         for elem in row:
#             print(elem,end=' ')
#     print()

import sys

H, W = map(int,input().split())
graph = [[] for _ in range(H)]
count_graph =[[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
    graph[i] = list(sys.stdin.readline())



steps = [(-1,1),(1,1),(0,1)]
all_steps = [(-1,-1),(-1,0),(-1,1),
             (0,-1),(0,1),
             (1,-1),(1,0),(1,1)]
flag = True
answer = -1

#first
hubos = []
flag = False
answer_flag = True

for i in range(1, H - 1):
    left = 3
    middle = [graph[i][0], graph[i-1][0], graph[i+1][0]].count('.')

    for j in range(0, W - 1):

        right = 0
        for step in steps:
            ni = i + step[0]
            nj = j + step[1]
            if graph[ni][nj] == '.':
                right += 1

        count = left+middle+right
        count_graph[i][j] = count


        if graph[i][j] != '.':
            if count >= int(graph[i][j]):
                flag = True
                hubos.append((i, j))

        left = middle
        middle = right

for i, j in hubos:
    graph[i][j] = '.'
answer += 1

adj = [[[] for _ in range(W)] for _ in range(H)]

for i in range(H):
    for j in range(W):
        for step in all_steps:
            _di,_dj = step
            _ni,_nj = i+_di,j+_dj
            adj[i][j].append((_ni,_nj))

while flag:
    visited = [[False for _ in range(W)] for _ in range(H)]
    check_list = []
    for hubo in hubos:
        for ni,nj in adj[hubo[0]][hubo[1]]:
            if not visited[ni][nj]:
                check_list.append((ni,nj))
                count_graph[ni][nj]+=1
                visited[ni][nj] = True
    hubos = []
    flag = False
    answer_flag = True
    for i,j in check_list:
        count = count_graph[i][j]
        if graph[i][j] != '.':
            if count >= int(graph[i][j]):
                flag = True
                hubos.append((i,j))

    for i,j in hubos:
        graph[i][j] = '.'
    answer+=1
    next = hubos[:]

print(answer)
