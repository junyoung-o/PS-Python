special_char = "~!@#$%^&*()=+[{]}:?,<>/"

def to_lower(new_id):
    return new_id.lower()

def delete_speical_char(new_id):
    temp = new_id
    for char in new_id:
        if(char in special_char):
            temp = temp.replace(char, '')
            
    return temp

def trans_dot(new_id):
    temp = ""
    index = 0
    while(index < len(new_id)):
        if(new_id[index] == "."):
            temp += "."
            while(index < len(new_id) and new_id[index] == "."):
                index += 1
            
        else:
            temp += new_id[index]
            index += 1
            
            
    return temp

def delete_dot(new_id):
    if(len(new_id)==0):
        return new_id
    if(new_id[0] == "."):
        new_id = new_id[1:]
        
    if(len(new_id)==0):
        return new_id
    
    if(new_id[-1] == "."):
        new_id = new_id[:-1]
    return new_id

def extend(new_id):
    if(len(new_id) == 0):
        return "a"
    return new_id

def limit_len(new_id):
    if(len(new_id) >= 16):
        new_id = delete_dot(new_id[:15])
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