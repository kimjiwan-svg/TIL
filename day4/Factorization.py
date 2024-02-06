def solution(n):
    answer_set = set()
    tmp = 2
    while(n>=2):
        if (n % tmp):
            tmp +=1
        else:
            n /= tmp
            answer_set.add(tmp)
            tmp = 2
    answer = list(answer_set)
    answer.sort()
    return answer
