def solution(my_string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    for alpha in vowel:
        my_string = my_string.replace(alpha, '')
    answer = my_string
    return answer
