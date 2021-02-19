n = int(input())
A = []
result = []

def set_A():
    global A

    A = list(map(int, input().split()))

def init():
    set_A()
    return

def test():
    rind = 0
    pre = -1

    for ind in range(n):
        check = False
        
        if(pre < A[ind] and ind < rind and A[ind] < A[rind]):
            result.append(A[rind])
            check = True
            
        else:
            for cind in range(ind + 1, n):
                if(A[cind] > A[ind]):
                    pre = A[ind]
                    rind = cind
                    result.append(A[rind])
                    check = True
                    break

        if(not check):
            result.append(-1)

def print_result():
    [print(r, end=" ") for r in result]


def main():
    test()
    print_result()
    return

if(__name__=="__main__"):
    init()
    main()