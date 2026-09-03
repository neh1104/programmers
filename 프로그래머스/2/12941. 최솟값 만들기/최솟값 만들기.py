def solution(A,B):
    A.sort()
    B.sort(reverse = True)
    s = 0
    for i, j in zip(A, B):
        s += i*j
        
    return s