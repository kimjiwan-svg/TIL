def factorial(n):
        
    if (n == 1) or (n == 0):
        return 1
    else:
        return n*factorial(n-1)

def solution(n):
    sum0 = 1
    while(factorial(sum0)<=n):
        sum0 += 1
    sum0 -= 1
    return sum0
    
