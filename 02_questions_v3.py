import random

score = 0
score = int(score)

print("""What is the Square Root of 100?
a.  11
b.  10
c.  5
d.  14.14""")

answer1 = "b"
response1 = input("Your answer is: ")

if response1 != answer1:
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response1 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")

print("""5 x 7 =?
a. 35 
b. 30 
c. 75 
d. 10""")

answer2 = "a"
response2 = input("Your answer is:")

if response2 != answer2:
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response2 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")

print("""8 x (9 + 3) =?
a.  98
b.  108
c.  106
d.  96""")

answer3 = "d"
response3 = input("Your answer is:")

if response3 != answer3:
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response3 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")

print("""76 - 42
a. 34
b. 32
c. 44
d. 30""")

answer4 = "a"
response4 = input("Your answer is:")

if response4 != answer4:
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response4 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")

print(""" The Hypotenuse times sin(𝛳) = the length of the opposite
a. False
b. True""")

answer5 = "b"
response5 = input("Your answer is:")

if response5 != answer5:
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response5 + " is correct!")
    score = score + 1

print("Rapid Questions")

question = input("You will be asked 5 randoms questions in quick succession.\nReady?")


def yes_no(question):
    valid = False
    while not valid:
        response = input(question).strip().lower()

        if response == "y" or response == "yes":
            response = "yes"
            return response
        else:
            print("Please answer yes or no")


def checker(ans, correct_ans):
    correct = False
    if ans == correct_ans:
        print("Well done!")
        correct = True
    else:
        print("Incorrect")
    print()
    return correct


def add(num_1, num_2):
    while True:
        try:
            response = int(input("{} + {} = ".format(num_1, num_2)))
            print()
            return response
        except ValueError:
            print("Enter a whole number please")


def multi(num_1, num_2):
    while True:
        try:
            response = int(input("{} x {} = ".format(num_1, num_2)))
            print()
            return response
        except ValueError:
            print("Enter a whole number please")


def minus(num_1, num_2):
    while True:
        try:
            response = int(input("{} - {} = ".format(num_1, num_2)))
            print()
            return response
        except ValueError:
            print("Enter a whole number please")


numbers = []
for i in range(5):

    mode = random.randint(1, 3)

    for item in range(2):
        rng = random.randint(1, 13)
        numbers.append(rng)

    if mode == 1:
        correct_answer = numbers[0] + numbers[1]
        guess = add(numbers[0], numbers[1])
    elif mode == 2:
        correct_answer = numbers[0] * numbers[1]
        guess = multi(numbers[0], numbers[1])
    else:
        correct_answer = numbers[0] - numbers[1]
        guess = minus(numbers[0], numbers[1])

    true = checker(guess, correct_answer)
    if true:
        score += 1
    numbers.clear()
