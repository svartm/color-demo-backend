def generate_random_color():
    # Generate a random color code
    # Return the color code as JSON
    return '#0000ff'

def process_guess(answer, guess):
    # Process the inputted hex code
    # Determine the changes in the values of red, green, and blue
    # Determine the correctness of the values
    # Return the result as JSON
    message = 'Try again!'
    if (answer == guess):
        message = 'Correct!'
    return message
