def get_result(phone_book):
    phone_book = sorted(phone_book, key = lambda x : (x, len(x)))
    
    for front, compare in zip(phone_book, phone_book[1:]):
        print(front, compare)
        if(compare.startswith(front)):
            return False
    return True
        
def solution(phone_book):
    answer = get_result(phone_book)
    return answer