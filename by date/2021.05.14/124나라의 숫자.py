question = ["1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10"]

answer = [1, 2, 4, 11, 12, 14, 21, 22, 24, 41]

num = ["1", "2", "4"]
def get_result(n):
    if(n <= 3):
        return num[n - 1]   

    q, r = divmod(n - 1, 3)

    
    return get_result(q) + num[r]
    
def solution(n):
    answer = get_result(n)
    print(answer)
    return int(answer)

for i, (q, a) in enumerate(zip(question, answer)):
    if(solution(int(q)) == a):
        print("{} is right".format(i + 1))
    else:
        print("{} is worng".format(i + 1))