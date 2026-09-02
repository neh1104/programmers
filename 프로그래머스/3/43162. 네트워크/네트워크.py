def solution(n, computers):
    num_cnt = 0
    vt = [0 for _ in range(n)]
    
    def dfs(curr):
        vt[curr] = 1
        for i in range(n):
            if i == curr:
                continue
            if computers[curr][i] == 1 and vt[i] == 0:
                dfs(i)

    for i in range(n):
        if vt[i] == 0:
            dfs(i)
            num_cnt += 1  

    return num_cnt