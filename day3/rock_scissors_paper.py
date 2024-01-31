def solution(rsp):
    win_rsp = {
        '0' : '5',
        '2' : '0',
        '5' : '2'
              }
    answer = ''
    for i in rsp:
        answer += win_rsp[i]
    
    return answer
