import queue as qu

n = True
max_r = 0

while(n):
    q = qu.Queue()
    base = 0
    test = list(map(int, input().split()))
    
    if(test[0] == 0):
        test = test[:-1]
        n = False
    
    for i in test:
        q.put(i)
    
    while(q.empty() != True):
        x = q.get()

        if(pre > x):
            pre = x
            print(x)
            _6549(x, base)
            
        if(pre < x):
            base = 0
            pre = x
            print(x)
            _6549(x, base)

def _6549(a, base):
    global max_r

    base += 1
    area = base * a

    if(max_r < area):
        max_r = area