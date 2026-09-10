def solution(brown, yellow):
    for i in range(1, brown):
        for j in range(i, brown):
            if 2*i+2*j-4 == brown and (i-2)*(j-2) == yellow:
                return [j, i]