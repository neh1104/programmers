def solution(begin, target, words):
    
    def can_move(s1, s2):
        return sum(i != j for i, j in zip(s1, s2)) == 1
    
    from collections import deque
    n = len(words)
    q = deque([(begin, 0)])
    vt = [0 for _ in range(n)]
    
    def bfs():
        while q:
            s, idx = q.popleft()
            if s == target:
                return idx
            for i in range(n):
                if vt[i]:
                    continue
                if can_move(s, words[i]):
                    q.append((words[i], idx+1))
                    vt[i] = 1
        return 0
    
    return bfs()