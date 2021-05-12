m_dic = {1 : 31,
         2 : 29,
         3 : 31,
         4 : 30,
         5 : 31,
         6 : 30,
         7 : 31,
         8 : 31,
         9 : 30,
         10 : 31,
         11 : 30,
         12 : 31}

d_list = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
d_index = 5

def get_first_day(a):
    global d_index
    
    for i in range(1, a):
        d_index = (d_index + m_dic[i] % 7) % 7

def get_day(b):
    global d_index
    
    m = b % 7
    if(m == 0):
        m = 7
    m -= 1
    
    d_index = (d_index + m) % 7
    
def init(a, b):
    get_first_day(a)
    get_day(b)
    
        
def solution(a, b):
    init(a, b)
    answer = d_list[d_index]
    return answer