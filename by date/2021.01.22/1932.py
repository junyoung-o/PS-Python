N = int(input())
pyramid = []

## {(level, node) : [left, right], ...}
graph = {}

result = 0

def set_pyramid():
    for _ in range(N):
        x = list(map(int, input().split()))
        pyramid.append(x)

def set_graph():
    for level in range(N - 1):
        for node in range(len(pyramid[level])):
            graph[(level, pyramid[level][node])] = [pyramid[level + 1][node], pyramid[level + 1][node + 1]]

def traveling(level, node, candidate):
    global result

    if(level == N - 1):
        result = max(result, candidate + node)
        return

    candidate += node

    left, right = graph[(level, node)]

    traveling(level + 1, left, candidate)
    traveling(level + 1, right, candidate)

def main():
    traveling(0, pyramid[0][0], 0)
    
if(__name__ == "__main__"):
    set_pyramid()
    set_graph()
    main()
    print(result)