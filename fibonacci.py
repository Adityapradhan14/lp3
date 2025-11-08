steps = 0  # count how many times loop runs

n = int(input("Enter how many terms: "))

a, b = 0, 1

print("Fibonacci Series (Non-Recursive):")

if n > 0:
    print(a, end=" ")
if n > 1:
    print(b, end=" ")

for i in range(2, n):
    steps += 1
    c = a + b
    print(c, end=" ")
    a = b
    b = c

print("\nTotal steps:", steps)











##2 non recursive


steps = 0  # count how many times loop runs

n = int(input("Enter how many terms: "))

a, b = 0, 1

print("Fibonacci Series (Non-Recursive):")

if n > 0:
    print(a, end=" ")
if n > 1:
    print(b, end=" ")

for i in range(2, n):
    steps += 1
    c = a + b
    print(c, end=" ")
    a = b
    b = c

print("\nTotal steps:", steps)

