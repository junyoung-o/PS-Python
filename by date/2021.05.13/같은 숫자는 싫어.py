def get_result(arr):
    pre = arr[0]
    result= [pre]
    for i in arr[1:]:
        if(i != pre):
            result.append(i)
            pre = i
    return result

def solution(arr):
    answer = get_result(arr)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    return answer