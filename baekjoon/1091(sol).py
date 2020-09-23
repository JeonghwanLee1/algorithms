def solution():
    N = int(input())
    P = list(map(int,input().split()))
    S = list(map(int,input().split()))
    cards = list(range(N))
    target = [set() for _ in range(3)]

    for i,elem in enumerate(P):
        target[elem].add(i)


    #print(N,P,S)
    flag = True
    counts = 0
    #print(N*N*N*N)

    for _ in range(N*N*N*3):
        #print(cards)
        players = [set() for _ in range(3)]
        # distribute
        for i,elem in enumerate(cards):
            idx = i%3
            players[idx].add(elem)

        #check
        #print(target,players)
        sum = 0
        for i,player in enumerate(players):
            sum+=len(player-target[i])
        if sum == 0:
            print(counts)
            return

        new_cards = list(range(N))
        #shuffle
        for i, elem in enumerate(S):
            new_cards[elem]=cards[i]
        #print(new_cards)
        cards = new_cards[:]
        counts+=1

    print(-1)

solution()
