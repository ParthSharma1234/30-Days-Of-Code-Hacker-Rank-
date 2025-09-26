import math

def is_prime(n):
    if n <= 1:
        return "Not prime"
    if n <= 3:
        return "Prime"
    if n % 2 == 0 or n % 3 == 0:
        return "Not prime"
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return "Not prime"
        i += 6
    return "Prime"

T = int(input())
for _ in range(T):
    num = int(input())
    print(is_prime(num))