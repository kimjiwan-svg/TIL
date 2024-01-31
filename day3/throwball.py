def solution(numbers, k):
    answer = 1 + 2*(k-1) % len(numbers)
    
    return answer
