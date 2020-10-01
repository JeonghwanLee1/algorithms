steps = {}
steps['R']=(0,1)
steps['L']=(0,-1)
steps['B']=(1,0)
steps['T']=(-1,0)

steps['RT']=(-1,1)
steps['LT']=(-1,-1)
steps['RB']=(1,1)
steps['LB']=(1,-1)

k,p,n = input().split()
k_pos = (8-int(k[1]),ord(k[0])-ord('A'))
p_pos = (8-int(p[1]),ord(p[0])-ord('A'))
n = int(n)

for _ in range(n):
    #print(k_pos,p_pos)
    command = input()
    ki,kj = k_pos
    pi,pj = p_pos

    di,dj = steps[command]
    nki,nkj = ki+di,kj+dj

    if nki == pi and nkj == pj:
        npi,npj = pi+di,pj+dj
    else:
        npi,npj = pi,pj


    if 0<=nki<8 and 0<=nkj<8 and 0<=npi<8 and 0<=npj<8:
        k_pos = (nki,nkj)
        p_pos = (npi,npj)
        print(k_pos,p_pos)
    else:
        print("stu",k_pos,p_pos)
        continue


k_result = str(chr(ord('A')+k_pos[1]))+str(8-k_pos[0])
p_result = str(chr(ord('A')+p_pos[1]))+str(8-p_pos[0])
print(k_result)
print(p_result)