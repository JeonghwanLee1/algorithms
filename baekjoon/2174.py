A,B = map(int,input().split())
N,M = map(int,input().split())
inits = []
insts = []
directions = []
import sys

for _ in range(N):
    init = input().split()
    inits.append(init)

for _ in range(M):
    inst = input().split()
    insts.append(inst)

board = [[0 for _ in range(A)] for _ in range(B)]
#print(board)

for i, init in enumerate(inits):
    dir = init[2]
    if dir == 'E':
        directions.append((0,1))
    elif dir == 'W':
        directions.append((0,-1))
    elif dir == 'S':
        directions.append((-1,0))
    elif dir == 'N':
        directions.append((1,0))
    board[int(init[1])-1][int(init[0])-1] = i+1

#print(board)
for inst in insts:
    #print(inst)
    id = int(inst[0])
    dir = inst[1]
    for _ in range(int(inst[2])):
        if dir == 'L':
            di,dj = directions[id-1]
            if di == -1:
                directions[id-1] = (0,1)
            elif di == 1:
                directions[id-1] = (0,-1)
            elif dj == -1:
                directions[id-1] = (-1,0)
            elif dj == 1:
                directions[id-1] = (1,0)

        elif dir == 'R':
            di, dj = directions[id - 1]
            if di == -1:
                directions[id - 1] = (0, -1)
            elif di == 1:
                directions[id - 1] = (0, 1)
            elif dj == -1:
                directions[id - 1] = (1, 0)
            elif dj == 1:
                directions[id - 1] = (-1, 0)

        elif dir == 'F':
            j,i = (int(inits[id-1][0])-1,int(inits[id-1][1])-1)
            ni,nj = (directions[id-1][0]+i,directions[id-1][1]+j)

            if 0<=ni<B and 0<=nj<A:

                if board[ni][nj] != 0:
                    print('Robot', id ,'crashes into robot', board[ni][nj])
                    sys.exit(0)

                board[ni][nj] = id
                board[i][j] = 0

                inits[id-1][0] = str(nj+1)
                inits[id-1][1] = str(ni+1)


            else:
                print("Robot", id, 'crashes into the wall')
                sys.exit(0)
        #print(board)
print("OK")