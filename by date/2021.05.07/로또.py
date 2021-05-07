def count_zero(_list):
    return _list.count(0)

def count_min(min_uo, win):
    cnt = 0
    for num in min_uo:
        if(num in win):
            cnt += 1
    return cnt

def get_grade(num):
    for g in range(7):
        if(g <= 1 and num <= 1):
            return 6
        elif(num == g):
            return 7 - g

def get_result(lottos, win_nums):
    correct_min = count_min(lottos, win_nums)
    correct_max = correct_min + count_zero(lottos)
    # print(correct_max, correct_min)
    return get_grade(correct_max), get_grade(correct_min)

def solution(lottos, win_nums):
    answer = get_result(lottos, win_nums)
    return answer