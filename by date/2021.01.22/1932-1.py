N = int(input())
pyramid = []

## {(level, node) : [left, right], ...}
graph = {}
log = {}

result = 0

def set_pyramid():
    for _ in range(N):
        x = list(map(int, input().split()))
        pyramid.append(x)

def set_graph():
    for level in range(N - 1):
        for node in range(len(pyramid[level])):
            ind = (((level + 1) * level) / 2) + 1 + node
            l_ind = (((level + 1) * (level + 2)) / 2) + 1 + node
            r_ind = (((level + 1) * (level + 2)) / 2) + 1 + node + 1
            graph[(level, pyramid[level][node], ind)] = [pyramid[level + 1][node], l_ind, pyramid[level + 1][node + 1], r_ind]

def traveling(level, node, candidate, ind):
    global result

    if(level == N - 1):
        result = max(result, candidate + node)
        return

    candidate += node

    try:
        if(log[(level, node, ind)] > candidate):
            print(ind)
            return
    except:
        log[(level, node, ind)] = candidate

        left, l_ind, right, r_ind = graph[(level, node, ind)]

        traveling(level + 1, left, candidate, l_ind)
        traveling(level + 1, right, candidate, r_ind)

def main():
    traveling(0, pyramid[0][0], 0, 1)
    
if(__name__ == "__main__"):
    set_pyramid()
    set_graph()
    main()
    print(result)
    print(log)