cnt = int(input())
diviser = []

def sort_diviser():
    global diviser

    diviser = sorted(diviser)

def init():
    global diviser

    diviser = list(map(int, input().split()))
    sort_diviser()
    return

def is_extra():
    if(cnt == 1):
        print(diviser[0] ** 2)
        return True

    if(cnt == 2):
        print(diviser[0] * diviser[1])
        return True

    return False

def main():
    # print(diviser)

    if(not is_extra()):
        print(diviser[0] * diviser[-1])
        return
    return

if(__name__=="__main__"):
    init()
    main()
