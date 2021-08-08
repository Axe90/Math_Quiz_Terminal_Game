import random

name = input(str("What is your name?: " ))
while name == "":
    name = input(str("What is your name?: " ))
dif_in = input("Type 'e' for EASY or 'm' for MEDIUM or 'h' for HARD: ")



def sum_easy():
    a = random.randint(0, 20)
    b = random.randint(0, 10)
    answer = a + b
    response = input("{a} + {b} = ".format(a = a, b = b))
    if response == str(answer):
        score = 1
        print("Correct!"'\n')
    else:
        score = 0
        print("Incorrect! the answer is: " + str(answer)+'\n')
    return score

def sub_easy():
    a = random.randint(5, 20)
    b = random.randint(0, 5)
    answer = a - b
    response = input("{a} - {b} = ".format(a = a, b = b))
    if response == str(answer):
        score = 1
        print("Correct!"'\n')
    else:
        score = 0
        print("Incorrect! the answer is: " + str(answer)+'\n')
    return score  

def sum_medium():
    a = random.randint(0, 20)
    b = random.randint(10, 20)
    answer = a + b
    response = input("{a} + {b} = ".format(a = a, b = b))
    if response == str(answer):
        score = 1
        print("Correct!"'\n')
    else:
        score = 0
        print("Incorrect! the answer is: " + str(answer)+'\n')
    return score   

def sub_medium():
    a = random.randint(10, 20)
    b = random.randint(0, 10)
    answer = a - b
    response = input("{a} - {b} = ".format(a = a, b = b))
    if response == str(answer):
        score = 1
        print("Correct!"'\n')
    else:
        score = 0
        print("Incorrect! the answer is: " + str(answer)+'\n')
    return score  

def sub_hard():
    a = random.randint(50, 100)
    b = random.randint(10, 80)
    answer = a - b
    response = input("{a} - {b} = ".format(a = a, b = b))
    if response == str(answer):
        score = 1
        print("Correct!"'\n')
    else:
        score = 0
        print("Incorrect! the answer is: " + str(answer)+'\n')
    return score  

def sum_hard():
    a = random.randint(20, 500)
    b = random.randint(20, 500)
    answer = a + b
    response = input("{a} + {b} = ".format(a = a, b = b))
    if response == str(answer):
        score = 1
        print("Correct!"'\n')
    else:
        score = 0
        print("Incorrect! the answer is: " + str(answer)+'\n')
    return score

def mult_hard():
    a = random.randint(0, 5)
    b = random.randint(0, 5)
    answer = a * b
    response = input("{a} x {b} = ".format(a = a, b = b))
    if response == str(answer):
        score = 1
        print("Correct!"'\n')
    else:
        score = 0
        print("Incorrect! the answer is: " + str(answer)+'\n')
    return score

def dif(difficulty):
    if difficulty == 'e':
        dif_set = "easy"
        return dif_set
    elif difficulty == 'm':
        dif_set = 'medium'
        return dif_set
    elif difficulty == 'h':
        dif_set = 'hard'
        return dif_set
    elif difficulty != 'e' or difficulty != 'm' or difficulty != 'h':
        return dif(input("TRY AGAIN Type 'e' for EASY or 'm' for MEDIUM or 'h' for HARD: ")) 


def quiz():
    score = 0
    difficulty = dif(dif_in)    
    if difficulty == 'easy':
        print('\n'+"Welcome {0} to the EASY quiz!".format(name)+'\n')
        score += sum_easy()
        score += sum_easy()
        score += sub_easy()
        score += sum_easy()
        score += sum_easy()
        print("You finished the quiz with a score of " + str(score) + " out of 5 \n") 
        return "Thank you for playing\n" 
    elif difficulty == 'medium':
        print('\n'+"Welcome {0} to the MEDIUM quiz!".format(name)+'\n')
        score += sum_medium()
        score += sum_medium()
        score += sub_medium()
        score += sub_medium()
        score += sum_medium()
        print("You finished the quiz with a score of " + str(score) + " out of 5 \n") 
        return "Thank you for playing\n"
    elif difficulty == 'hard':
        print('\n'+"Welcome {0} to the HARD quiz!".format(name)+'\n')
        score += mult_hard()
        score += sub_hard()
        score += mult_hard()
        score += sum_hard()
        score += mult_hard()
        print("You finished the quiz with a score of " + str(score) + " out of 5 \n") 
        return "Thank you for playing\n" 


print(quiz())

 


