import random

questions = {
    "Who, as the UK leader, signed the Munich agreements?:\nA. Chamberlen \nB. Churchill \nC. Daladier" : "A",
    "When the WWII started?:\nA. 1938 \nB. 1939 \nC. 1940": "B",
    "On what city was the second nuclear bomb dropped?:\nA. Tokyo \nB. Hiroshima \nC. Nagasaki": "C",
}
l = list(questions.items())
print(l)
random.shuffle(l)
print(l)
questions = dict(l)

print(questions)

# points = 0
# print("\n\nHello! This program is made by Vadim:) I hope you have a nice day!")
# print("Please answer the following questions by typing A, B or C. You can't return to the previous question, so choose wisely")
# while True:
#     for key, value in questions.items():
#         answer = input(key+"\nMy answer is:   ").capitalize()
        
#         while answer not in questions.values():
#             answer = input("Wrong input, try again: ").capitalize()

#         if answer == value:
#             print("Right answer!")
#             print("------------------------------")
#             points = points + 1
#         elif answer != value:
#             print("Wrong answer!")
#             print("------------------------------")

#     print("Thanks for the game! Your score is {}.". format(points))
#     replay_var = input("Do you want to play again? y/n: ").lower()
#     if replay_var == "y":
#         print("Restarting the game")
#         points = 0
#     else:
#         print("Bye!")
#         break
