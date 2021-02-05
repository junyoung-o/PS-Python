a, b = list(map(int, input().split()))

a_e = [0] * (max(a, b) + 1)
b_e = [0] * (max(a, b) + 1)

def set_e():
    temp_a = a
    for i in range(2, a + 1):
        temp = 0
        while(temp_a % i == 0):
            temp_a /= i
            temp += 1
        a_e[i] = temp

    temp_b = b
    for i in range(2, b + 1):
        temp = 0
        while(temp_b % i == 0):
            temp_b /= i
            temp += 1
        b_e[i] = temp

def init():
    set_e()
    return

def get_result():
    result_g = 1
    result_l = 1

    result_ge = [0, 0]
    result_le = [0, 0]

    for ind in range(2, len(a_e)):
        result_ge.append(min(a_e[ind], b_e[ind]))
        result_le.append(max(a_e[ind], b_e[ind]))

    for ind in range(2, len(result_le)):
        if(result_le[ind] != 0):
            result_l *= ind ** result_le[ind]

        if(result_ge[ind] != 0):
            result_g *= ind ** result_ge[ind]

    return result_g, result_l

def print_result(result):
    print(result[0])
    print(result[1])

def main():
    print_result(get_result())
    return

if(__name__=="__main__"):
    init()
    main()
