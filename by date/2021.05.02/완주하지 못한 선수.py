completion = []
participant = []

def set_completion(c):
    global completion
    completion = c
    
def set_participant(p):
    global participant
    participant = p

def init(participant, completion):
    set_completion(completion)
    set_participant(participant)
    
def get_result():
    check_dic = {}
    for h in participant:
        if(h in check_dic.keys()):
            check_dic[h] += 1
        else:
            check_dic[h] = 1
            
    for c in completion:
        check_dic[c] -= 1
    
    check_list = list(check_dic.items())
    for h, check in check_list:
        if(check == 1):
            return h
    
    
def solution(participant, completion):
    init(participant, completion)
    answer = get_result()
    return answer