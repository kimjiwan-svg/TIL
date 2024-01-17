# ice Americano

def solution(money):
    cups = int(money) // 5500
    change = int(money) % 5500
    answer = []
    answer.append(cups)
    answer.append(change)
    return answer
