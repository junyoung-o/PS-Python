N = int(input())
numbers = 0
operator = {}
use_operator = {}
result_list = []

def get_numbers():
    global numbers
    numbers = list(map(int, input().split()))

def get_operator():
    global operator
    templates = ["+", "-", "*", "//"]

    operator_num = 0
    operator_num = list(map(int, input().split()))

    for i in range(4):
        operator[templates[i]] = operator_num[i]

    for i in range(4):
        use_operator[templates[i]] = 0

def get_candidate():
    templates = ["+", "-", "*", "//"]
    
    candidate = []
    for i in range(4):
        if(use_operator[templates[i]] != operator[templates[i]]):
            candidate.append(templates[i])

    return candidate

def print_result():
    result_min = min(result_list)
    result_max = max(result_list)

    print(result_max)
    print(result_min)

def backtracking(ind, result):
    global result_list

    if(ind >= N - 1):
        result_list.append(result)
        return

    candidate = get_candidate()
    
    for i in candidate:
        if(i == "+"):
            use_operator[i] += 1
            next_result = result + numbers[ind + 1]
            backtracking(ind + 1, next_result)
            use_operator[i] -= 1

        if(i == "-"):
            use_operator[i] += 1
            next_result = result - numbers[ind + 1]
            backtracking(ind + 1, next_result)
            use_operator[i] -= 1

        if(i == "*"):
            use_operator[i] += 1
            next_result = result * numbers[ind + 1]
            backtracking(ind + 1, next_result)
            use_operator[i] -= 1

        if(i == "//"):
            use_operator[i] += 1
            next_result = abs(result) // numbers[ind + 1]
            if(result < 0):
                next_result = -next_result
            backtracking(ind + 1, next_result)
            use_operator[i] -= 1

def main():
    backtracking(0, numbers[0])

if(__name__ == "__main__"):
    get_numbers()
    get_operator()
    main()
    print_result()