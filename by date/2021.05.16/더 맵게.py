import heapq

def shuffle(a, b):
    return a + (b * 2)

def get_result(scoville, K):
    h = []
    
    for s in scoville:
        heapq.heappush(h, s)
    
    if(len(h) <= 1):
        return -1
    
    if(h[1] == 0):
        return -1
    
    result = 0
    while(len(h) >= 1):
        x = heapq.heappop(h)
        if(x >= K):
            break
        if(len(h) == 0 and x < K):
            return -1
        
        y = heapq.heappop(h)
        heapq.heappush(h, shuffle(x, y))
        result += 1
    
    return result

def solution(scoville, K):
    answer = get_result(scoville, K)
    return answer