import random

def random_problem():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 5)
    op = random.choice(['+', '-', '*','/'])
     
    if op == '+':
        problem = f"{num1} + {num2}"
        answer = num1 + num2
    elif op == '-':
        problem = f"{num1} - {num2}"
        answer = num1 - num2
    elif op == '*':
        while num2 == 0 or num1 % num2 != 0
        problem = f"{num1} * {num2}"
        answer = num1 * num2
    elif op == '/':
        while num2 == 0 or num1 % num2 != 0:
        problem = f"{num1} / {num2}"
        answer = num1 / num2

    return problem, answer

def math_quiz():
    score = 0
    total_questions = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(int(total_questions)):
        problem, answer = random_problem()
        print(f"\nQuestion: {problem}")
        user_answer = int(input("Your answer: "))

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if _name_ == "_main_":
    math_quiz()
