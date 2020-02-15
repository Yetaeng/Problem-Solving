def solution(array, commands):
    answer = []
    for list_commands in commands:
        cut_array = array[list_commands[0]-1: list_commands[1]]
        cut_array.sort()
        answer.append(cut_array[list_commands[2]-1])
    return answer