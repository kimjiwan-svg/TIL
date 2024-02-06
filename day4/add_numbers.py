def solution(my_string):
    num_list = [int(num) for num in my_string if num.isdigit()]
    answer = sum(num_list)
    return answer
