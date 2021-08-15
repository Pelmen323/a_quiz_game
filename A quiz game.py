import random

# Dictionaries with questions
python_quiz = {       #w3schools - 25/25 questions from https://www.w3schools.com/quiztest/quiztest.asp?qtest=PYTHON, others created while progressing Python to keep myself in shape
    'What is a correct syntax to output "Hello World" in Python?: \nA. p("Hello World") \nB. print("Hello World") \nC. echo "Hello World" \nD. echo("Hello World");': "B",
    'How do you insert COMMENTS in Python code?: \nA. #This is a comment \nB. /*This is a comment*/ \nC. //This is a comment': "A",
    'Which one is NOT a legal variable name?: \nA. my_var \nB. Myvar \nC. _myvar \nD. my-var': "D",
    'How do you create a variable with the numeric value 5?: \nA. x = int(5) \nB. Both answers are correct \nC. x = 5': "B",
    'What is the correct file extension for Python files?: \nA. .pyth \nB. .pt \nC. .pyt \nD. .py': "D",
    'How do you create a variable with the floating number 2.8?: \nA. x = float(2.8) \nB. x = 2.8 \nC. Both answers are correct': "C",
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
    # Some other questions from the Python course:
    'How to return a number of items in the container OR a length of string?: \nA. len() \nB. num() \nC. length() \nD. count()': "A",
    'How to import an object from other file (Class, function etc.)?: \nA. import file_name, object_name \nB. import object_name \nC. from file_name import object_name \nD. import object_name from file_name': "C",
    'How to import a file?: \nA. import file_name \nB. file_name.add \nC. from file_name import \nD. import.file_name ': "A",
    'How to initialize a Class?: \nA. def init(): \nB. def __init__(): \nC. def(): \nD. class.init() ': "B",
    'What the "Class" is ?: \nA. A type of loop \nB. A container with key-value pairs \nC. A "blueprint" to create objects \nD. Exception type ': "C",
    'What is an instanced variable of the Class?: \nA. It is declared outside the class and is a default value for created objects \nB. It is declared inside the class and can be unique for each object \nC. It has a common value for each object and is declared inside the __init__ method ': "B",
    'What a correct example of creating child class "Fish" (parent - Animals)?: \nA. class Fish(Animals): \nB. class Animals.Fish: \nC. class (Fish_Animals):': "A",
    'How to create an object "fish_1" of the class "Fish" (parent - Animals)?: \nA. fish_1 is Fish:  \nB. fish_1 = Fish(Animals): \nC. fish_1 = Fish(): \nD. fish_1 = Animals.Fish:': "C",
    'Class "Organism" has attribute "alive = True", its child class Animal has the method "running". What will inherit the child class of the Animal ?: \nA. only "running" \nB. "running" and "alive" \nC. nothing \nD. only "alive"': "B",
    'What is the difference between function and method?: \nA. They are the same in Python  \nB. Function is called by a name of associated object, method is just called on its name \nC. Method is called by a name of associated object, function is just called on its name': "C",
    'What is the difference between usual and abstract class?: \nA. Abstract class doesnt inherit anything  \nB. Objects of abstract class cant be created, as well as attributes/methods - inherited \nC. It is a class without methods': "B",
    'How to mark the method as abstract?: \nA. @abstractmethod  \nB. method_name.abstractmethod \nC. method_name(abstractmethod)': "A",
    'How to mark the class as abstract?: \nA. class Classname.abstract:  \nB. class Classname(abstract): \nC. class Classname(ABC):': "C",
    'What is a correct example of walrus operator usage instead of \n" happy = True \nprint(happy)  ": \nA. print(happy = True)  \nB. print(happy := True) \nC. you cant assign a variable while using it': "B",
    'Can the function be assigned to a variable?: \nA. only without input (i.e. var = print)  \nB. only with input (i.e. var = print("hello")) \nC. it cant \nD. It can be assigned regardless of passed arguments': "D",
    'Choose a correct example of lambda usage?: \nA. function_name = lambda argument1,argument2 : argument1+argument2  \nB. function_name = lambda(argument1,argument2) : argument1+argument2 \nC. function_name = lambda : argument1+argument2': "A",
    'Select the variant with the key, value, item of the dictionary Metallica:Battery : \nA. Battery, Metallica, Metallica:Battery  \nB. Metallica:Battery, Metallica, Battery \nC. Metallica, Battery, Metallica:Battery': "C",
    'What is the difference between sort() and sorted(): \nA. sorted() works only for lists and returns None (it mutates the original list), while sort() works for everything but creates a new object \nB. sort() works only for lists and returns None (it mutates the original list), while sorted() works for everything but creates a new object \nC. sorted() doesnt work with lists , while sort() works for everything \nD. They are identical': "B",
    'Select the correct variant of key to sort the list by the length of the strings: \nA. key = len  \nB. key = lambda x: len(x) \nC. key = x: len(x)': "B",
    'Select the correct variant of key to sort the list of tuples by the 2nd item of the tuples: list = [(name, A, 11),(name2, F, 2),(name3, A, 10)]: \nA. key= lambda x : x[1]  \nB. key=[1] \nC. key= x[1]': "A",
    'Select the correct variant of key to sort the list of tuples by the 3nd letter of 1st item of the tuples: list = [(name, A, 11),(name2, F, 2),(name3, A, 10)]: \nA. key= lambda x : x[2]  \nB. key=[2] \nC. key= lambda x: x[0][2]': "C",
    'Select the correct variant of key to sort the list of tuples by the 2nd item and then by the 1st item of the tuples: list = [(name, A, 11),(name2, F, 2),(name3, A, 10)]: \nA. key= lambda x : x[2] and x[1]  \nB. key= lambda x: (x[1], x[0]) \nC. key= lambda x: x[1][0]': "B",
}

http_quiz = { 
    #HTTP Training course https://www.linkedin.com/learning/http-essential-training plus some other questions (WIP)
    'What is HTTP?: \nA. Hyper Text Transfer Protocol:  \nB. Hyper Text Typing Protocol \nC. High Text Tooltip Protocol': "A",
    'For what HTTP is used?: \nA. To store data:  \nB. To transfer web documents using TCP/IP  \nC. To transfer text on a local machine ': "B",
    'What is true about HTTP and HTTPS: \nA. HTTP is no longer used  \nB. HTTPS is slower \nC. HTTPS uses encryption': "C",
    'What is TCP (to transfer data between server and client): \nA. Transmission Control Protocol  \nB. Transmission Creation Protocol \nC. Transfer Control Protocol': "A",
    'What is IP: \nA. Internet Paradigm \nB. Illustration Protocol \nC. Internet Protocol': "C",
    'What is URL (universal resource locator): \nA. Non-human-read address of the resource on the Web \nB. Human-read address of the resource on the Web with the method to access that resource': "B",
    'What is DNS (Domain Name Server) used for: \nA. To store domain URLs and point them to the IPs of the servers \nB. To show human-read address in the browser and navigate to them ': "A",
    'How the server and client communicate: \nA. Using requests only \nB. Using request-response-request combination \nC. Using request-response pairs': "C",
    'What is header part of the HTTP request/response used for: \nA. To transfer data about the request/response \nB. To transfer data that is needed to be POST/PUT or PATCH on the server \nC. To transfer methods only': "A",
    'HTTP request method GET: \nA. To get something from the server \nB. To update existing resource with replacing all or some of its content \nC. To add something \nD. To create a new resource (example - submitting a form)': "A",
    'HTTP request method POST: \nA. Always for creating a resource (even if it is a duplicate) \nB. For checking if resource exists then update, else create new resource \nC. Always to update a resource ': "A",
    'HTTP request method PUT: \nA. Always for creating a resource (even if it is a duplicate) \nB. For checking if resource exists then update, else create new resource \nC. Always to update a resource ': "B",
    'HTTP request method PATCH: \nA. Always for creating a resource (even if it is a duplicate) \nB. For checking if resource exists then update, else create new resource \nC. Always to update a resource ': "C",
    'HTTP request method DELETE: \nA. To get something from the server \nB. To update existing resource with replacing all or some of its content \nC. To update something \nD. To delete something': "D",
    'HTTP response code 200: \nA. OK \nB. Not found \nC. Resource created \nD. Access denied': "A",
    'HTTP response code 201: \nA. OK \nB. Not found \nC. Resource created \nD. Access denied': "C",
    'HTTP response code 403: \nA. Method not allowed \nB. Not found \nC. Internal server error \nD. Access denied (Method is allowed)': "D",
    'HTTP response code 404: \nA. Method not allowed \nB. Not found \nC. Internal server error \nD. Access denied (Method is allowed)': "B",
    'HTTP response code 405: \nA. Method not allowed \nB. Not found \nC. Internal server error \nD. Access denied (Method is allowed)': "A",
    'HTTP response code 500: \nA. Service unavailable \nB. Not found \nC. Internal server error \nD. Access denied': "C",
    'HTTP response code 503: \nA. Service unavailable \nB. Not found \nC. Internal server error \nD. Access denied': "A",
    'Mandatory parts of HTTP message : \nA. Method to define the action \nB. URL to point the requested resource \nC. Both': "C",
    'In "https://google.com/learning/index.html" how "https" and "google.com/learning" parts are called? : \nA. Protocol declaration and URL \nB. Protocol declaration and URN (Uniform resource name) \nC. Protocol declaration and URI': "B",
    'What host part of the URL (google.com) is used for? : \nA. It is a name which is registered for a certain DNS (domain name server), which points client to a certain IP \nB. It directly shows the IP of the resource to the client': "A",
    'Correct example of URL resource path ? : \nA. https://google.com/learning.html \nB. google.com \nC. /index.html': "C",
    'Correct example of chained URL query (for example - stores user name or encoding etc) ? : \nA. u=12345&q=abcd \nB. ?u=12345&q=abcd \nC. ?u=12345?q=abcd': "B",
    'How server can track the actions of user (example - automatic login when reloading the page)? : \nA. Using requests/responses \nB. Using caching \nC. Using cookies': "C",
    'How server can send some data to client to avoid redownloading the same element a lot of times? : \nA. Using requests/responses \nB. Using caching \nC. Using cookies': "B",
    'What is REST API?: \nA. Representation State Transfer Application Programming Interface': "A",
    'REST API is a set of rules: \nA. To receive standard verbs (GET, POST, PUT etc) and return standardized data (resource -.xml or .json)': "A",
    'Why is HTTP needed?: \nA. To send a request to the server and receive a response in readable for client format \nB. To process the request and send back the requested data \nC. To store data/content' : "A",
    'Why is REST API needed?: \nA. To send a request to the server and receive a response in readable for client format \nB. To process the request and send back the requested data \nC. To store data/content' : "B",
    'Why is database (SQL) needed?: \nA. To send a request to the server and receive a response in readable for client format \nB. To process the request and send back the requested data/creates a new entities/updates, deletes existing \nC. To store data/content' : "C",
    'HTML part of the webpage is?: \nA. Content on the webpage \nB. Layout of the content on the webpage \nC. Manipulations with document/styes': "A",
    'CSS part of the webpage is?: \nA. Content on the webpage \nB. Layout of the content on the webpage \nC. Manipulations with document/styes': "B",
    'JavaScript part of the webpage is?: \nA. Content on the webpage \nB. Layout of the content on the webpage \nC. Manipulations with document/styes': "C",
}
# Choose the quiz
def selecting_quiz():           
    selected_dictionary = None
    while True:
        if selected_dictionary == "python":
            questions = python_quiz
            break
        elif selected_dictionary == "http":
            questions = http_quiz
            break
        else:
            selected_dictionary = input("Please, input the name of the test you want to take. Currently available: Python, HTTP: ").lower()
    return questions

# Shuffle the questions order
def shuffling():                
    questions = selecting_quiz()
    l = list(questions.items())     # Convert dictionary into a list of tuples [(key, value), (key, value) etc]
    random.shuffle(l)               # Shuffle the order of the list items
    questions = dict(l)             # Turn the list of tuples back into a dictionary
    return questions
                                          
# Print the answers
def print_answers(list_var):    
    for i in list_var:
        print(i, end=" ")
    return print()

# Print the results
def quitting(points, user_answers_list, right_answers_list):
    score_var = str(round(points/(len(questions))*100))             # Calculate the % of the right answers. len() calculates num of objects in container
    print("Thanks for the game! Your score is {}%. You've answered {}/{} questions right". format(score_var, points, len(questions))) # After all items from the dictionary are checked, the score is pronted
    print("Inputted answers: ", end=" ")
    print_answers(user_answers_list)
    print("Expected answers: ", end=" ")
    print_answers(right_answers_list)


points = 0                      # Initialize the points var
user_answers_list = []          # Initializing lists var to save input
right_answers_list = []         
var_quest_number = 1            # Questions number starts from 1

print("\n\n###############################################\nHello! This program is made by Vadzim:) I hope you have a nice day!")
print("- Answer the following questions by typing A, B, C or D. \n- You can't return to the previous question, so choose wisely. \n- Inputting 'End' will close the game.\n###############################################\n")

while True:
    questions = shuffling()                                         # Start with selecting the dict and shuffling

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
    else:           #The else part WILL be executed only if the for loop was NOT broken (see the 'END' part which breaks the loop)
        quitting(points, user_answers_list, right_answers_list)
                                         # Restart functionality
        replay_var = input("Do you want to play again? y/n: ").lower()  # Anything but Y/y will restart the game
        if replay_var == "y":
            print("Restarting the game...\n")
            points = 0                                                  # Resetting the points value
            var_quest_number = 1
            user_answers_list.clear()
            right_answers_list.clear()
            continue                                                    # Restarting the 'while' loop
        else:                                                           
            break                                                       # Breaking the the inner loop
    break                                                               # Breaking the outer loop, used only in 'End' functionality to exit the while loop
print("Bye!")