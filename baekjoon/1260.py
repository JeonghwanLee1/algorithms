from collections import deque
N,M,V = map(int,input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
	src,dst = map(int,input().split())
	edges[src].append(dst)
	edges[dst].append(src)

for edge in edges:
	edge.sort()

stack = deque([V])
queue = deque([V])

dfs_visited = []
bfs_visited = [V]

#dfs : stack
def dfs(s):
	dfs_visited.append(s)
	for adj in edges[s]:
		if adj not in dfs_visited:
			dfs(adj)
			
def bfs(s):
	queue = deque([V])
	while queue:
		now = queue.popleft()
		for adj in edges[now]:
			if adj not in bfs_visited:
				bfs_visited.append(adj)
				queue.append(adj)

dfs(V)
bfs(V)

print(" ".join(map(str,dfs_visited)))
print(" ".join(map(str,bfs_visited)))
