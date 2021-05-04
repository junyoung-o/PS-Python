left = 10
right = 11

left_col = [1, 4, 7]
right_col = [3, 6, 9]

edge = [[] for _ in range(12)]
is_visit = [False for _ in range(12)]
min_visit = 0

def link(a, b):
    global edge
    edge[a].append(b)
    edge[b].append(a)

def sort_edge():
    global edge
    for i in range(len(edge)):
        edge[i] = sorted(edge[i])
        
def set_edge():
    link(1, 2)    
    link(1, 4)    
    link(2, 3)    
    link(2, 5)    
    link(3, 6)    
    link(4, 5)    
    link(4, 7)    
    link(5, 6)    
    link(5, 8)    
    link(6, 9)    
    link(7, 8)    
    link(7, 10)    
    link(8, 9)    
    link(8, 0)    
    link(9, 11)    
    link(0, 10)    
    link(0, 11)    

    sort_edge()
    
def set_visit():
    global is_visit
    is_visit = [False for _ in range(12)]
    
def set_min_visit():
    global min_visit
    min_visit = 100
    
def init():
    set_edge()
    set_visit()
    set_min_visit()

def init_dfs():
    set_visit()
    set_min_visit()
    
def set_left(num):
    global left
    left = num

def set_right(num):
    global right
    right = num
    
def is_in_col(num):
    if(num in left_col or num in right_col):
        return True
    return False

def in_col(num):
    if(num in left_col):
        set_left(num)
        return "L"
    
    set_right(num)
    return "R"

def distance(v, target, visit):
    global is_visit, min_visit
    
    is_visit[target] = False
    
    if(v == target):
        # print(min_visit, visit)
        min_visit = min(min_visit, visit)
        return
    
    if(is_visit[v]):
        return
    
    is_visit[v] = True
    
    for n in edge[v]:
        if(not is_visit[n]):
            distance(n, target, visit + 1)
            is_visit[n] = False
            

def is_same(num):
    global min_visit
    
    init_dfs()
    distance(left, num, 0)
    left_distance = min_visit
    
    init_dfs()
    distance(right, num, 0)
    right_distance = min_visit
    
    if(left_distance == right_distance):
        return True
    return False

def not_same(num):
    init_dfs()
    distance(left, num, 0)
    left_distance = min_visit
    
    init_dfs()
    distance(right, num, 0)
    right_distance = min_visit
    
    if(left_distance < right_distance):
        set_left(num)
        return "L"
    
    set_right(num)
    return "R"

def get_touch_finger(num, hand):
    if(is_in_col(num)):
        return in_col(num)
    
    if(is_same(num)):
        if(hand == "right"):
            set_right(num)
            return "R"
        else:
            set_left(num)
            return "L"

    else:
        return not_same(num)


def get_result_list(numbers, hand):
    result_list = []
    for num in numbers:
        result_list.append(get_touch_finger(num, hand))
    return result_list
        
def get_result(result_list):
    result = ""
    for r in result_list:
        result += r
    return result

def solution(numbers, hand):
    init()
    result_list = get_result_list(numbers, hand)
    answer = get_result(result_list)
    return answer