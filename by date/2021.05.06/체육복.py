student_num = 0
is_having = []
remain = []

def renting(student, having_s):
    global remain, is_having
    is_having[student] = True
    remain[having_s] = False
    
def set_student_num(n):
    global student_num
    student_num = n

def set_is_having(lost):
    global is_having
    is_having = [True for _ in range(student_num + 2)]
    is_having[0] = False
    is_having[-1] = False
    
    for l in lost:
        is_having[l] = False
    
def set_remain(reserve):
    global remain
    remain = [False for _ in range(student_num + 2)]
    
    for r in reserve:
        remain[r] = True
    
def setting_two_piece():
    for r in range(1, student_num+1):
        if(remain[r] and not is_having[r]):
            renting(r, r)
    
def init(n, lost, reserve):
    set_student_num(n)
    set_is_having(lost)
    set_remain(reserve)
    setting_two_piece()
    
def is_left(student):
    if(remain[student - 1]):
        return True
    return False
 
def is_right(student):
    if(remain[student + 1]):
        return True
    return False
    
def rent():
    # False의 좌우를 보고 친구가 remain이라면 왼쪽부터 받자.
    for student in range(1, student_num + 1):
        if(not is_having[student]):
            if(is_left(student)):
                renting(student, student - 1)
                
            elif(is_right(student)):
                renting(student, student + 1)        
                
def get_result():
    result = sum(is_having)
    return result
    
def solution(n, lost, reserve):
    init(n, lost, reserve)
    rent()
    answer = get_result()
    return answer