A = [6,2,1,5,4,3]

def solution(A):
    A_sor = sorted(A)
    target = set(range(1,len(A)))
    blanks = set(A_sor)-target

    for i, elem in enumerate(A_sor):
        min_ele = 200000
        for ele in blanks:
            if abs(ele-elem)<min_ele:
                min_ele = ele




    print(A_sor)
    prev = A_sor[0]
    result = 0

    right = A_sor[-1] + 1
    left = A_sor[0] - 1