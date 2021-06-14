

for x in range(51):
    print(x)


for x in range(5, 1001, 5):
    print(x)


for x in range(1, 101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else: print(x)


sum = 0
for x in range(5000000):
    sum = sum+x
print(sum)


for x in range(2018, 0, -4):
    print(x)


def flex_countdown(lowNum, highNum, mult):
    for x in range(highNum, lowNum, -mult):
        print(x)
print(flex_countdown(2,4,10))
print(flex_countdown(32,83,6))
