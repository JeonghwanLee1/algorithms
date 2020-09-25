c_map = {}
for i in range(1,10):
    offset = (i//3)*4 + i%3
    if i%3 == 0:
        offset = offset-1
    tmp = [offset,offset+1,offset+4,offset+5]
    c_map[i] = tmp
#print(c_map)
c_graph = {}
steps = [1,-1,3,-3]
for i in range(1,10):
    tmp = []
    for step in steps:
        if 1<=i+step<=9:
            tmp.append(i+step) 
    c_graph[i] = tmp
#print(c_graph)



while True:
    N = int(input())
    if N == 0:
        break


    town_sun = [[] for _ in range(17)]
    for day in range(N):
        inp = input().split()
        for i,elem in enumerate(inp):
            if elem == '1':
                town_sun[i+1].append(day)
    
    #dfs
    stack = [(5,[5])]    #position,depth,path
    print(town_sun)

    routes = []
    while stack:
        #print(stack)
        main_flag = False
        pos,path = stack.pop()
        depth = len(path)
        if depth == N:
            routes.append(path)
            continue

        for nei in c_graph[pos]: #연결된 구름
            flag1 = True
            for town in c_map[nei]: #연결된 구름의 소속 town
                if depth in town_sun[town]:
                    flag1 = False
                    break

            if flag1:
                stack.append((nei,path+[nei]))

    town_rain = [0 for _ in range(17)]
    result_flag = True

