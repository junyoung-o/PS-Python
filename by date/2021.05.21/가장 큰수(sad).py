def swap(list_, i, j):
    temp = list_[i]
    list_[i] = list_[j]
    list_[j] = temp
    return list_

def get_list(numbers):
    x = max(numbers)
    x_len = len(str(x))
    list_ = list(map(str, numbers))
    list_ = list(map(lambda x : x.ljust(x_len, ".").replace("0"," "), list_))
    return sorted(list_, reverse = True, key = lambda x : str(x))

def get_result(numbers):
    list_ = get_list(numbers)
    print(list_)
    result = "".join(list_)
    result = result.replace(".", "")
    result = result.replace(" ", "0")
     
                
    return result
    
def solution(numbers):    
    answer = get_result(numbers)
    return answer