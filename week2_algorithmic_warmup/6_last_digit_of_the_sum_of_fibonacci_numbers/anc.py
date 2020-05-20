def fibonacci_sum_naive(n):
    if n<=1:
            return n
    sum = 0
    p =[0,1]
    for _ in range (n-1):
        p.append((p[-1] + p[-2])%10)
        p.pop(-3)
        sum +=p[-1]
    return sum+1


print(fibonacci_sum_naive(2))