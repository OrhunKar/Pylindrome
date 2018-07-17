print ('\nPython Palindrome!\n')

def palindrome():

    print ('''Please enter the word you would like to check
                              for example: racecar''')

    word = input(">> ")

    if word == word[::-1]:
        print ('This string is a palindrome!')
    else:
        print ("This string isn't a palindrome :(")

    re_play = input("Do you want to enter a new string (y/n)? ")

    if re_play.lower().startswith("y"):
        palindrome()
    else:
        print ('\nBye!')

palindrome()