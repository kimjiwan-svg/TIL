def solution(my_string):
    numbers = [str(num) for num in range(10)]
    answer = [int(alpha) for alpha in my_string if alpha in numbers]
    answer.sort()
    return answer
