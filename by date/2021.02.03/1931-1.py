N = int(input())
schedule = []
result = []

def sort_schedule():
    global schedule

    schedule = sorted(schedule, key = lambda s : s[0])
    schedule = sorted(schedule, key = lambda s : s[1])

def set_schedule():
    import sys

    for _ in range(N):
        schedule.append(list(map(int, sys.stdin.readline().split())))

    sort_schedule()

def init():
    set_schedule()

def record_result():
    limit = 0

    for (start, finish) in schedule:
        if(limit <= start):
            result.append((start, finish))
            limit = finish

def print_result():
    print(len(result))

def main():
    record_result()
    print_result()
    return

if(__name__=="__main__"):
    init()
    main()
