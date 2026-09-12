def solution(routes):
    routes.sort(key = lambda x: (x[1], x[0]))
    n = len(routes)
    print(routes)
    
    cnt = 0; idx = 0
    while True:
        _, e = routes[idx]
        cnt += 1
        
        if idx == n-1:
            return cnt
        
        while True:
            idx += 1
            
            s, _ = routes[idx]
            if e < s:
                break
            
            if idx == n-1:
                return cnt