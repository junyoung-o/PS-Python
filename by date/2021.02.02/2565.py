A = []
B = []
memo = []

def str_to_list(_list, _str):
    for i in range(len(_str)):
        _list.append(_str[i])

def set_sequence():
    global A, B
    
    A_str = input()
    B_str = input()

    str_to_list(A, A_str)
    str_to_list(B, B_str)

def set_memo():
    global memo

    memo = [[0] * (len(B) + 1) for _ in range(len(A)+1)]
 
def record():
    for a_ind in range(1, len(A) + 1):
        for b_ind in range(1, len(B) + 1):
            if(A[a_ind-1] == B[b_ind-1]):
                memo[a_ind][b_ind] = memo[a_ind - 1][b_ind - 1] + 1
            else:
                memo[a_ind][b_ind] = max(memo[a_ind-1][b_ind], memo[a_ind][b_ind-1])

def print_result():
    print(memo.pop().pop())

def main():
    record()
    print_result()
    return
    
if(__name__ == "__main__"):
    set_sequence()
    set_memo()
    main()