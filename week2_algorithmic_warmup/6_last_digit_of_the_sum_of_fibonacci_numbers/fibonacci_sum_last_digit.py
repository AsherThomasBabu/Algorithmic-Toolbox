# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n<=1:
            return n
    sum = 1
    p =[0,1]
    for _ in range (n-1):
        p.append(p[-1]%10 + p[-2]%10)
        p.pop(-3)
        sum +=p[-1]%10
    return sum%10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
