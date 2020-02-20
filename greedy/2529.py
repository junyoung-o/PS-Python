k = int(input())
in_A = list(map(str, input().split()))
A = in_A
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
temp = num

def indf(A):
    ind = 0
    while(A[ind] != ">"):
        ind += 1
    return ind

def max_f(A, temp):
    max_r = []
    e = len(temp)-1

    for i in range(k):
        if('<' in A):
            for i in temp[e - indf(A):]:
                max_r.append(i)
            temp = temp[:e - indf(A)]
            A = A[indf(A):]
        else:
            temp.sort(reverse = True)
            print(temp)
            for i in range(k-len(max_r)+1):
                max_r.append(temp[i])
    return max_r

def min_f(A, temp):
    min_r = []

    for i in range(k):
        if('<' in A):
            for i in temp[:indf(A)+1]:
                min_r.append(i)
            temp = temp[indf(A)+1:]
            A = A[indf(A):]
        else:
            temp.sort(reverse = True)
            print(temp)
            for i in range(k-len(min_r)+1):
                min_r.append(temp[i])
    return min_r

print(max_f(A,temp), min_f(A, temp))