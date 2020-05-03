# Uses python3
import sys

def get_fibonacci_huge_naive(n,m):
    if n <= 1:
        return n
    p =[0,1]
    pisano =0
    while True:
        p.append((p[-1] + p[-2])%m)
        if p[-2:]==[0,1]:
            pisano = len(p)-2
            p =[0,1]
            break
    if ((n%pisano)-1) < 0:
        return 0
    for _ in range ((n%pisano)-1):
        
        p.append(p[-1] + p[-2])
        p.pop(-3)
    return p[-1]%m

if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
