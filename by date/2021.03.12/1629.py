import sys
input = sys.stdin.readline

a, b, c = list(map(int, input().split()))

def prog(s):
    if(s == 1):
        return a%c

    if(s == 2):
        return a**2%c

    