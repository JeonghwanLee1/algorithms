from functools import reduce
import sys


N = int(input())
nums = []
for _ in range(N):
	nums.append(int(sys.stdin.readline()))
nums.sort()
diffs = []

for i in range(1,len(nums)):
	diff = nums[i]-nums[i-1]
	diffs.append(diff)

def get_gcd(a,b):
	if b == 0 :
		return a
	return get_gcd(b,a%b)

gcd = reduce(get_gcd,diffs)
temp = []

for i in range(2,int(gcd**(1/2)+1)):
	if gcd%i==0:
		print(i,end=" ")
		temp.append(i)

for i in temp[::-1]:
	if gcd//i not in temp:
		print(gcd//i,end=" ")

print(gcd)
