# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n<=1:
            return n
    p =[0,1]
    for _ in range (n-1):
        p.append((p[-1] + p[-2])%10)
        p.pop(-3)
    return p[-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
