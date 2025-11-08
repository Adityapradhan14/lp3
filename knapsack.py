# 0-1 Knapsack using a simple greedy-like approach (not optimal but easy)

# list of values and weights
values = [1, 4, 5, 7]
weights = [1, 3, 4, 5]
capacity = 7

# calculate value/weight ratio for each item
ratio = []
for i in range(len(values)):
    ratio.append(values[i] / weights[i])

# combine all info together
items = list(zip(values, weights, ratio))

# sort items by ratio (value per weight) in descending order
items.sort(key=lambda x: x[2], reverse=True)

total_value = 0
total_weight = 0

# loop through sorted items
for v, w, r in items:
    if total_weight + w <= capacity:
        total_value += v
        total_weight += w
        print(f"Taken item (value={v}, weight={w})")
    else:
        print(f"Skipped item (value={v}, weight={w})")

print("\nTotal weight in bag:", total_weight)
print("Total value in bag:", total_value)

