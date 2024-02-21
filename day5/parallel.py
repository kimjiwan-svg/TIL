def solution(dots):
    
    answer = 0
    def cal_(dot1,dot2,dot3,dot4):
        return (dot1[0]-dot2[0])*(dot3[1]-dot4[1]), (dot1[1]-dot2[1])*(dot3[0]-dot4[0])

    dot_index = [(0,1), (0,2), (0,3)]
    dot_index2 = [(2,3), (1,3),(1,2)]

    for dd, tt in zip(dot_index, dot_index2):
        tmp1, tmp2 = cal_(dots[dd[0]],dots[dd[1]],dots[tt[0]], dots[tt[1]])
        if tmp1 == tmp2:
            answer = 1


    return answer
