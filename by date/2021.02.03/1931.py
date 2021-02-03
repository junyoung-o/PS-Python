N = int(input())
schedule = []
candidate = {}
result = []

def set_schedule():
    import sys

    for _ in range(N):
        schedule.append(list(map(int, sys.stdin.readline().split())))

def get_compatible(start, finish, _list):
    return len(_list) - len(list(filter(lambda compare : compare[1] <= start or finish <= compare[0], _list))) - 1

def sort_candidate():
    global candidate

    items = list(candidate.items())
    sorted_candidate = sorted(items, key = lambda x : x[0][1])
    candidate = dict(sorted(sorted_candidate, key = lambda x : x[1]))

def set_candidate():
    for (start, finish) in schedule:
        candidate[(start, finish)] = get_compatible(start, finish, schedule)

    sort_candidate()

def init():
    set_schedule()
    set_candidate()
    return

def is_compatible(start, finish):
    test = get_compatible(start, finish, result) + 1

    if(test > 0):
        return False

    return True


def record_result():
    keys = list(candidate.keys())

    for (start, finish) in keys:
        if(is_compatible(start, finish)):
            result.append((start, finish))

def print_result():
    print(len(result))

def main():
    record_result()
    print_result()
    return

if(__name__=="__main__"):
    init()
    main()
