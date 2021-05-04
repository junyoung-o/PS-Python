poketmon_dic = {}
choice_num = 0

def set_poketmon_dic(nums):
    global poketmon_dic
    for poketmon in nums:
        if(poketmon in poketmon_dic.keys()):
            poketmon_dic[poketmon] += 1
        else:
            poketmon_dic[poketmon] = 1

def set_choice_num(nums):
    global choice_num
    choice_num = len(nums) // 2
            
def init(nums):
    set_poketmon_dic(nums)
    set_choice_num(nums)

def get_result():
    if(choice_num < len(list(poketmon_dic.keys()))):
        return choice_num
    return len(list(poketmon_dic.keys()))
    
def solution(nums):
    init(nums)
    answer = get_result()
    return answer