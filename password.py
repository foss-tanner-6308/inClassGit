import random
import string


def pw():
    a = input("Enter a number: ")
    chars = string.ascii_letters
    p = "".join(random.choice(chars) for i in range(a))
    print(p)