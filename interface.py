# MIT License
# Copyright (c) 2026 mathe man
#
# This source file is licensed under the MIT License.
# You may use, modify, and distribute it freely.


def space(size: int = 1) -> None:
    if size == 1:
        print()
        return

    for i in range(size):
        print()


def get_key() -> str:
    return input()[0]


def choose(options) -> int:
    for i in range(len(options)):
        print(str(i+1) + "] " + options[i])

    print("> ", end="")

    answer = get_key()
    jump = not answer.isdigit()

    while not jump:
        print("Answer is invalide: " + answer)
        print("Retry")
        print("> ", end="")
        answer = get_key()

        # Get out of the while loop when the answer is a digit and in the range of the choices
        if answer.isdigit():
            if int(answer) -1 < len(options):
                jump = True


    return int(answer)

def get_floats(vars):
    answers = []
    for i in range(len(vars)):
        try:
            answer = float(input("<" + vars[i] + "> :"))
            answers.append(answer)

        except ValueError:  # Catch convertion error => answer not float
            print("Incorrect ×")
            i -= 1  # Decrement i to retry

    return answers
