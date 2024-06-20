def solution(order):
    answer = 0
    order_list = str(order)
    for num in order_list:
        if num in ['3', '6', '9']:
            answer += 1
    return answer

