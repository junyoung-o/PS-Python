N = int(input())
pyramid = []
candidate = []

def set_pyramid():
    for i in range(N):
        x = list(map(int, input().split()))
        pyramid.append(x)
        candidate.append([0 for _ in range(i+1)])

def top_down():
    candidate[0][0] = pyramid[0][0]
    
    for level in range(N-1):
        for ind in range(len(pyramid[level])):
            current = candidate[level][ind]
            left = pyramid[level+1][ind]
            right = pyramid[level+1][ind+1]

            ## go_left
            candidate[level+1][ind] = max(current + left, candidate[level+1][ind])
            ## go_right
            candidate[level+1][ind+1] = max(current + right, candidate[level+1][ind+1])

def print_result():
    print(max(candidate[-1]))

def main():
    top_down()
    return
    
if(__name__ == "__main__"):
    set_pyramid()
    main()
    print_result()