
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("#################################################")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or C): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("Correct Answer")
        return 1
    else:
        print("Wrong Answer!")
        return 0


def display_score(correct_guesses, guesses):
    print("*****************************")
    print("Results")
    print("*****************************")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses / len(questions))*100)
    print("Your final score is: {}%".format(score))


def play_again():
    msg = input("Do you want to play again? (y/n): ")
    msg = msg.upper()

    if msg == "Y":
        return True
    else:
        return False


questions = {
    "Who is the director of the Blue Velvet Movie?: ": "D",
    "which of these Movie is from Krzysztof Kieslowski?: ": "C",
    "Who is the main character of Sons Of Anarchy series?: ": "A",
    "Who has the most Academy Awards?: ": "B"
}


options = [["A. David Fincher", "B. Christopher Nolan", "C. William Smith", "D. David Lynch"],
          ["A. Blue Valentine", "B. On The Water Front", "C. The Double Life Of Veronique", "D. Bitter Moon"],
          ["A. Jackson Teller", "B. Rick white", "C. Arthur Shelbi", "D. Joel"],
          ["A. Marlon Brando", "B. Walt Disney", "C. Daniel Day-Lewis", "D. Al Pacino"]]

if __name__ == "__main__":
    new_game()

while play_again():
    new_game()

print("Thanks for playing!")