result = 0

def recur(index, numbers, target, r):
    global result
    
    if(index == len(numbers)):
        if(r == target):
            result += 1
        return
        
    if(index >= len(numbers)):
        return
    
    recur(index + 1, numbers, target, r - numbers[index])
    recur(index + 1, numbers, target, r + numbers[index])

def set_result(numbers, target):
    recur(0, numbers, target, 0)    

def solution(numbers, target):
    set_result(numbers, target)
    answer = result
    return answer