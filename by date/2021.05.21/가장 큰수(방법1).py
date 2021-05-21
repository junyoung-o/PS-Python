import functools

def compare(a, b):
    t1 = a + b
    t2 = b + a
    
    if(t1 > t2):
        return 1
    elif(t1 == t2):
        return 0
    else:
        return -1

def get_result(numbers):
    list_ = list(map(str, numbers))
    list_ = sorted(list_, reverse = True, key = functools.cmp_to_key(compare))
    result = str(int("".join(list_)))
    return result
    
def solution(numbers):    
    answer = get_result(numbers)
    return answer