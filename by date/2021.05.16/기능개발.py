from collections import deque
import math

def get_result(progresses, speeds):
    result = []
    days = []
    
    for p, s in zip(progresses, speeds):
        days.append(math.ceil((100-p)/s))
            
    q = deque(days)
        
    while(len(q) != 0):
        cnt = 1
        pre = q.popleft()
        while(len(q) != 0):
            current = q.popleft()
            if(pre >= current):
                cnt += 1
                
            else:
                q.appendleft(current)
                break
                
        result.append(cnt)
        
    return result
        

def solution(progresses, speeds):
    answer = get_result(progresses, speeds)
    return answer