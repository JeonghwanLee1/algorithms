def distance(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

t = int(input())
for _ in range(t):
    n = int(input())
    start = list(map(int,input().split()))
    conv = []
    for _ in range(n):
        conv.append(list(map(int,input().split())))
    goal = list(map(int,input().split()))

    #dfs
    stack = [start]
    visited = [False for _ in range(n)]
    flag = True
    while stack:
        pos = stack.pop()
        if distance(pos,goal)<=1000:
            print("happy")
            flag = False
            break
        
        for i,elem in enumerate(conv):
            if not visited[i] and distance(pos,elem)<=1000:
                stack.append(elem)
                visited[i] = True
    if flag:
        print("sad")









