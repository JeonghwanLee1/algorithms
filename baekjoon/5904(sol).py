N = int(input())
k = 0
s_k = 3
k_sk = {k:s_k}

#get_k
while N>s_k:
    s_k = 2*s_k+k+4
    k+=1
    k_sk[k]=s_k

while True:
    if k==0:
        print('m',end=' ') if N==1 else print('o', end=' ')
        break

    #left
    if N<=k_sk[k-1]:
        N = N

    #center
    elif N<=k_sk[k-1]+k+3:
        print('m',end=' ') if N-k_sk[k-1]==1 else print('o', end=' ')
        break

    #right
    else:
        N = N-k_sk[k-1]-(k+3)

    k = k-1
