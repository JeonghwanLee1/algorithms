N = int(input())
M = int(input())
graph = [[] for _ in range(N)]
for _ in range(M):
	fr,to = list(map(int,input().split()))
	graph[fr-1].append(to-1)
	graph[to-1].append(fr-1)

queue = [0]
visited = [0]
while queue:
	now = queue.pop()
	adj = graph[now]
	for elem in adj:
		if elem not in visited:
			queue.append(elem)
			visited.append(elem)

print(len(visited)-1)





