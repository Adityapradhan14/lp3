# Fractional Knapsack Problem

def fractional_knapsack(values, weights, capacity):
    n = len(values)
    
    # Calculate value/weight ratio for each item
    ratio = []
    for i in range(n):
        ratio.append((values[i] / weights[i], i))  # (ratio, index)

    # Sort items by ratio in descending order
    ratio.sort(reverse=True)

    total_value = 0  

    # Pick items based on highest ratio
    for r, i in ratio:
        if capacity == 0:
            break
        
        if weights[i] <= capacity:
            # take full item
            total_value += values[i]
            capacity -= weights[i]
        else:
            # take fractional part
            frac = capacity / weights[i]
            total_value += values[i] * frac
            capacity = 0

    return total_value


# Example
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value = fractional_knapsack(values, weights, capacity)
print("Maximum value in knapsack =", max_value)

