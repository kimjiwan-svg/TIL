def solution(age):
    alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    answer = ''
    while age>0:
        answer += alpha_list[age%10]
        age //= 10
    answer = answer[::-1]
    return answer
