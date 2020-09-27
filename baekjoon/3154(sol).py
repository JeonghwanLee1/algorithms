def effort(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def get_effort(text,graph):    #HHMM
    eff = 0
    for i in range(3):
        #print(eff)
        #print(i,text)
        eff+=graph[int(text[i])][int(text[i+1])]
    return eff

graph = [[0 for _ in range(11)] for _ in range(11)]

for i in range(10):
    for j in range(10):
        a = i%3,i//3
        b = j%3,j//3
        graph[i+1][j+1] = effort(a,b)

zero = (1,3)
for i in range(10):
    a = i%3,i//3
    eff = effort(zero,a)
    graph[0][i+1]= eff
    graph[i+1][0]= eff

hour, minute = map(int,input().split(':'))
hour_cand = [hour]

if minute+60<=99:
    minu_cand = [minute,minute+60]
else:
    minu_cand = [minute]

temp_hour = hour
while True:
    if temp_hour+24<=99:
        temp_hour += 24
        hour_cand.append(temp_hour)
    else:
        break

min_eff = 999
min_hou = -1
min_min = -1
for hou in hour_cand:
    for min in minu_cand:
        text_hou = '0'+str(hou) if hou<10 else str(hou)
        text_min = '0'+str(min) if min<10 else str(min)
        text = text_hou+text_min
        eff = get_effort(text,graph)

        if eff < min_eff:
            min_eff = eff
            min_hou = hou
            min_min = min

res_hou = '0'+str(min_hou) if min_hou<10 else str(min_hou)
res_min = '0'+str(min_min) if min_min<10 else str(min_min)

result = res_hou+':'+res_min
print(result)

