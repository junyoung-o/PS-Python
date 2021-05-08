def solution(d, budget):
    s_list = sorted(d)
    
    index = 0
    answer = 0
    target = budget
    
    while(index < len(d)):
        if(target - s_list[index] < 0):
            break
            
        target -= s_list[index]
        answer+= 1
        index += 1
        
    return answer