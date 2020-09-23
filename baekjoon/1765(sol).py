n = int(input())
m = int(input())
friends = {}
enemies = {}
visited = [False for _ in range(n)]
for i in range(n):
    friends[i] = [i]
    enemies[i] = []
for _ in range(m):
    rel, a, b = input().split()
    if rel == 'F':
        friends[int(a)-1].append(int(b)-1)
        friends[int(b)-1].append(int(a)-1)
    elif rel == 'E':
        enemies[int(a)-1].append(int(b)-1)
        enemies[int(b)-1].append(int(a)-1)

for i in range(n):
    for enemy in enemies[i]:
        friends[i].extend(enemies[enemy])


vals = list(map(list,(map(set,list(friends.values())))))
vals.sort(key=len,reverse=True)
#print(vals)
teams = 0
for val in vals:
    flag = True
    for elem in val:
        if visited[elem]:
            flag= False
            break
        else:
            visited[elem]=True
    if flag:
        teams+=1
print(teams)
