def even_num():
    count = 0
    for item in range(1,10):
        if item%2 == 0:
            print(item)
            count += 1
        else:
            continue
    print("We have", count, "even numbers")

def main():
    even_num()

main()
