import random


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
