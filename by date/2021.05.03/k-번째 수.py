g_array = []
g_commands = []

def set_array(a):
    global g_array
    g_array = a
    
def set_commands(c):
    global g_commands
    g_commands = c

def init(array, commands):
    set_array(array)
    set_commands(commands)

def get_result(command):
    temp_list = g_array
    temp_list = temp_list[command[0]-1:command[1]]
    temp_list = sorted(temp_list)
    return temp_list[command[2]-1]
    
def get_result_list():
    result_list = []
    for command in g_commands:
        result_list.append(get_result(command))
    
    return result_list    
    
def solution(array, commands):
    init(array, commands)
    answer = get_result_list()
    return answer