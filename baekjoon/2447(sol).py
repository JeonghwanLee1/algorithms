def merge_str(strings): #2차원 배열 9개 -> 2차원 배열
    n = len(strings[0])    # 한 변의 길이
    result = [[] for _ in range(n*3)]
    for string in strings[0:3]:
        for i in range(n):
            result[i].extend(string[i])

    for string in strings[3:6]:
        for i in range(n):
            result[i+n].extend(string[i])

    for string in strings[6:9]:
        for i in range(n):
            result[i+2*n].extend(string[i])

    return result

def star(N):
    if N == 3:
        return [['*',"*",'*'],['*'," ",'*'],['*',"*",'*']]
    prev = star(N//3)
    return merge_str([prev,prev,prev,
                      prev,[[' ' for _ in range(N//3)] for _ in range(N//3)],prev,
                      prev,prev,prev])

def print_arr(arr):
    for row in arr:
        print("".join(row))

N = int(input())
print_arr(star(N))
