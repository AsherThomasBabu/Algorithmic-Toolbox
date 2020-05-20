def get_optimal_value(capacity, weights, values):
    index = list(range(len(values)))
    # contains ratios of values to weight
    ratio = [v/w for v, w in zip(values, weights)]
    # index is sorted according to value-to-weight ratio in decreasing order
    index.sort(key=lambda i: ratio[i], reverse=True)
 
    max_value = 0
    fractions = [0]*len(values)
    for i in index:
        if weights[i] <= capacity:
            fractions[i] = 1
            max_value += values[i]
            capacity -= weights[i]
        else:
            fractions[i] = capacity/weights[i]
            max_value += values[i]*capacity/weights[i]
            break
 
    return max_value

print(get_optimal_value(50, [20,50], [60,100]))