from collections import deque
import numpy as np

def get_result(loc_list, location):
    d = deque(loc_list)
    result = 0
    
    while(len(d) != 2):
        loc, p = d.popleft()
        max_p = max(np.array(list(d))[:, 1])
        if(p < max_p):
            d.append((loc, p))
            
        else:
            result += 1
            if(loc == location):
                return result
        
    if(len(d) == 2):
        loc, p = d.popleft()
        
        if(loc == location):
            return result + 1
        
        else:
            return result + 2
        
    return result

def loc_(priorities):
    loc_list = []
    for i, p in enumerate(priorities):
        loc_list.append((i, p))
    return loc_list

def solution(priorities, location):
    loc_list = loc_(priorities)
    answer = get_result(loc_list, location)
    return answer