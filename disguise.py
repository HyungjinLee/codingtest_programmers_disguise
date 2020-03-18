import collections

def solution(clothes):
    answer = 1
    c = collections.Counter([x[1] for x in clothes]) 
    print(c)
    for k,v in c.items() :
        answer *= (v+1)
    answer -= 1
    
    return answer