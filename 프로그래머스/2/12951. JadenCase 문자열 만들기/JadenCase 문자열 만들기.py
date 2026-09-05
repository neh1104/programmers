def solution(s):
    plus = ord('A') - ord('a')
    upper = 1; ls = []

    for i in s:
        if i == ' ':
            ls.append(' ')
            upper = 1
            continue
            
        if upper:
            if i.isalpha() and not(i.isupper()):
                ls.append(chr(ord(i)+plus))
            else:
                ls.append(i)
            upper = 0
        else:
            if i.isupper():
                ls.append(chr(ord(i)-plus))
            else:
                ls.append(i)
    
    return ''.join(ls)