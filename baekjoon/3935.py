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

    town_rain = [0 for _ in range(17)]
    town_sun = [[] for _ in range(17)]
    for day in range(N):
        inp = input().split()
        for i,elem in enumerate(inp):
            if elem == '1':
                town_sun[i+1].append(day)
    
    #dfs
    stack = [(5,0)]    #position,depth
    while stack:
        main_flag = False
        pos,depth = stack.pop()
        if depth == N:
            main_flag = True
            continue

        for nei in c_graph[pos]:
            flag1 = True
            for town in c_map[nei]:
                if depth in town_sun[town]:
                    flag1 = False
                    break
            if flag1:
                stack.append((nei,depth+1))
                
                for town in c_map[nei]:
                    town_rain[nei] = 0
        




    #print(town_sun)

