from collections import deque

result = 1

def solution(n,a,b):
    global result

    d = deque([[i, i + 1] for i in range(1, n+1, 2)])    
    w = [a, b]
    
    m = n // 2
    index = 0
    while(True):
        fight = []

        a1, b1 = d.popleft()
        
        if(a1 in w and b1 in w):
            break
            
        if(a1 in w):
            fight.append(a1)
            
        if(b1 in w):
            fight.append(b1)
            
        a2, b2 = d.popleft()
        
        if(a2 in w and b2 in w):
            break
        
        if(a2 in w):
            fight.append(a2)
            
        if(b2 in w):
            fight.append(b2)

        
        while(len(fight) < 2):
            fight.append(-1)

        d.append(fight)
        
        index += 1
        if(index == m // 2):
            m = m // 2
            result += 1
            index = 0

    answer = result
    return answer
