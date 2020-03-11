# HL Complete program
# Im putting together the code as i make the components

import random, math

#Functions go here
def intcheck(question,low = None,high = None):
    valid = False
    # Error messages
    if low is not None and high is not None: # Error message if variables are given
        error = "Please enter a whole number between {} and {} (Inclusive) ".format(low,high)
    elif low is not None and high is None: # Error message if only low variable is given
        error = "Please enter a whole number equal to or above {} ".format(low)
    elif low is not None and high is None: # Error message if only high variable is given
        error = "Please enter a whole number equal to or below {} ".format(high)
    else: # Error message if no variables are given
        error = "please enter a whole number"

    while not valid:
        try:
            # Gets user input
            response = int(input(question.format(low, high)))
            # Checks number is not too low
            if low is not None and response < low:
                print(error) # If its too low  display error
                continue
            # Checks number is not too high
            if high is not None and response > high:
                print(error) # If it is too high print error
                continue

            return response
        # If input is not a number or is a decimal then display error
        except ValueError:
            print(error)
            print()


def guess_calc(high,low):
    range = high - low + 1
    max_raw = math.log2(range)  # gets maximum number of guesses using binary search
    max_upped = math.ceil(max_raw)  # Rounds up max_raw
    max_guesses = max_upped + 1  # Gives the user an extra guess incase they mess up
    return max_guesses




#Main routine goes here
rounds = intcheck("How many rounds do you want to play?: ",1)  # Asks how many rounds user wants to play
rounds_played = 0  # Counts rounds played
num_won = 0  # Counts rounds won
while rounds_played < rounds:
    print() # separates each round

    rounds_played += 1  # This round has started so add 1 to how many rounds are played
    already_guessed = [] # List that contains all guesses in this round

    print("Round {}".format(rounds_played)) # Display what round the user is on

    guess = ""
    # Gets range for secret number from the user
    low_num = intcheck("What do you want the lowest number to be: ")  # Gets lowest number from the user
    high_num = intcheck("What do you want the highest number to be: ".format(low_num),low_num)  # Gets the highest number from the user

    max_guesses = guess_calc(high_num,low_num)  # Generates the max number of guesses
    secret_num = random.randint(low_num, high_num)  # Generates random number
    guesses_left = max_guesses # Sets amount of guesses fo the user
    print("You have a max of {} guesses".format(guesses_left))  # Tells user their max amount of guesses

    # loops question until user runs out of guess or gets it right
    while guesses_left >= 1 and secret_num != guess:
        guess = intcheck("What is your guess: ",low_num,high_num)  # Gets user guess between low number and high number

        # Checks if user has guessed the number before if the user has it loops the question.
        if guess in already_guessed:
            print("You have guessed this number already, please try again")
            print("You have {} guesses left".format(guesses_left))
            continue

        guesses_left -= 1
        already_guessed.append(guess)  # Adds the current guess to the list of already_guessed above

        if guesses_left >= 1:  # Compares users guess to the secret number and gives appropriate feedback
            if guess < secret_num:  # If guess is lower than secret number tell user to go higher
                print("Higher")  # Feedback
            elif guess > secret_num:  # If guess is higher than secret number tell user to go lower
                print("Lower")  # Feedback
            elif guess == secret_num:  # if user gets it right then congratulate them
                if guesses_left == max_guesses - 1:
                    print("Amazing!, You got it right in 1 guess")
                else:
                    print("Congratulations, You got it right in {} guesses".format(max_guesses - guesses_left))
                num_won += 1
        # Prints appropiate feedback based on the amount of guesses the user has left
        if guesses_left >= 1 and guess != secret_num:
            print("You have {} guesses left".format(guesses_left))
        elif guess != secret_num :
            print("you ran out of guesses")
    print("Won: {} | Lost: {}".format(num_won, rounds_played - num_won))













