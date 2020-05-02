# Uses python3
def calc_fib(n):
    if n<=1:
            return n
    p = [0,1]
    for i in range (n-1):
        p.append(p[-1]+p[-2])
    return p[-1]
   
n = int(input())
print(calc_fib(n))
