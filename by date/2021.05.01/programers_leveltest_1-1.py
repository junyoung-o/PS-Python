def get_result(n):
    str_n = str(n)

    result = 0
    for i in str_n:
        result += int(i)
    return result

def solution(n):
    answer = get_result(n)

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer