def solution(num_list):
    odd = [x for x in num_list if x % 2 == 1]
    even = [x for x in num_list if x % 2 == 0]
    answer = [len(even), len(odd)]
    return answer
