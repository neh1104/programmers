def solution(m, n, puddles):
    vt = [[1 for _ in range(m)] for _ in range(n)]
    for i, j in puddles:
        vt[j-1][i-1] = 0
        
    for i in range(1, n):
        if vt[i-1][0] == 0:
            vt[i][0] = 0
        
    for i in range(1, m):
        if vt[0][i-1] == 0:
            vt[0][i] = 0
    
    for i in range(1, n):
        for j in range(1, m):
            if vt[i][j] != 0:
                vt[i][j] = vt[i-1][j]+vt[i][j-1]
                
    print(*vt, sep = '\n')
    return vt[n-1][m-1]%1000000007