import random

# Input your questions
questions = {       #w3schools - 25/25 questions from https://www.w3schools.com/quiztest/quiztest.asp?qtest=PYTHON
    'What is a correct syntax to output "Hello World" in Python?: \nA. p("Hello World") \nB. print("Hello World") \nC. echo "Hello World" \nD. echo("Hello World");': "B",
    'How do you insert COMMENTS in Python code?: \nA. #This is a comment \nB. /*This is a comment*/ \nC. //This is a comment': "A",
    'Which one is NOT a legal variable name?: \nA. my_var \nB. Myvar \nC. _myvar \nD. my-var': "D",
    'How do you create a variable with the numeric value 5?: \nA. x = int(5) \nB. Both the other answers are correct \nC. x = 5': "B",
    'What is the correct file extension for Python files?: \nA. .pyth \nB. .pt \nC. .pyt \nD. .py': "D",
    'How do you create a variable with the floating number 2.8?: \nA. x = float(2.8) \nB. x = 2.8 \nC. Both the other answers are correct': "C",
    'What is the correct syntax to output the type of a variable or object in Python?: \nA. print(type(x)) \nB. print(typeof x) \nC. print(typeOf(x)) \nD. print(typeof(x))': "A",
    'What is the correct way to create a function in Python?: \nA. def myFunction(): \nB. create myFunction(): \nC. function myfunction():': "A",
    'In Python, single quotes Hello single quotes, is the same as "Hello": \nA. True \nB. False': "A",
    'What is a correct syntax to return the first character in a string?: \nA. x = "Hello".sub(0, 1) \nB. x = sub("Hello", 0, 1) \nC. x = "Hello"[0]': "C",
    'Which method can be used to remove any whitespace from both the beginning and the end of a string?: \nA. strip() \nB. trim() \nC. len() \nD. ptrim()': "A",
    'Which method can be used to return a string in upper case letters?: \nA. upperCase() \nB. upper() \nC. uppercase() \nD. toUpperCase()': "B",
    'Which method can be used to replace parts of a string?: \nA. repl() \nB. replace() \nC. replaceString() \nD. switch()': "B",
    'Which operator is used to multiply numbers?: \nA. # \nB. % \nC. x \nD. *': "D",
    'Which operator can be used to compare two values?: \nA. <> \nB. = \nC. == \nD. ><': "C",
    'Which of these collections defines a LIST?: \nA. {"apple", "banana", "cherry"} \nB. {"name": "apple", "color": "green"} \nC. ("apple", "banana", "cherry") \nD. ["apple", "banana", "cherry"]': "D",
    'Which of these collections defines a TUPLE?: \nA. {"apple", "banana", "cherry"} \nB. {"name": "apple", "color": "green"} \nC. ("apple", "banana", "cherry") \nD. ["apple", "banana", "cherry"]': "C",
    'Which of these collections defines a SET?: \nA. {"apple", "banana", "cherry"} \nB. {"name": "apple", "color": "green"} \nC. ("apple", "banana", "cherry") \nD. ["apple", "banana", "cherry"]': "A",
    'Which of these collections defines a DICTIONARY?: \nA. {"apple", "banana", "cherry"} \nB. {"name": "apple", "color": "green"} \nC. ("apple", "banana", "cherry") \nD. ["apple", "banana", "cherry"]': "B",
    'Which collection is ordered, changeable, and allows duplicate members?: \nA. DICTIONARY \nB. LIST \nC. TUPLE \nD. SET': "B",
    'Which collection does not allow duplicate members?: \nA. LIST \nB. SET \nC. TUPLE': "B",
    'How do you start writing an if statement in Python?: \nA. if x > y then: \nB. if x > y: \nC. if (x > y)': "B",
    'How do you start writing a while loop in Python?: \nA. while x > y: \nB. x > y while { \nC. while x > y { \nD. while (x > y)': "A",
    'How do you start writing a for loop in Python?: \nA. for x > y: \nB. for x in y: \nC. for each x in y:': "B",
    'Which statement is used to stop a loop?: \nA. return \nB. stop \nC. exit \nD. break': "D",
    "Which collection is unordered and doesn't allow duplicates?: \nA. DICTIONARY \nB. LIST \nC. TUPLE \nD. SET": "D",
    'Which collection consists of unique key:value pairs?: \nA. DICTIONARY \nB. LIST \nC. TUPLE \nD. SET': "A",
    'Which collection is unchangeable?: \nA. DICTIONARY \nB. LIST \nC. TUPLE \nD. SET': "C",
}

# Shuffle the dictionary
l = list(questions.items())     # Convert dictionary into a list of tuples [(key, value), (key, value) etc]
random.shuffle(l)               # Shuffle the order of the list items
questions = dict(l)             # Turn the list of tuples back into a dictionary

points = 0                      # Initialize the points var
user_answers_list = []          # Initializing lists var to save input
right_answers_list = []
var_quest_number = 1
                                            # Function to print the answers
def print_answers(list_var):    
    for i in list_var:
        print(i, end=" ")
    return print()

def quitting(points, user_answers_list, right_answers_list):
    score_var = str(round(points/(len(questions))*100))             # Calculate the % of the right answers. len() calculates num of objects in container
    print("Thanks for the game! Your score is {}%. You've answered {}/{} questions right". format(score_var, points, len(questions))) # After all items from the dictionary are checked, the score is pronted
    print("Inputted answers: ", end=" ")
    print_answers(user_answers_list)
    print("Expected answers: ", end=" ")
    print_answers(right_answers_list)

z = 1
print("\n\nHello! This program is made by Vadim:) I hope you have a nice day!")
print("Please answer the following questions by typing A, B or C. You can't return to the previous question, so choose wisely. Inputting 'End' will close the game")
while True:
    for key, value in questions.items():                            # For each item in dictionary
        answer = input(str(var_quest_number) + ". " + key +"\nMy answer is:   ").upper()            # The question (key) is printed and the user has to input the answer

        if answer == 'END':
            quitting(points, user_answers_list, right_answers_list)
            break                                                   # Breaking the the inner loop

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
        var_quest_number = var_quest_number + 1
                                            # Printing the game stats
    else:
        quitting(points, user_answers_list, right_answers_list)
                                         # Restart functionality
        replay_var = input("Do you want to play again? y/n: ").lower()  # Anything but Y/y will restart the game
        if replay_var == "y":
            print("Restarting the game")
            points = 0                                                  # Resetting the points value
            var_quest_number = 1
            user_answers_list.clear()
            right_answers_list.clear()
            continue
        else:                                                           
            break                                                       # Breaking the the inner loop
    break
print("Bye!")