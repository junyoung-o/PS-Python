def get_result(absolutes, signs):
    result = 0
    for index, num in enumerate(absolutes):
        if(signs[index]):
            result += num
        else:
            result -= num
    return result

def solution(absolutes, signs):
    answer = get_result(absolutes, signs)
    return answer