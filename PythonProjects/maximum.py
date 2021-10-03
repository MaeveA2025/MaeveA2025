# Create a program that finds that maximum between 2 numbers
def max(a, b):
    if a >= b:
        return a 
    else:
        return b



def main():
    print(max(2,4))
    print(max(-1, -4))
    print(max(2,2))

main()