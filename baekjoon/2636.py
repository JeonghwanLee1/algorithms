n, m = map(int,input().split())
board = []
graph = []
for _ in range(n):
    board.append(input().split())

for _ in range(n):
    row = []
    for _ in range(m):
        row.append(0)
    graph.append(row)

#위에서 아래
for i,row in enumerate(board):
    for j,elem in enumerate(row):
        if elem == '1' and 0 < j < m - 1:
            tmp = graph[i-1][j]+1
            graph[i][j] = tmp
        elif 0 < i < n-1:
            tmp = graph[i-1][j]+1
            graph[i][j] = tmp

for elem in graph:
    print(elem)
print()

#아래에서 위
for i in range(n-2,-1,-1):
    for j in range(m):
        if board[i][j] == '1':
            tmp = graph[i + 1][j] + 1
            if tmp < graph[i][j]:
                graph[i][j] = tmp
        else:
            tmp = graph[i + 1][j]+1
            if tmp < graph[i][j]:
                graph[i][j] = tmp


for elem in graph:
    print(elem)
print()

#좌에서 우
for i, row in enumerate(board):
    for j, elem in enumerate(row):
        if elem == '1':
            tmp = graph[i][j-1] + 1
            if tmp < graph[i][j]:
                graph[i][j] = tmp
        elif j>0:
            tmp = graph[i][j - 1]+1
            if tmp < graph[i][j]:
                graph[i][j] = tmp

for elem in graph:
    print(elem)
print()

#우에서 좌
for i in range(n):
    for j in range(m-2,-1,-1):
        if board[i][j] == '1':
            tmp = graph[i][j+1] + 1
            if tmp < graph[i][j]:
                graph[i][j] = tmp
        else:
            tmp = graph[i][j + 1]+1
            if tmp < graph[i][j]:
                graph[i][j] = tmp

for elem in graph:
    print(elem)

#find max
max = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]>max:
            max = graph[i][j]

answer = 0

for elem in graph:
    print(elem)
print()
for i in range(n):
    for j in range(m):
        if graph[i][j] == max and board[i][j]=='1':
            answer+=1

print(max)
print(answer)