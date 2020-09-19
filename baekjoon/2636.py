def print_graph(graph):
    for elem in graph:
        print(elem)
    print()

n, m = map(int,input().split())
board = []
graph = []
for _ in range(n):
    board.append(input().split())

stack = [(0,0)]
visited = []
for _ in range(n):
    tmp = []
    for _ in range(m):
        tmp.append(False)
    visited.append(tmp)

while stack:
    x,y = stack.pop()



    



print(max)
print(answer)
