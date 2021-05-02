def is_power(n):
    root = n ** (1/2) 
    if(root == int(root)):
        return True
    return False

def get_result(n):
    return ((n ** (1/2)) + 1) ** 2

def solution(n):
    if(is_power(n)):
        answer = get_result(n)
    else:
        answer = -1
    return answer