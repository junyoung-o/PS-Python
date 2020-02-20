inS = input()

x = inS.split("+")

num = []
c = []
ch = False
re = 0

for i in x:
    if("-" in i and ch == False):
        y = i.split("-")
        num.append(int(y[0]))
        y[0] = 0
        for i in y:
            c.append(int(i))
        ch = True
    
    elif("-" in i and ch == True):
        y = i.split("-")
        for i in y:
            c.append(int(i))
    
    elif(ch == False):
        num.append(int(i))
    
    elif(ch == True):
        c.append(int(i))

for i in num:
    re += i

for i in c:
    re -= i

print("x : {}, num :{}, c :{}".format(x, num, c))

print(re)