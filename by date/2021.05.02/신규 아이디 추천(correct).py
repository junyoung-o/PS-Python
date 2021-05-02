import re
special_char = "~!@#$%^&*()=+[{]}:?,<>/"

def to_lower(new_id):
    return new_id.lower()

def delete_speical_char(new_id):
    return re.sub(special_char, '', new_id)

def trans_dot(new_id):
    return re.sub('\.+','.',new_id)

def delete_dot(new_id):
    return re.sub("^[.]|[.]$", '', new_id)

def extend(new_id):
    if(len(new_id) == 0):
        return "a"
    return new_id

def limit_len(new_id):
    if(len(new_id) >= 16):
        return delete_dot(new_id[:15])
    return new_id

def limit_three(new_id):
    if(len(new_id) <= 2):
        while(len(new_id) <= 2):
            new_id += new_id[-1]
    return new_id

def solution(new_id):
    new_id = to_lower(new_id)
    new_id = delete_speical_char(new_id)
    new_id = trans_dot(new_id)
    new_id = delete_dot(new_id)
    new_id = extend(new_id)
    new_id = limit_len(new_id)
    new_id = limit_three(new_id)
    
    answer = new_id
    return answer