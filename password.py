import random
import string

a = int(input("Enter number: "))


def pw(x):
    chars = string.ascii_letters
    p = "".join(random.choice(chars) for i in range(a))
    print(p)


pw(a)