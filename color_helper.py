import random


def generate_hex_color():
    r = random.randint(0,5)
    g = random.randint(0,5)
    b = random.randint(0,5)

    r *= 51
    g *= 51
    b *= 51

    hex_code = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return hex_code


def process_guess(answer, guess):
    message = 'Try again!'
    if (answer == guess):
        message = 'Correct!'
    return message
