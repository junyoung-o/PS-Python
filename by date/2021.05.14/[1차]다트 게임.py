## #: (-1)
## * : (바로전 + 현재) * 2
## S : --
## D : **2
## T : **3

import re

question = ["1S2D*3T",
            "1D2S#10S",
            "1D2S0T",
            "1S*2T*3S",
            "1D#2S*3S",
            "1T2D3D#",
            "1D2S3T*"]

answer = [37, 9, 3, 23, 5 , -4, 59]

bonus = {"S" : 1, "D" : 2, "T" : 3}
option = ["*", "#"]

def get_result(dartResult):
    x = re.compile(r"\d+[SDT]+[*#]*")
    x = x.findall(dartResult)
    result = []

    for i in range(len(x)):
        if(x[i][-1] == option[0]):
            x[i] = x[i].replace(x[i][-1], "*(2)")
            if(i - 1 >= 0):
                x[i-1] = x[i-1] + "*(2)"
        if(x[i][-1] == option[1]):
            x[i] = x[i].replace(x[i][-1], "*(-1)")

    for i in x:
        for b in bonus:
            if(b in i):
                result.append(eval(i.replace(b, f"**{bonus[b]}")))

    return sum(result)




def solution(dartResult):
    answer = get_result(dartResult)
    return answer



for i, (q, a) in enumerate(zip(question, answer)):
    if(solution(q) == a):
        print("{} is right".format(i + 1))
    else:
        print("{} is worng".format(i + 1))