c = []
is_visit = []

def set_is_visit(end):
    global is_visit
    is_visit = [False for _ in range(end + 1)]

def is_p(num):
    if(num == 2):
        return True
    
    for i in range(2, num):
        if(num % i == 0):
            return False
    return True

def dfs(vertex, index, nums, f, visit):
    global c
    if(is_visit[vertex]):
        return
    
    if(visit == 3):
        c.append(f + vertex)
        return
    
    is_visit[vertex] = True
    
    for next_ in range(index + 1, len(nums)):
        if(not is_visit[nums[next_]]):
            dfs(nums[next_], next_, nums, f + vertex, visit + 1)

def conbi(nums):
    nums = sorted(nums)
    for index, vertex in enumerate(nums):
        set_is_visit(max(nums))
        dfs(vertex, index, nums, 0, 1)
        set_is_visit(vertex)

def get_result():
    result = 0
    ## 3개의 조합을 만드는법
    for p_num in c:
        if(is_p(p_num)):
            result += 1
    
    return result
        
def solution(nums):
    answer = -1
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    conbi(nums)
    answer = get_result()
    

    return answer