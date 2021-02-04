N = int(input())

def is_sequence(number):
    str_num = str(number)
    d = int(str_num[0]) - int(str_num[1])

    for ind in range(1, len(str_num) - 1):
        if(int(str_num[ind]) - int(str_num[ind + 1]) != d):
            return False
    return True

def get_result():
    result = 0

    for number in range(1, N + 1):
        if(number // 10 == 0 and number != 10):
            result += 1
        
        elif(is_sequence(number)):
            result += 1

    return result

def is_extra():
    if(N == 1):
        print(1)
        return True
    return False

def main():
    if(not is_extra()):
        print(get_result())
    return

if(__name__=="__main__"):
    main()
