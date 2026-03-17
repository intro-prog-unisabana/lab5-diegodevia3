def input_response(secret, user_input):
    if user_input < secret:
        return ("Too low! Try a higher number.", False)
    elif user_input > secret:
        return ("Too high! Try a lower number.", False)
    else:
        return ("Correct! You guessed the number!", True)