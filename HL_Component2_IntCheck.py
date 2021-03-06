#Higher Lower Component 2 IntCheck
# Loops question so it repeats until a valid number is entered
# make code recyclable

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


#Main routine goes here
low_num = intcheck("What do you want the lowest number to be: ") # Gets lowest number from the user
high_num = intcheck("What do you want the highest number to be: ".format(low_num),low_num) # Gets the highest number from the user



guess = intcheck("What is your guess: ",low_num,high_num) # Gets user guess between low number and high number
rounds = intcheck("How many rounds do you want to play?: ",1)# Asks how many rounds user wants to play
