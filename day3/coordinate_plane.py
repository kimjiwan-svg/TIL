idef solution(dot):
    dot_x = dot[0]
    dot_y = dot[1]
    if dot_x>0:
        if dot_y>0:
            answer = 1
        else:
            answer = 4
    
    else:
        if dot_y>0:
            answer = 2
        else:
            answer = 3
            
    return answer
