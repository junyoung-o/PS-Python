A = []
B = []
linked = []
memo = []

def str_to_list(arr, arr_str):
    for i in range(len(arr_str)):
        arr.append(arr_str[i])

def set_sequence():
    A_str = input()
    B_str = input()

    str_to_list(A, A_str)
    str_to_list(B, B_str)

def set_linked():
    if(len(A) <= len(B)):
        for ind in range(len(A)):
            for compare in range(len(B)):
                if(A[ind] == B[compare]):
                    linked.append((ind, compare))

    else:
        for ind in range(len(B)):
            for compare in range(len(A)):
                if(B[ind] == A[compare]):
                    linked.append((ind, compare))


def set_memo():
    global memo
    memo = [0 for _ in range(len(linked))]

def get_result():
    for ind in range(len(linked)):
        memo_value = 0
        for compare in range(ind):
            if(linked[ind][0] > linked[compare][0] and linked[ind][1] > linked[compare][1]):
                memo_value =  max(memo_value, memo[compare])

        memo[ind] = memo_value + 1

def print_result():
    # print(A, len(A))
    # print(B, len(B))
    # print(linked)
    # print(memo)
    print(max(memo))

def main():
    get_result()
    print_result()
    return
    
if(__name__ == "__main__"):
    set_sequence()
    set_linked()
    set_memo()
    main()