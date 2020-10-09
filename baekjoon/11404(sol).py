import sys
def print_graph(graph):
    for row in graph:
        print(" ".join(map(str,row)))

n = int(input())
m = int(input())
maxi = 100001*n
graph = [[maxi for _ in range(n)] for _ in range(n)]

for _ in range(m):
    row = map(int,sys.stdin.readline().split())
    fr,to,cost = row
    graph[fr-1][to-1] = min([cost,graph[fr-1][to-1]])

for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k]+graph[k][j]:
                graph[i][j] = graph[i][k]+graph[k][j]

for i in range(n):
    for j in range(n):
        if graph[i][j] == maxi:
            graph[i][j] = 0

print_graph(graph)