A = []
B = []
candidate = [0]
memo = [0 for _ in range(1001)]

def str_to_list(A_str, B_str):
    global A, B

    for i in range(len(A_str)):
        A.append(A_str[i])

    for i in range(len(B_str)):
        B.append(B_str[i])

def set_sequence():
    A_str = input()
    B_str = input()

    str_to_list(A_str, B_str)

def record():
    if(len(A) <= len(B)):
        for ind in range(len(A)):
            memo_value = memo[ind-1]
            memo[ind] = memo_value

            for compare in range(candidate[-1], len(B)):
                if(A[ind] == B[compare]):
                    candidate.append(compare)
                    memo[ind] = memo_value + 1
                    break

        

    else:
        for ind in range(len(B)):
            memo_value = memo[ind - 1]
            memo[ind] = memo_value

            for compare in range(candidate[-1], len(A)):
                if(B[ind] == A[compare] and (compare not in candidate)):
                    candidate.append(compare)
                    memo[ind] = memo_value + 1
                    break

                
def print_result():
    # print(A, len(A))
    # print(B, len(B))
    # print(candidate)
    # print(memo[:len(A)])
    print(max(memo))

def main():
    record()
    print_result()
    return

if(__name__=="__main__"):
    set_sequence()
    main()