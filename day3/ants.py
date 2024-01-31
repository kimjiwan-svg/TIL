def solution(hp):
    general = hp // 5
    hp %= 5
    soldier = hp // 3
    work = hp % 3
    
    answer = general + soldier + work
    return answer
