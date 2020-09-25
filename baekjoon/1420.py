def dfs_any(graph,start,N,M):
    stack = [start]
    deltas = [(0,1),(0,-1),(1,0),(-1,0)]
    visited = [[False for _ in range(M)] for _ in range(N)]

    while stack:
        pos = stack.pop()
        n,m = pos
        for delta in deltas:
            nn = delta[0]+n
            nm = delta[1]+m
            if 0 <= nn < N and 0 <= nm < M and not visited[nn][nm]:
                if graph[nn][nm] == '.':
                    visited[nn][nm] = True
                    stack.append((nn,nm))
                elif graph[nn][nm] == 'H':
                    return True
    return False


def dfs(graph, start,N,M,pathes):
    routes = []
    stack = [(start, set([start]))]
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while stack:
        pos, path = stack.pop()
        n, m = pos

        for delta in deltas:
            nn = delta[0] + n
            nm = delta[1] + m
            if 0 <= nn < N and 0 <= nm < M and (nn, nm) in pathes - path:
                if graph[nn][nm] == '.':
                    npath = path.copy()
                    npath.add((nn, nm))
                    stack.append(((nn, nm), npath))
                elif graph[nn][nm] == 'H':
                    routes.append(path)
    return routes

def solution():
    from itertools import combinations
    N, M = map(int,input().split())
    graph = []
    pathes = set()

    for i in range(N):
        row = input()
        tmp = []
        for j,elem in enumerate(row):
            tmp.append(elem)
            pathes.add((i,j))
            if elem == 'K':
                start = (i,j)
            elif elem == 'H':
                goal = (i,j)
        graph.append(tmp)

    routes = dfs(graph,start,N,M,pathes)
    if routes:
        result = routes[0]
    else:
        print(0)
        return 0

    for route in routes:
        result = result.intersection(route)

    #print(routes)
    start_end = set([start,goal])
    result = result-start_end
    answer = len(result)

    for i in range(len(result),0,-1):
        comb = list(combinations(result,i))
        if comb:
            #print(comb)
            for elem in comb:
                #print(elem)
                n = elem[0][0]
                m = elem[0][1]
                graph[n][m] = '#'

            if dfs_any(graph,start,N,M):
                #원상복귀
                for elem in comb:
                    n = elem[0]
                    m = elem[1]
                    graph[n][m] = '.'
                    answer = i
                continue

    print(answer)
    return

solution()