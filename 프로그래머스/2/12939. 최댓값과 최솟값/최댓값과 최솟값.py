def solution(s):
    a = list(map(int, s.split(' ')))
    a = [str(min(a)), str(max(a))]
    return ' '.join(a)