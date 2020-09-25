def refresh(graph):
    n = len(graph)
    m = len(graph[0])
    blanks = [0 for _ in range(m)]
    for col in range(m):
        count = 0
        for row in range(n-1,-1,-1):
            if graph[row][col] != '.':
                blanks[col] = count
                break
            else:
                count+=1
    
    for col in range(m):
        blank = blanks[col]
        if blank>0:
            for i in range(n-1,n-1-blank,-1):
                graph[i] = graph[i-blank]
                


