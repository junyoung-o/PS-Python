problem_n = 0
student_1 = None
student_2 = None
student_3 = None


def set_problem_n(answers):
    global problem_n
    problem_n = len(answers)

def s_list(x_list):
    return_list = []
    index = 0
    while(len(return_list) < problem_n):
        return_list.append(x_list[index % len(x_list)])
        index += 1
    return return_list
    
def set_student():
    global student_1, student_2, student_3
    student_1 = s_list([1, 2, 3, 4, 5])
    student_2 = s_list([2, 1, 2, 3, 2, 4, 2, 5])
    student_3 = s_list([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    
def init(answers):
    set_problem_n(answers)
    set_student()

def get_score(student_list, answers):
    score = 0
    for s, a in zip(student_list, answers):
        if(s == a):
            score += 1
    return score
    
def get_scores(answers):
    scores = []
    scores.append(get_score(student_1, answers))
    scores.append(get_score(student_2, answers))
    scores.append(get_score(student_3, answers)) 
    return scores

def get_result(scores):
    result = []
    max_num = 0
    for s in scores:
        if(s > max_num):
            max_num = s
    
    for student in range(3):
        if(scores[student] == max_num):
            result.append(student + 1)
    
    result = sorted(result)
    return result
    
def solution(answers):
    init(answers)
    scores = get_scores(answers)
    answer = get_result(scores)
    return answer