def get_result(arr, divisor):
    result = []
    for i in arr:
        if(i % divisor == 0):
            result.append(i)
            
    if(len(result) == 0):
        return [-1]
    return sorted(result)
    
def solution(arr, divisor):
    answer = get_result(arr, divisor)
    return answer