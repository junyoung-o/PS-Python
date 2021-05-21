from itertools import permutations

def get_result(numbers):
    list_ = list(map(str, numbers))
    list_ = list(permutations(list_, len(list_)))
    list_ = list(map(lambda x : "".join(x), list_))
    list_ = sorted(list_, reverse = True)
    return list_[0]
    
def solution(numbers):
    answer = get_result(numbers)
    return answer