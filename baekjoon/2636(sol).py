def print_graph(graph):
    for elem in graph:
        print(elem)
    print()

n, m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(input().split())

visited = []
for _ in range(n):
    tmp = []
    for _ in range(m):
        tmp.append(False)
    visited.append(tmp)
visited[0][0] = True
del_list = []
depth = -1
while True:
    visited_copy = visited
    for i in range(n):
        for j in range(m):
            visited_copy[i][j] = False

    depth+=1
    stack = [(0, 0)]
    while stack:
        y,x = stack.pop()
        for delta in (0,-1),(0,1),(1,0),(-1,0):
            new_y = y+delta[0]
            new_x = x+delta[1]
            if not 0<=new_y<n or not 0<=new_x<m:
                continue

            if graph[new_y][new_x] == '1':
                if not visited_copy[new_y][new_x]:
                    visited_copy[new_y][new_x] = True
                    del_list.append((new_y, new_x))

            else:
                if not visited_copy[new_y][new_x]:
                    visited_copy[new_y][new_x] = True
                    stack.append((new_y, new_x))

    if len(del_list) == 0:
        break
    prev = len(del_list)
    while del_list:
        dely,delx = del_list.pop()
        graph[dely][delx] = '0'

print(depth)
print(prev)