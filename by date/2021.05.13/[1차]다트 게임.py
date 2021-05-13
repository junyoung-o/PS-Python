## #: (-1)
## * : (바로전 + 현재) * 2
## S : --
## D : **2
## T : **3

bonus = ["S", "D", "T"]
options = ["#", "*"]
def calc_star(dartResult):
    only_num = dartResult.replace("*", "")
    only_num = only_num.replace("#", "")
    
    num = []
    add_i = 0
    for i in range(1, len(only_num), 2):
        i += add_i
        if(i > len(only_num)):
            break
            
        if(only_num[i] == "0" and only_num[i-1] == "1"):
            if(only_num[i+1] == "S"):
                num.append(int(10))
            elif(only_num[i+1] == "D"):
                num.append(int(10) ** 2)
            elif(only_num[i+1] == "T"):
                num.append(int(10) ** 3)
            add_i += 1
            
        else:
            if(only_num[i] == "S"):
                num.append(int(only_num[i-1]))
            elif(only_num[i] == "D"):
                num.append(int(only_num[i-1]) ** 2)
            elif(only_num[i] == "T"):
                num.append(int(only_num[i-1]) ** 3)

    return num

def get_result(num_list, dartResult):
    index = 0
    n_id = -1
    result = num_list.copy()
    print(num_list, dartResult)
    while(index < len(dartResult) and n_id < len(num_list)):
        if(dartResult[index] in options):
            if(dartResult[index] == "#"):
                if(n_id == -1):
                    result[0] *= -1
                else:
                    result[n_id] *= -1
                
                
            else:
                if(n_id == 0):
                    result[0] *= 2
                else:
                    result[n_id] *= 2
                    if(n_id - 1 >= 0):
                        result[n_id - 1] *= 2
    
        if(dartResult[index] in bonus):
            n_id += 1
        
        index += 1
    
    
    
    return sum(result)

def solution(dartResult):
    num_list = calc_star(dartResult)
    answer = get_result(num_list, dartResult)
    # answer = 0
    return answer