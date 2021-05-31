N, K = map(int,input().split())
numbers = list(map(int, input().split()))
diffs=[numbers[i]-numbers[i-1] for i in range(1,N)]
diffs.sort(reverse=True)
print(sum(diffs[K-1:]))
