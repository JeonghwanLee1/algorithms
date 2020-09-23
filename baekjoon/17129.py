import collections
def bfs():
    n,m = map(int,input().split())
    graph = []
    steps = [(0,1),(1,0),(0,-1),(-1,0)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        row = input()
        for j,elem in enumerate(row):
            if elem == '2':
                start = (i,j)
        graph.append(row)

    queue = collections.deque([(start,1)])

    flag = True
    visited[0][0] = True
    foods = ['3','4','5']
    while queue:
        (i,j),depth = queue.popleft()
        for step in steps:
            ni = step[0]+i
            nj = step[1]+j
            if n>ni>=0 and m>nj>=0 and not visited[ni][nj]:
                if graph[ni][nj] == '0':
                    queue.append(((ni,nj),depth+1))
                    visited[ni][nj] = True
                elif graph[ni][nj] in foods:
                    flag = False
                    print("TAK")
                    print(depth)
                    queue = []
                    return
    print("NIE")

bfs()

