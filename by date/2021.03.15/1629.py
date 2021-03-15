import sys
input = sys.stdin.readline

a, b, c = list(map(int, input().split()))

def is_odd(num):
    if(num%2 != 0):
        return True
    return False

def program(time):
    if(time == 1):
        return a % c

    if(time == 2):
        return (a**2) % c

    m = time//2
    remain = program(m)

    if(is_odd(time)):
        return (((remain**2)%c)*a) % c

    else:
        return (remain**2) % c

print(program(b))