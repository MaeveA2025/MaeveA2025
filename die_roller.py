import random
print("Hi! Welcome to die roll, pick 2 numbers!")
first = int((input("First number: ")))
second = int((input("Second number: ")))
result = random.randint(first, second)
print("The number was ", result, "!", sep="")