N = int(input())
linked_dict = {}
linked_list = []

def input_linked():
    import sys
    
    for _ in range(N):
        a, b = list(map(int, sys.stdin.readline().split()))
        linked_dict[(a, b)] = 0
        linked_list.append((a, b))

def set_linked():
    linked_list = list(linked_dict.keys())

    for update in range(len(linked_list)):
        a, b = linked_list[update]
        for compare in range(len(linked_list)):
            ca, cb = linked_list[compare]
            if(update != compare):
                if((a < ca and b > cb) or (a > ca and b < cb)):
                    linked_dict[(a, b)] += 1

def sort_linked():
    global linked_dict

    sorted_linked = sorted(linked_dict.items(), key = lambda k : k[1], reverse =True)
    sorted_linked = sorted(sorted_linked, key = lambda k : k[0][0], reverse =False)

    linked_dict = dict(sorted_linked)

def check_finish():
    if(sum(list(linked_dict.values())) == 0):
        return True
    return False

def get_result():
    result = 0
    linked_keys = list(linked_dict.keys())

    for (a, b) in linked_keys:
        if(check_finish()):
            break
        
        linked_dict[(a, b)] = 0
        result += 1
        candidate = list(filter(lambda compare : (a < compare[0] and b > compare[1]) or (a > compare[0] and b < compare[1]) , linked_list))

        for update in candidate:
            if(linked_dict[update] != 0):
                linked_dict[update] -= 1

    return result

def main():
    print(get_result())
    return
    
if(__name__ == "__main__"):
    input_linked()
    set_linked()
    sort_linked()
    main()