def print_graph(graph):
    for elem in graph:
        print(''.join(elem))
    print()


def refresh(graph):
    n = 12
    m = 6
    for col in range(m):
        for row in range(n-2,-1,-1):
            i,j = row,col
            while i<n-1:
                if graph[i+1][j] == '.':
                    graph[i+1][j] = graph[i][j]
                    graph[i][j] = '.'
                    i = i+1
                else:
                    break



def get_steps(i, j):
    steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    result = []
    for step in steps:
        ni = step[0] + i
        nj = step[1] + j
        if 0 <= ni < 12 and 0 <= nj < 6:
            result.append((ni, nj))
    return result


def pang(graph):
    n = 12
    m = 6
    points = []

    for i in range(n):
        for j in range(m):
            if graph[i][j] != '.':
                points.append((i, j))

    result = []
    #print(points)
    for point in points:
        visited = [point]
        stack = [point]
        color = graph[point[0]][point[1]]
        while stack:
            pos = stack.pop()
            for nei in get_steps(pos[0], pos[1]):

                if graph[nei[0]][nei[1]] == color and nei not in visited:
                    stack.append(nei)
                    visited.append(nei)

        if len(visited) >= 4:
            result.append(visited)

    for visit in result:
        for pos in visit:
            graph[pos[0]][pos[1]] = '.'


    if result:
        refresh(graph)
        return True
    else:
        return False


# main
graph = []
for _ in range(12):
    row = list(input())
    graph.append(row)

chain = 0
while pang(graph):
    #print_graph(graph)
    chain+=1

print(chain)