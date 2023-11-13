def math_quiz():
    s = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = randint(1, 10)
        n2 = randint(1, 5.5)
        o = choice(['+', '-', '*'])
        problem = f"{n1} {o} {n2}"
        print(f"\nQuestion: {problem}")

        if o == '+': a = n1 + n2
        elif o == '-': a = n1 - n2
        else: a = n1 * n2

        useranswer = int(input("Your answer: "))

        if useranswer == a:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {a}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()