is_visit = [False for _ in range(8)]
edge = [[] for _ in range(8)]
result = []

def set_visit(n):
    global is_visit
    is_visit = [False for _ in range(n)]
    
def link(a, b):
    global edge
    edge[a].append(b)
    edge[b].append(a)
    
def set_edge(n):
    global edge
    edge = [[] for _ in range(8)]
    
    for i in range(n):
        for j in range(i + 1, n):
            link(i, j)

def init(n):
    set_visit(n)
    set_edge(n)

def get_num_list(numbers):
    num_list = []
    for i in numbers:
        num_list.append(i)
    return num_list

def dfs(v, s, num_list):
    if(is_visit[v]):
        return
    
    is_visit[v] = True
    s += num_list[v]
    result.append(int(s))
    
    for next_v in edge[v]:
        if(not is_visit[next_v]):
            dfs(next_v, s, num_list)
            is_visit[next_v] = False


def set_result(num_list):
    for i in range(len(num_list)):
        init(len(num_list))
        dfs(i, "", num_list)

def is_p(num):
    if(num <= 1):
        return False
    
    if(num == 2):
        return True
    
    for i in range(2, num):
        if(num % i == 0):
            return False
    return True
        
def get_result():
    p_result = 0
    s_result = set(result)
    for r in s_result:
        if(is_p(r)):
            p_result += 1
            
    return p_result
        
def solution(numbers):
    num_list = get_num_list(numbers)
    set_result(num_list)
    answer = get_result()
    return answer