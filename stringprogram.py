def occurences(string1, string2):
    count = -3
    for word in string1:
     for character in word:
        count = count + 1
    return count
first_string = input('Enter the first string: ')
second_string = input('Enter the second string: ')
occurance_var = occurences(first_string,second_string)
print(second_string,'ocures',occurance_var,'in',first_string)
