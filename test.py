import random
a = [1.4 ** i for i in range(29, -1, -1)]
b = [0] * 30
for i in range(10000):
    b[random.choices(range(30), weights = a)[0]] += 1
print(b)