import random
import string


def welcome():
    print("welcome in random passowrd generator")


welcome()
length = input("the length of the password you want: ")


def makeingRandomPassword(length):
    random_chars = ''.join(random.choices(
        string.ascii_letters+string.digits, k=int(length)))
    print(random_chars, len(random_chars))


def check(string):
    mode = ""
    if string.isnumeric():
        makeingRandomPassword(string)
        return
    if not string.isnumeric():
        print("please write a number")
        print()
        mode = False
        while (mode == False):
            length2 = input("the length of the password you want: ")
            if length2.isnumeric():

                makeingRandomPassword(length2)
                return
            else:
                print()
                print("please write a number")


check(length)
