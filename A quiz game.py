import random

# Input your questions
questions = {       #w3schools 12/25 questions added https://www.w3schools.com/quiztest/quiztest.asp?qtest=PYTHON
    'What is a correct syntax to output "Hello World" in Python?: \nA. p("Hello World") \nB. print("Hello World") \nC. echo "Hello World" \nD. echo("Hello World");': "B",
    'How do you insert COMMENTS in Python code?: \nA. #This is a comment \nB. /*This is a comment*/ \nC. //This is a comment': "A",
    'Which one is NOT a legal variable name?: \nA. my_var \nB. Myvar \nC. _myvar \nD. my-var': "C",
    'How do you create a variable with the numeric value 5?: \nA. x = int(5) \nB. Both the other answers are correct \nC. x = 5': "B",
    'What is the correct file extension for Python files?: \nA. .pyth \nB. .pt \nC. .pyt \nD. .py': "D",
    'How do you create a variable with the floating number 2.8?: \nA. x = float(2.8) \nB. x = 2.8 \nC. Both the other answers are correct': "C",
    'What is the correct syntax to output the type of a variable or object in Python?: \nA. print(type(x)) \nB. print(typeof x) \nC. print(typeOf(x)) \nD. print(typeof(x))': "A",
    'What is the correct way to create a function in Python?: \nA. def myFunction(): \nB. create myFunction(): \nC. function myfunction():': "A",
    'In Python, single quotes Hello single quotes, is the same as "Hello": \nA. True \nB. False': "A",
    'What is a correct syntax to return the first character in a string?: \nA. x = "Hello".sub(0, 1) \nB. x = sub("Hello", 0, 1) \nC. x = "Hello"[0]': "C",
    'Which method can be used to remove any whitespace from both the beginning and the end of a string?: \nA. strip() \nB. trim() \nC. len() \nD. ptrim()': "A",
    'Which method can be used to return a string in upper case letters?: \nA. upperCase() \nB. upper() \nC. uppercase() \nD. toUpperCase()': "B",
    "Select the correct info and syntax of lists in Python:\nA.[], changeable, ordered \nB. (), unchangeable, ordered \nC. {}, changeable, unordered \nD. {:}, changeable, ordered": "A",
    "Select the correct info and syntax of tuples in Python:\nA.[], changeable, ordered \nB. (), unchangeable, ordered \nC. {}, changeable, unordered \nD. {:}, changeable, ordered": "B",
    "Select the correct info and syntax of sets in Python:\nA.[], changeable, ordered \nB. (), unchangeable, ordered \nC. {}, changeable, unordered \nD. {:}, changeable, ordered": "C",
    "Select the correct info and syntax of dictionaries in Python:\nA.[], changeable, ordered \nB. (), unchangeable, ordered \nC. {}, changeable, unordered \nD. {:}, changeable, ordered": "D",
}

# Shuffle the dictionary
l = list(questions.items())     # Convert dictionary into a list of tuples [(key, value), (key, value) etc]
random.shuffle(l)               # Shuffle the order of the list items
questions = dict(l)             # Turn the list of tuples back into a dictionary

points = 0                      # Initialize the points var
user_answers_list = []          # Initializing lists var to save input
right_answers_list = []
                                         # Function to print the answers
def print_answers(list_var):    
    for i in list_var:
        print(i, end=" ")
    return print()

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
        user_answers_list.append(answer)                            # Saving inputted answer
        right_answers_list.append(value)                            # Saving correct answer

                                            # Printing the game stats
    score_var = str(round(points/(len(questions))*100))             # Calculate the % of the right answers. len() calculates num of objects in container
    print("Thanks for the game! Your score is {}%. You've answered {} questions right". format(score_var, points)) # After all items from the dictionary are checked, the score is pronted
    print("Inputted answers: ", end=" ")
    print_answers(user_answers_list)
    print("Expected answers: ", end=" ")
    print_answers(right_answers_list)
                                            # Restart functionality
    replay_var = input("Do you want to play again? y/n: ").lower()  # Anything but Y/y will restart the game
    if replay_var == "y":
        print("Restarting the game")
        points = 0                                                  # Resetting the points value
        total_answers = 0
        user_answers_list.clear()
        right_answers_list.clear()
    else:                                                           
        print("Bye!")
        break                                                       # Breaking the while loop
