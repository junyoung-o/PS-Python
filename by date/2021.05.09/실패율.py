stage_dic = {}
rate_dic = {}
people_n = 0

def set_dic(stages):
    global stage_dic
    
    for s in stages:
        if(s in stage_dic):
            stage_dic[s] += 1
        else:
            stage_dic[s] = 1

def set_n(stages):
    global people_n
    people_n = len(stages)
            
def set_rate(N):
    global rate_dic
    list_ = sorted(stage_dic.items(), reverse = True)
    stored_n = 0
    for k, v in list_:
        stored_n += v
        
        if(v == 0):
            rate_dic[k] = 0
        if(k in range(1, N + 1)):
            rate_dic[k] = v / stored_n
    
        
def init(N,stages):
    set_dic(stages)
    set_n(stages)
    set_rate(N)

def set_result_ls():
    list_ = sorted(list(rate_dic.items()), key = lambda x : (x[1], x[0]))
    list_ = sorted(list_, key = lambda x : x[1], reverse = True)
    return list_
    
def get_result(n, list_):
    result = []
    
    for k, v in list_:
        result.append(k)
    
    for i in range(1, n + 1):
        if(i not in result):
            result.append(i)
    return result
        
    
def solution(N, stages):
    init(N,stages)
    result_ls = set_result_ls()
    answer = get_result(N, result_ls)
    return answer