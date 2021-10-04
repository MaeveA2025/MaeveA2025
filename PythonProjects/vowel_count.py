# Create a function that will add up all the vowels in a string and return that value
def get_count(sentence):
    count = 0
    for letter in sentence:
        print(letter)
        if letter == 'a' or letter =='e' or letter == 'i' or letter == 'o' or letter == 'u':
            count += 1
        else:
            count += 0

    return count
    #print(count)

get_count('abracadabra')
