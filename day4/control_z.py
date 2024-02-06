def solution(s):
    s_list = s.split(' ')
    sum0 = 0
    for i in range(0, len(s_list)):
        if s_list[i] == 'Z':
            sum0 -= int(s_list[i-1])
        else:
            sum0 += int(s_list[i])
        
    answer = sum0
    return answer
