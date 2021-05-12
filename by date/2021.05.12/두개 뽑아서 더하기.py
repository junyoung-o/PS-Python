from itertools import combinations

def get_c(numbers):
    return combinations(numbers, 2)

def get_result(list_):
    result = set()
    for i, j in list_:
        result.add(i + j)

    return sorted(list(result))

def solution(numbers):
    answer = get_result(get_c(numbers))
    return answer