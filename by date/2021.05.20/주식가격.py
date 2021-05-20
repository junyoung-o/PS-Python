def get_result(prices):
    result = []
    
    for index, p in enumerate(prices):
        cnt = 0
        while(index + 1 < len(prices)):
            if(p > prices[index+1]):
                cnt += 1
                break
            cnt += 1
            index += 1
                
        result.append(cnt)
                
    return result



def solution(prices):
    return get_result(prices)
