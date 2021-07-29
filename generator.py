import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols


def generate():
    temp = random.sample(all, 12)
    password = "".join(temp)
    return password



