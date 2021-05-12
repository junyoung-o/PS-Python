
def get_three(n):
    stack = []
    q = n
    while(True):
        if(q == 0):
            break
        r = q % 3
        q = q // 3
        stack.append(r)
        
    return stack

def get_ten(stack):
    digit = 1
    result = 0
    while(len(stack) != 0):
        result += stack.pop() * digit
        digit *= 3
    return result

def solution(n):
    stack = get_three(n)
    answer = get_ten(stack)
    return answer