# python3


def max_pairwise_product(numbers):

    max_first = max(numbers)
    numbers.remove(max_first)
    max_second = max(numbers)
    
    return max_first*max_second




if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
