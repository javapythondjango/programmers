def solution(n, m, section):
    n=0
    k=0
    for s in section:
        if s> k:
            n+=1
            k = m+s-1
    
    return n