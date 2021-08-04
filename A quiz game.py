import random

# Input your questions
questions = {
    "Who, as the UK leader, signed the Munich agreements?:\nA. Chamberlen \nB. Churchill \nC. Daladier" : "A",
    "When the WWII started?:\nA. 1938 \nB. 1939 \nC. 1940": "B",
    "On what city was the second nuclear bomb dropped?:\nA. Tokyo \nB. Hiroshima \nC. Nagasaki": "C",
}

# Shuffle the dictionary
l = list(questions.items())     # Convert dictionary into a list of tuples [(key, value), (key, value) etc]
random.shuffle(l)               # Shuffle the order of the list items
questions = dict(l)             # Turn the list of tuples back into a dictionary

points = 0                      # Initialize the points var
print("\n\nHello! This program is made by Vadim:) I hope you have a nice day!")
print("Please answer the following questions by typing A, B or C. You can't return to the previous question, so choose wisely")
while True:
    for key, value in questions.items():                            # For each item in dictionary
        answer = input(key+"\nMy answer is:   ").upper()            # The question (key) is printed and the user has to input the answer
        
        while answer not in questions.values():                     # If the answer is not defined in dictionary values - the loop will ask for a viable answer
            answer = input("Wrong input, try again: ").upper()

        if answer == value:                                         # Right answer
            print("Right answer!")
            print("------------------------------")
            points = points + 1                                     # +1 to the score
        elif answer != value:                                       # Wrong answer answer   
            print("Wrong answer!")
            print("------------------------------")

    print("Thanks for the game! Your score is {}.". format(points)) # After all items from the dictionary are checked, the score is pronted
    replay_var = input("Do you want to play again? y/n: ").lower()  # Anything but Y/y will restart the game
    if replay_var == "y":
        print("Restarting the game")
        points = 0                                                  # Resetting the points value
    else:                                                           
        print("Bye!")
        break                                                       # Breaking the while loop
