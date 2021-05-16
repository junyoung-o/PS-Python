from queue import PriorityQueue

def shuffle(a, b):
    return a + (b * 2)

def get_result(scoville, K):
    if(scoville.count(0) >= 2):
        return -1
    
    q = PriorityQueue()
    
    for s in scoville:
        q.put(s)
    
    result = 0
    while(not q.empty()):
        x = q.get()
        if(x >= K):
            break
            
        result += 1
        y = q.get()
        q.put(shuffle(x, y))
        
    return result    

def solution(scoville, K):
    answer = get_result(scoville, K)
    return answer