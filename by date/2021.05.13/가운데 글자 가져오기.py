def solution(s):
    m = len(s) // 2
    if(len(s) % 2 != 0):
        answer = s[m]
    else:
        answer = s[m - 1] + s[m]
    return answer