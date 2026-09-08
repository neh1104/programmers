def solution(n):
    answer = []
    def hanoi(n, s, e, v):
        if n == 1:
            answer.append([s, e])
            return 
        hanoi(n-1, s, v, e)
        
        answer.append([s, e])
        
        hanoi(n-1, v, e, s)
    hanoi(n, 1, 3, 2)
    return answer