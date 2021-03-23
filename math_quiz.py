import random

name = input(str("What is your name?: " ))
dif_in = input("Type 'e' for easy: ")



def sum_easy():
    a = random.randint(0, 10)
    b = random.randint(0, 5)
    answer = a + b
    response = input("{a} + {b} = ".format(a = a, b = b))
    if response == str(answer):
        score = 1
        print("Correct!")
    else:
        score = 0
        print("Incorrect! the answer is: " + str(answer))
    return score

def sub_easy():
    a = random.randint(5, 10)
    b = random.randint(0, 5)
    answer = a - b
    response = input("{a} - {b} = ".format(a = a, b = b))
    if response == str(answer):
        score = 1
        print("Correct!")
    else:
        score = 0
        print("Incorrect! the answer is: " + str(answer))
    return score  

def mult(num1, num2):
    return num1, num2

def div(num1, num2):
    return num1 / num2

def dif(difficulty):
    if difficulty == 'e':
        dif_set = "easy"
        return dif_set
    elif difficulty == 'h':
        dif_set = 'hard'
        return dif_set

def easy_quiz():
    score = 0
    difficulty = dif(dif_in)
    if difficulty == 'easy':
        print("Welcome {0} to the EASY quiz!".format(name))
        score += sum_easy()
        score += sum_easy()
        score += sub_easy()
        print("You finished the quiz with a score of " + str(score))  


print(easy_quiz())
#print(dif(name))
 


