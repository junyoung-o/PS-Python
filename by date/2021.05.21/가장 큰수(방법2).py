def get_list(numbers):
    return sorted(numbers, reverse = True, key = lambda x : str(x) * 4)

def get_result(numbers):
    list_ = get_list(numbers)
    list_ = list(map(str, list_))  
    result = str(int("".join(list_)))
    return result

def solution(numbers):    
    answer = get_result(numbers)
    return answer
