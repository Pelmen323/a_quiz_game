import random

# Dictionaries with questions
python1_quiz = {                                                                    # w3schools - 25/25 questions from https://www.w3schools.com/quiztest/quiztest.asp?qtest=PYTHON, others created while progressing Python to keep myself in shape
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
    'What is true about indexing "tree"[0:3]?: \nA. x and y are inclusive ("tree") \nB. y is inclusive, x is not ("ree") \nC. x is inclusive, y is not ("tre") \nD. both x and y are exclusive ("re")': "C",
    'What is the difference between continue and pass?: \nA. pass starts the next iteration of for loop without executing the rest of the loop, continue does nothing \nB. they both start the next iteration of for loop \nC. pass finishes the for loop, continue starts the next iteration of the for loop \nD. continue starts the next iteration of for loop without executing the rest of the loop, pass does nothing': "D",
}
python2_quiz = {                                                                # Some other questions from the Python course (intermediate):
    'How to return a number of items in the container OR a length of string?: \nA. len() \nB. num() \nC. length() \nD. count()': "A",
    'How to import an object from other file (Class, function etc.)?: \nA. import file_name, object_name \nB. import object_name \nC. from file_name import object_name \nD. import object_name from file_name': "C",
    'How to import a file?: \nA. import file_name \nB. file_name.add \nC. from file_name import \nD. import.file_name ': "A",
    'What is a correct example of walrus operator usage instead of \n" happy = True \nprint(happy)  ": \nA. print(happy = True)  \nB. print(happy := True) \nC. you cant assign a variable while using it': "B",
    'Can the function be assigned to a variable?: \nA. only without input (i.e. var = print)  \nB. only with input (i.e. var = print("hello")) \nC. it cant \nD. It can be assigned regardless of passed arguments': "D",
    'Choose a correct example of lambda usage?: \nA. function_name = lambda argument1,argument2 : argument1+argument2  \nB. function_name = lambda(argument1,argument2) : argument1+argument2 \nC. function_name = lambda : argument1+argument2': "A",
    'Select the variant with the key, value, item of the dictionary Metallica:Battery : \nA. Battery, Metallica, Metallica:Battery  \nB. Metallica:Battery, Metallica, Battery \nC. Metallica, Battery, Metallica:Battery': "C",
    "What is the difference between sort() and sorted(): \nA. sorted() works only for lists and returns None (it mutates the original list), while sort() works for everything but creates a new object \nB. sort() works only for lists and returns None (it mutates the original list), while sorted() works for everything but creates a new object \nC. sorted() doesn't work with lists , while sort() works for everything \nD. They are identical": "B",
    'Select the correct variant of key to sort the list by the length of the strings: \nA. key = len  \nB. key = lambda x: len(x) \nC. key = x: len(x)': "B",
    'Select the correct variant of key to sort the list of tuples by the 2nd item of the tuples: list = [(name, A, 11),(name2, F, 2),(name3, A, 10)]: \nA. key= lambda x : x[1]  \nB. key=[1] \nC. key= x[1]': "A",
    'Select the correct variant of key to sort the list of tuples by the 3rd letter of 1st item of the tuples: list = [(name, A, 11),(name2, F, 2),(name3, A, 10)]: \nA. key= lambda x : x[2]  \nB. key=[2] \nC. key= lambda x: x[0][2]': "C",
    'Select the correct variant of key to sort the list of tuples by the 2nd item and then by the 1st item of the tuples: list = [(name, A, 11),(name2, F, 2),(name3, A, 10)]: \nA. key= lambda x : x[2] and x[1]  \nB. key= lambda x: (x[1], x[0]) \nC. key= lambda x: x[1][0]': "B",
    'Correct example of map function usage to multiply by 1.5 the 2nd element of a tuple in the list [("Jeans", 10), ("Jacket", 25)]?: \nA. func_name = x:= (x[0], x[1]*1.5)  \nB. func_name = lambda x: x[0], x[1]*1.5 \nC. func_name = lambda x: (x[1], x[2]*1.5) \nD. func_name = lambda x: (x[0], x[1]*1.5)': "D",
    'Correct example of map function usage to capitalize the 1st element of a tuple in the list [("jeans", 10), ("jacket", 25)]?: \nA. func_name = x:= x[0], x[1].capitalize()  \nB. func_name = lambda x: (x[0].capitalize(), x[1]) \nC. func_name = lambda x: (x[0], x[1].capitalize()) \nD. func_name = lambda x: (x[0], x[1]).capitalize()': "B",
    'Correct example of filter() function usage to get the iterable from the list of tuples list_name = [("ABC", 10),("ABA", 22),("ABB", 36) ] with 2nd value of each tuple > 18: \nA. func_name = x:x[1] >= 18 \nlist(filter(func_name, list_name))  \nB. func_name = lambda x: x.1 >= 18 \nlist(filter(func_name, list_name)) \nC. func_name = lambda x: x[1] >= 18 \nlist(filter(func_name, list_name))': "C",
    'Correct example of reduce function usage to get the sum of all elements of the list = [1, 2, 3, 4, 5]: \nA. var = functools.reduce(x+y, list))  \nB. var = functools.reduce(lambda x, y: x+y, list) \nC. var.reduce(lambda x, y: x+y, list)': "B",
    'Correct example of list comprehension: \nA. list_squares = [i*i for i in range (1, 11)]  \nB. list_more_60 = [i for i in iterable_var if i>=60]  \nC. list_more_60_else_failed = [i if i>=60 else "Failed" for i in iterable_var] \nD. All mentioned variants are correct': "D",
    'Correct return of 1. 5 % 2 and 2. 10 % 2: \nA. 2,5 ; 5  \nB. 250 ; 500 \nC. 0 ; 1 \nD. 1 ; 0': "D",
    'How to backward the whole string using [::]?: \nA. [1::1]  \nB. val[-1::] \nC. val[::-1] \nD. val[-1:-1:-1]': "C",
    'What will var[-5:-2] return if var = "chicken"?: \nA. nothing  \nB. "ick" \nC. "icke" \nD. "ekci"': "B",
    'What will var[-2:-5] return if var = "chicken"?: \nA. nothing  \nB. "ick" \nC. "icke" \nD. "ekci"': "A",
    'How to find a difference between two dates in tuple format a = (1982, 4, 19), b = (1982, 4, 22) (output should be an integer)?: \nA. abs(((datetime(a[0], a[1], a[2]))-(datetime(b[0], b[1], b[2])))) \nB. abs(((datetime.date(a[0], a[1], a[2]))-(datetime.date(b[0], b[1], b[2]))).days) \nC. abs(a-b) \nD. abs(((datetime.date(a[0], a[1], a[2]))-(datetime.date(b[0], b[1], b[2])))': "B",
    "What'return (','.join(phrases)).replace('right', 'left')' will return if phrases = ('bright aright right', 'ok')?: \nA. nothing  \nB. 'bleft aleft left,ok' \nC. 'bright, alright, right, ok' \nD. 'bleft, aleft, left, ok' ": "B",
    'What func is used to count the amount of matches in tuple or in string?: \nA. .len() \nB. .amount() \nC. .count() \nD. .findall': "C",
}
python3_quiz = {                                                                # Random, OS, advanced stuff
    'How to generate a random integer?: \nA. random.randint(x, y) \nB. random.random() \nC. random.shuffle \nD. random.choice': "A",
    'How to generate a random float from 0 to 1?: \nA. random.randint(x, y) \nB. random.random() \nC. random.shuffle \nD. random.choice': "B",
    'How to randomly change the order of items in the iterable?: \nA. random.randint(x, y) \nB. random.random() \nC. random.shuffle \nD. random.choice': "C",
    'How to select a random value from the iterable?: \nA. random.randint(x, y) \nB. random.random() \nC. random.shuffle \nD. random.choice': "D",
    'How to select random values for several times?: \nA. Cant do that \nB. You have to rewrite the program each time \nC. use for loop, but only with random.choice (random.choice(iterable) for i in range(x)) \nD. Same as C, but for other functions too, like random.randint or random.random': "D",
    'How to check if the path exists in system?: \nA. os.path.isfile \nB. os.path.isdir \nC. os.path.exists ': "C",
    'How to create a file or overwrite the file?: \nA. with open(path, "w") as i: i.write(text) \nB. with open(path, "r") as i: i.write(text) \nC. with open(path, "a") as i: i.write(text) ': "A",
    'How to create a file or add the text to the file?: \nA. with open(path, "w") as i: i.write(text) \nB. with open(path, "r") as i: i.read() \nC. with open(path, "a") as i: i.write(text) ': "C",
    'How to print the contents of the file?: \nA. with open(path, "w") as i: i.write(text) \nB. with open(path, "r") as i: i.read() \nC. with open(path, "a") as i: i.write(text) ': "B",
    'How make, move and delete a folder?: \nA. os.makedirs(), os.replace(path1, path2), os.removedirs() \nB. os.mkdir(), os.replace(path1, path2), os.rmdir() \nC. os.replace(path1, path2), os.removedirs(), os.makedirs()': "A",
    'How to copy a file (without removing the original file)?: \nA. os.replace(path1, path2) \nB. shutil.copyfile(path1, path2) \nC. os.copy(path1, path2) ': "B",
    'How to delete a file?: \nA. os.delete \nB. os.remove ': "B",
    "Why do we need a tuple if we have lists?: \nA. They are needed since operations with them are faster than with lists \nB. I don't use tuples, they are obsolete \nC. They are entirely different since tuples store key:value pairs": "A",
    "How to copy an iterable to modify the copy without affecting the copied one?: \nA. Variants C, D and = (list2 = list1) \nB. You can't copy an iterable \nC. Only use .copy method (list2 = list1.copy()) \nD. variant C and indexing (list2 = list1[:]) or list func (list2 = list(list1)) ": "D",
    'How to change or add an item to the dict?: \nA. dict_name.update(key:value) \nB. dict is immutable \nC. dict_name.update(key:value) or dict[key]=value': "C",
    'What will be returned by dict_name.keys(), dict_name.values(), dict_name.items()?: \nA. 3 lists  \nB. 2 sets and 1 dict \nC. 1 dict and 2 lists \nD. 2 set-like objects and 1 dict-like object': "D",
    'Set A - {1, 2, 3}, Set B - {1, 2, 3, 4, 5}. What will return a.issubset(b), b.issuperset(a), a.isdisjoint(b)?: \nA. True False False  \nB. True True False \nC. True True True \nD. False False False': "B",
    'How raise AssertionError if x is less than zero?: \nA. AssertionError if x < 0 \nB. assert(x < 0) \nC. if x <= 0: raise AssertionError \nD. assert(raise Exception if x < 0) ': "B",
}
http_quiz = {                                                                   # HTTP Training course https://www.linkedin.com/learning/http-essential-training plus some other questions (WIP)
    'What is HTTP?: \nA. Hyper Text Transfer Protocol:  \nB. Hyper Text Typing Protocol \nC. High Text Tooltip Protocol': "A",
    'What is true about HTTP and HTTPS: \nA. HTTP is no longer used  \nB. HTTPS is slower \nC. HTTPS uses encryption': "C",
    'What is TCP (to transfer data between server and client): \nA. Transmission Control Protocol  \nB. Transmission Creation Protocol \nC. Transfer Control Protocol': "A",
    'What is IP: \nA. Internet Paradigm \nB. Illustration Protocol \nC. Internet Protocol': "C",
    'What is DNS (Domain Name Server) used for: \nA. To store domain URLs and point them to the IPs of the servers \nB. To show human-read address in the browser and navigate to them ': "A",
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
    'Correct example of chained URL query (for example - stores user name or encoding etc) ? : \nA. u=12345&q=abcd \nB. ?u=12345&q=abcd \nC. ?u=12345?q=abcd': "B",
    'How server can track the actions of user (example - automatic login when reloading the page)? : \nA. Using requests/responses \nB. Using caching \nC. Using cookies': "C",
    'How server can send some data to client to avoid redownloading the same element a lot of times? : \nA. Using requests/responses \nB. Using caching \nC. Using cookies': "B",
    'What is REST API?: \nA. Representation State Transfer Application Programming Interface': "A",
    'REST API is a set of rules: \nA. To receive standard verbs (GET, POST, PUT etc) and return standardized data (resource -.xml or .json)': "A",
    'Why is HTTP needed?: \nA. To send a request to the server and receive a response in readable for client format \nB. To process the request and send back the requested data \nC. To store data/content': "A",
    'Why is REST API needed?: \nA. To send a request to the server and receive a response in readable for client format \nB. To process the request and send back the requested data \nC. To store data/content': "B",
    'Why is database (SQL) needed?: \nA. To send a request to the server and receive a response in readable for client format \nB. To process the request and send back the requested data/creates a new entities/updates, deletes existing \nC. To store data/content': "C",
    'HTML part of the webpage is?: \nA. Content on the webpage \nB. Layout of the content on the webpage \nC. Manipulations with document/styes': "A",
    'CSS part of the webpage is?: \nA. Content on the webpage \nB. Layout of the content on the webpage \nC. Manipulations with document/styes': "B",
    'JavaScript part of the webpage is?: \nA. Content on the webpage \nB. Layout of the content on the webpage \nC. Manipulations with document/styes': "C",
}
pytest = {
    'What does "object.__new__.__defaults__ = (param1, param2 ...)" do?: \nA. Alters created object \nB. Deletes created object \nC. Sets default values for new objects ': "C",
    'What does "_asdict" do (OOP - namedtuple object)?: \nA. Modifies initial tuple into dict \nB. Returns initial tuple contents in form of dict ': "B",
    'What does "_replace" do (OOP - dict objects)?: \nA. Alters passed values of key=value pairs \nB. Same as .replace() ': "A",
    'How to run pytest and get full info on fails: \nA. pytest \nB. pytest -v \nC. pytest -v (and all files should have function calls) \nD. pytest -all ': "B",
    'How to name files for pytest to recognize?: \nA. test_ \nB. _test \nC. _test_ \nD. test_ or _test or directly pass the name file': "D",
}
oop = {
    'What the "Class" is ?: \nA. A type of loop \nB. A container with key-value pairs \nC. A "blueprint" to create objects \nD. Exception type ': "C",
    'How to initialize a Class object?: \nA. def init(): \nB. def __init__(): \nC. def(): \nD. class.init() ': "B",
    'What is the difference between function and method?: \nA. They are the same in Python  \nB. Function is called by a name of associated object, method is just called on its name \nC. Method is called by a name of associated object, function is just called on its name': "C",
    'What is an instanced variable of the Class?: \nA. It is declared outside the class and has only one value for all created objects \nB. It is declared inside the class and can be unique for each object \nC. It has a common value for each object and is declared inside the __init__ method ': "B",
    'What a correct example of creating child class "Fish" (parent - Animals)?: \nA. class Fish(Animals): \nB. class Animals.Fish: \nC. class (Fish_Animals):': "A",
    'How to create an object "fish_1" of the class "Fish" (parent - Animals)?: \nA. fish_1 is Fish:  \nB. fish_1 = Fish(Animals): \nC. fish_1 = Fish(): \nD. fish_1 = Animals.Fish:': "C",
    'Class "Organism" has attribute "alive = True", its child class Animal has the method "running". What will inherit the child class of the Animal ?: \nA. only "running" \nB. "running" and "alive" \nC. nothing \nD. only "alive"': "B",
    "What is the difference between usual and abstract class?: \nA. Abstract class doesn't inherit anything  \nB. Objects of abstract class cant be created, as well as attributes/methods - inherited \nC. It is a class without methods": "B",
    'How to mark the method as abstract?: \nA. @abstractmethod  \nB. method_name.abstractmethod \nC. method_name(abstractmethod)': "A",
    'How to mark the class as abstract?: \nA. class Classname.abstract:  \nB. class Classname(abstract): \nC. class Classname(ABC):': "C",
    'How to get all object-specific attributes?: \nA. name.attribute \nB. object._class__attribute \nC. object.__dict__ \nD. object.__doc__ ': "C",
    'How to get/set NON-PRIVATE object attribute?: \nA. name.attribute \nB. object._class__attribute \nC. name.__dict__ \nD. name.__doc__ ': "A",
    'How to get/set PRIVATE object attribute?: \nA. name.attribute \nB. object._class__attribute \nC. name.__dict__ \nD. name.__doc__ ': "B",
    'How to get the class/method documentation?: \nA. name.attribute \nB. object._class__attribute \nC. name.__dict__ \nD. name.__doc__ ': "D",
    'Correct example of decorator?: \nA. object = property()  \nB. self.object = decorator_name \nC. @decorator_name': "C",
    'What decorator takes and returns?: \nA. value, value  \nB. function, function \nC. nothing': "B",
    'Main purpose of property?: \nA. To call custom methods (getter/setter/deleter) behind the scenes while user calls attributes of the object \nB. To take a function, perform actions around it and return the function with its result, like an external layer of the function \nC. To access private methods and attributes of the object': "A",
    'What takes the method @classmethod?: \nA. object of a class  \nB. function \nC. class \nD. nothing': "C",
    'What takes the method @staticmethod?: \nA. object of a class  \nB. function \nC. class \nD. nothing': "D",
    'What methods are called "magic" or "dunder"?: \nA. @method  \nB. __method__ \nC. any class method \nD. only getters, setters, deleters and init': "B",
    'What method should be defined to change the result of "print(object)"?: \nA. __str__/__repr__  \nB. __len__ \nC. __eq__/__gt__/__ge__ \nD. __bool__': "A",
    'What method should be defined to make "len(object)" possible to call?: \nA. __str__/__repr__  \nB. __len__ \nC. __eq__/__gt__/__ge__ \nD. __bool__': "B",
    'What methods should be defined to perform comparisons between objects?: \nA. __iter__/__next__  \nB. __getitem__, __setitem__, __delitem__ \nC. __eq__/__gt__/__ge__ \nD. __bool__': "C",
    'Why it is important to re-define __hash__ method when changing the __eq__ method?: \nA. Because hash method is annulled when changing the __eq__ one. Hash is used if object is a dict key  \nB. No need - hash is annulled when changing __eq__ but it doesnt affect common operations \nC. No need - hash doesnt depend on __eq__': "A",
    'What method should be defined to perform custom checks if the object is true or false with bool() func (default is always True)"?: \nA. __str__/__repr__  \nB. __len__ \nC. __eq__/__gt__/__ge__ \nD. __bool__': "D",
    'Is it possible to call object as a function ( object() )?: \nA. No  \nB. Yes, by default \nC. Yes, if __call__ is defined': "C",
    'Difference between polymorphism and duck typing?: \nA. Same  \nB. Polymorphism is related to the ability of child classes override the parents methods, while duck typing is about objects of different classes having the same methods and attributes': "B",
    'What methods should be defined to use [index] or ["key"] with objects?: \nA. __str__/__repr__  \nB.__getitem__, __setitem__, __delitem__\nC. __eq__/__gt__/__ge__ \nD. __bool__': "B",
    'How to make objects iterable?: \nA. __iter__/__next__ \nB. __getitem__, __setitem__, __delitem__ \nC. __eq__/__gt__/__ge__ \nD. __bool__': "A",
    'How to reuse parent method in child class method?: \nA. Just replace the whole method  \nB. Create a new separate method \nC. Use super() to call parent class method during child class method (super().__init__()) ': "C",
    'Alternative to super().__init__(arg)?: \nA. super.__init__(self, arg) \nB. object(arg).__init__ \nC. Class.__init__(self, arg)': "C",
    'Classes Tiger and Lion have the same method "purr". Class Cat is created via "class Cat(Lion, Tiger). Method of which class will be used if super().purr is used in class Cat?: \nA. Tiger \nB. Lion \nC. Object': "B",
    'What does __slots__ do?: \nA. Limits available attributes by defining them in an iterable \nB. Limits available methods by defining them in an iterable\nC. Limits available properties by defining them in an iterable': "A",
    'Do child classes use __slots__ if it is defined in parent class but not defined in child class?: \nA. Yes \nB. No ': "B",
    'Can child classes use __slots__ if it is not defined in parent class?: \nA. Yes \nB. No ': "B",
}


def selecting_quiz():
    selected_dictionary = None
    while True:
        if selected_dictionary == "python1":
            return python1_quiz
        elif selected_dictionary == "python2":
            return python2_quiz
        elif selected_dictionary == "python3":
            return python3_quiz
        elif selected_dictionary == "http":
            return http_quiz
        elif selected_dictionary == "pytest":
            return pytest
        elif selected_dictionary == "oop":
            return oop
        else:
            selected_dictionary = input("Please, input the name of the test you want to take. Currently available: Python1 (basic level), Python2 (indexing, lambda, OOP), Python3 (random, OS), HTTP, OOP: ").lower()


def shuffle_questions():                                                             # Shuffle the questions order
    questions = selecting_quiz()
    list_q = list(questions.items())                                                 # Convert dictionary into a list of tuples [(key, value), (key, value) etc]
    random.shuffle(list_q)                                                           # Shuffle the order of the list items
    questions = dict(list_q)                                                         # Turn the list of tuples back into a dictionary
    return questions


def print_answers(list_var):
    for i in list_var:
        print(i, end=" ")
    return print()


def print_score(points, user_answers_list, right_answers_list):
    score_var = str(round(points/(len(questions))*100))                             # Calculate the % of the right answers. len() calculates num of objects in container
    print(f"Thanks for the game! Your score is {score_var}%. You've answered {points}/{len(questions)} questions right")  # After all items from the dictionary are checked, the score is pronted
    print("Inputted answers: ", end=" ")
    print_answers(user_answers_list)
    print("Expected answers: ", end=" ")
    print_answers(right_answers_list)


print("\n\n###############################################\nHello! This program is made by Vadzim:) I hope you have a nice day!")
print("- Answer the following questions by typing A, B, C or D. \n- You can't return to the previous question, so choose wisely. \n- Inputting 'End' will close the game.\n###############################################\n")

while True:
    points = 0
    user_answers_list = []                                              # Initializing lists var to save input
    right_answers_list = []
    question_number = 1                                                 # Questions number starts from 1
    questions = shuffle_questions()                                     # Start with selecting the dict and shuffling

    for key, value in questions.items():
        answer = input(f"{question_number}. {key} \nMy answer is: ").upper()   # The question (key) is printed and the user has to input the answer

        while answer not in questions.values():                         # If the answer is not defined in dictionary values - the loop will ask for a viable answer
            answer = input("Wrong input, try again: ").upper()

        if answer == 'END':
            print_score(points, user_answers_list, right_answers_list)
            break                                                       # Breaking the the inner loop
        elif answer == value:                                           # Right answer
            print("Right answer!\n------------------------------")
            points += 1
        elif answer != value:                                           # Wrong answer
            print("Wrong answer!\n------------------------------")
        user_answers_list.append(answer)                                # Saving inputted answer
        right_answers_list.append(value)                                # Saving correct answer
        question_number += 1

    else:                                                               # The else part WILL be executed only if the for loop was NOT broken (see the 'END' part which breaks the loop)
        print_score(points, user_answers_list, right_answers_list)
        replay_var = input("Do you want to play again? y/n: ").lower()  # Only Y/y will restart the game
        if replay_var == "y":
            print("Restarting the game...\n")
            continue                                                    # Restarting the game
        else:
            break                                                       # Breaking the the inner loop, exit the game from the restarting part
    break                                                               # Breaking the outer loop, used only in 'End' functionality to exit the while loop
print("Bye!")
