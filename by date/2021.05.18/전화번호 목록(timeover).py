def get_result(phone_book):
    phone_book = sorted(phone_book, key = lambda x : len(x))
    
    for i, front in enumerate(phone_book):
        front_len = len(front)
        for number in phone_book[i+1:]:
            if(number[:front_len] == front):
                return False
    return True
        
def solution(phone_book):
    answer = get_result(phone_book)
    return answer
