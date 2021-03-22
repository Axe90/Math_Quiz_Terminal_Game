import random

name = input(str("What is your name?:" ))



def sum(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1, num2

def div(num1, num2):
    return num1 / num2

def dif(name = 'zac'):
    if name == 'zac':
        dif = "easy"
        return dif
    elif name == 'dom':
        dif = 'hard'
        return dif

def easy_quiz():
    score = 0
    difficulty = dif(name)
    if difficulty == 'easy':
        print("Welcome to the EASY quiz!")
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        #print("{a} + {b} = ".format(a = a, b = b))
        answer = input("{a} + {b} = ".format(a = a, b = b))
        if answer == str(sum(a, b)):
            score += 1
            print("Correct!")
        else:
            print("Incorrect! the answer is: " + str(sum(a, b)))


print(easy_quiz())
#print(dif(name))
    


