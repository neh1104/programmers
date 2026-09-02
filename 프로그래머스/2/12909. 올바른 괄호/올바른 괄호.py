def solution(s):
    isit = 0
    for i in s:
        if i == '(':
            isit += 1
        elif i == ')' and isit > 0:
            isit -= 1
        else:
            return False
    if isit != 0:
        return False
    return True