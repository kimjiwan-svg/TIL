def solution(balls, share):
    answer = 1
    if (balls/2) < share:
        share = balls - share
    for i in range(1, share+1):
        answer *= balls - i + 1
        answer /= i
    return answer
