def solution(triangle):
    n = len(triangle)
    vt = [[-1 for _ in range(n)] for _ in range(n)]
    
    def dp(r, c):
        if vt[r][c] != -1:
            return vt[r][c]
        if r == n-1:
            return triangle[r][c]
        
        vt[r][c] = max(dp(r+1, c), dp(r+1, c+1)) + triangle[r][c]
        return vt[r][c]

    return dp(0, 0)