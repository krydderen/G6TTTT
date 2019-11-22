import random

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


for x in range(len(numbers)):
    selection = random.randint(0, len(numbers)-1)
    goner = numbers.pop((selection))
    print(goner)