list_124 = ["1", "2", "4"]
result_list = []

def set_result_list(n):
    global result_list
    result_list = ["" for _ in range(n+1)]
    point = 0
    for i in range(1, 4):
        if(point >= n):
            break
        result_list[i] = list_124[point]
        point+=1
    
def init(n):
    set_result_list(n)
    
def get_result(n):
    global result_list
    init(n)
    
    point = 0
    
    if(4 <= n):
        point = 0
        digit = 1
        for i in range(4, n+1):
            result_list[i] += result_list[digit] + list_124[point]
            point += 1
            if(point == 3):
                point = point % 3
                digit += 1
        
    result = result_list[n]
    
    return result

def solution(n):
    answer = get_result(n)
    return answer