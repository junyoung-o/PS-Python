import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.visit = False

class make_tree:
    def __init__(self):
        self.root = None

    def making(self, data):
        if(self.root == None):
            self.root = Node(data)

        else:
            current = self.root
            while(True):
                if(current.data > data):
                    if(current.lchild == None):
                        current.lchild = Node(data)
                        break
                    current = current.lchild

                if(current.data < data):
                    if(current.rchild == None):
                        current.rchild = Node(data)
                        break
                    current = current.rchild

def DFS(node):
    global prenum

    if(node.visit == True):
        return

    if(node.lchild == None and node.rchild == None):
        return

    node.visit = True

    if (node.lchild != None and node.lchild.visit == False):
        prenum += 1
        DFS(node.lchild)
        prenum += 1 #postnum
        result[node.lchild.data] = prenum #postnum

    if(node.rchild != None and node.rchild.visit == False):
        prenum += 1
        DFS(node.rchild)
        prenum += 1 #postnum
        result[node.rchild.data] = prenum #postnum

obj = make_tree()
prenum = 1
result = {}

while(True):
    try:
        obj.making(int(sys.stdin.readline()))
    except:
        break

DFS(obj.root)
result[obj.root.data] = 20001

for k in result.keys():
    print(k)