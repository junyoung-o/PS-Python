s_map = []

def reverse(s):
    t = ""
    for i in range(len(s)):
        p = len(s) - i - 1
        t += s[p]
    return t

def to_bi(list_, n):
    stack = []
    for i in list_:
        bi = ""
        q = i
        while(True):
            if(q == 0):
                break
            r = q % 2
            q = q // 2
            bi += str(r)
            
        bi = reverse(bi)
            
        if(i < 2**(n-1)):
            while(len(bi) < n):
                bi = "0" + bi
        else:
            while(len(bi) < n):
                bi = bi + "0"
            
        stack.append(bi)
    return stack


def set_map(n, arr1, arr2):
    global s_map
    
    b1 = to_bi(arr1, n)
    b2 = to_bi(arr2, n)
    for i, j in zip(b1, b2):
        m = ""
        for k in range(n):
            m += str(max(int(i[k]), int(j[k])))
        s_map.append(m)
    
def get_result():
    result = []
    for s in s_map:
        t = ""
        for i in s:
            if(i == "1"):
                t += "#"
            else:
                t += " "
        result.append(t)
    return result

def solution(n, arr1, arr2):
    set_map(n, arr1, arr2)
    answer = get_result()
    return answer