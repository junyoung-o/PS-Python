def get_distance(x, y, a, b, c):
    return abs(a * x + b * y + c) / ((a**2 + b**2) ** (1/2))

def is_distance(dot1, dot2, a, b, c):
    x1, y1 = dot1
    x2, y2 = dot2
    
    d1 = get_distance(x1, y1, a, b, c)  
    d2 = get_distance(x2, y2, a, b, c)  
    
    if(0 < d1 < 2**(1/2) and 0 < d2 < 2**(1/2)):
        return True
    return False

def solution(w,h):
    ## hx + wy - wh = 0
    a, b, c = h, w, -w * h
    
    cnt = 0
    for x in range(w+1):
        for y in range(h+1):
            if(is_distance((x, y), (x+1, y+1), a, b, c)):
                cnt += 1
    
    answer = -c - cnt
    return answer