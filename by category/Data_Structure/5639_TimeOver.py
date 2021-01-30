import sys
import queue

class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class solving:
    def __init__(self):
        self.root = None

    def solve(self, data):
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

    def print_result(self, node):
        s = []
        while(True):
            while(node):
                if(node.rchild):
                    s.append(node.rchild)
                s.append(node)
                node = node.lchild
            node = s.pop()
            if(node.rchild and (s[-1] if len(s) else None) == node.rchild):
                s.pop()
                s.append(node)
                node =node.rchild
            else:
                print(node.data)
                node = None
                
            if(not s):
                break

obj = solving()

while(True):
    try:
        vertex = int(sys.stdin.readline().rstrip())
        obj.solve(vertex)
    except:
        break

obj.BFS(obj.root)