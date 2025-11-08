# Job sequencing using greedy method

jobs = [
    ['A', 2, 100],
    ['B', 1, 19],
    ['C', 2, 27],
    ['D', 1, 25],
    ['E', 3, 15]
]

# sort jobs by profit (highest first)
for i in range(len(jobs)):
    for j in range(i + 1, len(jobs)):
        if jobs[i][2] < jobs[j][2]:
            jobs[i], jobs[j] = jobs[j], jobs[i]

# assume 3 time slots
slot = [0, 0, 0]
result = ["", "", ""]
total_profit = 0

for job in jobs:
    name = job[0]
    deadline = job[1]
    profit = job[2]
    
    # find empty slot from last possible
    for j in range(deadline - 1, -1, -1):
        if slot[j] == 0:
            slot[j] = 1
            result[j] = name
            total_profit += profit
            break

print("Job order:", result)
print("Total profit:", total_profit)

