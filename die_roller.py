import random
print("Hello, welcome to dice roller! Choose 2 numbers to roll between")
first = int(input("What is the first number: "))
second = int(input("What is the second number: "))
result = random.randint(first, second)
print("Your number is ", result, "!", sep="")