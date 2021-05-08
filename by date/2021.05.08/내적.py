def get_result(a, b):
    result = 0
    for i, j in zip(a, b):
        result += i * j
    return result

def solution(a, b):
    answer = get_result(a, b)
    return answer