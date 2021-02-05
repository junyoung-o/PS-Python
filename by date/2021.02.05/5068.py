a, b = list(map(int, input().split()))


def get_result():
    if(b % a == 0):
        print("factor")
        return

    elif(a % b == 0):
        print("multiple")
        return

    else:
        print("neither")
        return
        

def main():
    global a, b

    while(a != 0 and b != 0):
        get_result()
        a, b = list(map(int, input().split()))
    return

if(__name__=="__main__"):
    main()
