import queue

N = int(input())
pyramid = []
candidate = []

def set_pyramid():
    import sys
    
    for i in range(N):
        x = list(map(int, sys.stdin.readline().split()))
        pyramid.append(x)
        candidate.append([0 for _ in range(i+1)])

def bfs(start_level, start_ind):
    if(N == start_level + 1):
        return

    q = queue.Queue()

    q.put((start_level, start_ind, start_level, start_ind, pyramid[start_level][start_ind]))

    while(not q.empty()):
        current_level, current_ind, pre_level, pre_ind, cand = q.get()
 
        if(candidate[current_level][current_ind] <= candidate[pre_level][pre_ind] + pyramid[current_level][current_ind] and cand >= candidate[current_level][current_ind]):
            candidate[current_level][current_ind] = candidate[pre_level][pre_ind] + pyramid[current_level][current_ind]

            if(current_level < N - 1):
                visit_list = [(current_level+1, current_ind, current_level, current_ind), (current_level+1, current_ind + 1, current_level, current_ind)]

                for next_level, next_ind, pre_level, pre_ind in visit_list:
                    if(candidate[pre_level][pre_ind] + pyramid[next_level][next_ind] >= candidate[next_level][next_ind]):
                        q.put((next_level, next_ind, pre_level, pre_ind, candidate[pre_level][pre_ind]))

def main():
    if(N == 1):
        candidate[-1] = [pyramid[0][0]]
    else:
        bfs(0, 0)
    return

if(__name__ == "__main__"):
    set_pyramid()
    main()
    print(max(candidate[-1]))