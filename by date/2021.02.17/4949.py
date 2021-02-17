stack = None

class Stack():
    def __init__(self):
        self.s = []
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        if(self.get_size() == 0):
            return True
        return False

    def condition_push(self, character):
        if(character == "("):
            self.s.append(")")

        else:
            self.s.append("]")

        self.size += 1

    def pop(self):
        if(self.is_empty()):
            return -1

        self.size -= 1
        return self.s.pop()

def define_stack():
    global stack
    stack = Stack()

def init():
    define_stack()
    return

def is_VPS(latest_pair):
    latest = stack.pop()
    if(latest == latest_pair):
        return True
    return False

def main():
    import sys

    while(True):
        init()
        result = "yes"

        sentence = sys.stdin.readline().rstrip("\n")
        
        if(sentence == "." and len(sentence) == 1):
            break
        
        for character in sentence:
            if(character == "."):
                break

            if(character == "(" or character == "["):
                stack.condition_push(character)
            
            elif(character == ")" or character == "]"):
                if(not is_VPS(character)):
                    result ="no"
                    break

        if(stack.get_size() != 0):
            result = "no"
            
        print(result)

    return

if(__name__=="__main__"):
    main()