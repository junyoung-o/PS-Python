# N : 가로, M : 세로
N, M = list(map(int, input().split()))

def _1783():
    if(M == 1 or N == 1):
        return 1
    if(M == 2 and N == 2):
        return 1
    if(M == 2 and N > 2):
        return 2
    if(M >= 3 and M < 7 and N == 2):
        return (M//5 + 2)
    if(M >= 7 and N == 2):
        return 4
    if(M == 3 and N >= 3):
        return 3
    if(M >= 4 and M < 7 and N >= 3):
        return 4
    else:
        return M-2

x = _1783()

print(x)