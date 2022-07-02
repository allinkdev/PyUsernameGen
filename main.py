import random
import re

global words

with open("wordlist.txt") as file:
    words = list(word.strip().lower() for word in file)


def split(string):
    return [char for char in string]


def random_boolean():
    return random.getrandbits(1)


def random_number():
    return random.randint(0, 8) + 1


def generate_name():
    name = ""
    name_length = random.randint(8, 20)
    word_amount = random.randint(1, 2)
    curr_words = 0

    for i in range(name_length):
        if curr_words < word_amount:
            if random.randint(1, 2) == 2:
                word = re.sub(r'[\W_]+', '', random.choice(words))
                name += word[0:1].upper() + word[1:]
                curr_words += 1

        if random.randint(0, 10) == 2 and name.count("_") == 0:
            name += "_"

    if random.randint(0, 2) == 2:
        name += str(random.randint(11, 99))

    if random.randint(0, 10) == 5:
        name = "The" + name

    return name


for i in range(100):
    print(generate_name())
