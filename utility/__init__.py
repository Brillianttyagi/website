import random
import string


def randomString(length):
    letters_and_digits = string.digits
    return ''.join((random.choice(letters_and_digits) for i in range(length)))
