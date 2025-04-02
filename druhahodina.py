import random

for x in range (30):
    a = random.randint(0,10)
    b = random.randint(0,10)
    znamenko = random.randint(1,4)

    if znamenko == 1:
        print(f"{a} * {b} = {a*b}")
    elif znamenko == 2:
        print(f"{a} / {b} = {a / b}")
    elif znamenko == 3:
        print(f"{a} + {b} = {a+b}")
    elif znamenko == 4:
        print(f"{a} - {b} = {a-b}")