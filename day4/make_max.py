def solution(numbers):
    numbers.sort(reverse=True)
    max1, max2 = numbers[0], numbers[1]
    answer = max1 * max2
    return answer
