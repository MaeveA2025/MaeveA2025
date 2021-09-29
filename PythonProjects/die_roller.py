import random
def roller():
    try:
        # Ask for user input 
        num = input("Hello welcome to die roller! Enter 2 numbers: ")
        #split input into tokens
        split_num = num.split()
        # Result is a random number between the first [0th index] and second [1st index] numbers
        # Lower to higher otherwise
        result = random.randint(int(split_num[0]), int(split_num[1]))
        # prints out the result of the randomizer
        print("The number was ", result, "!", sep="")
        # Calls roller again for more inputs
        roller()
    
    # If there is an invalid number catch it and re run the function
    except ValueError:
        print("Invalid input")
        roller()

# Define main as our roller function and call it
def main():
    roller()

main()
