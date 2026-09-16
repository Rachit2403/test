questions = (("9hrsud"),
             ("iueghsn"),
             ("uoegsnl"),
             ("ergdsd"),
             ("grsd"))
options = (("A. ", "B. ", "C. ", "D. "),
           ("A. ", "B. ", "C. ", "D. "),
           ("A. ", "B. ", "C. ", "D. "),
           ("A. ", "B. ", "C. ", "D. "),
           ("A. ", "B. ", "C. ", "D. "))
answers = ("B", "C", "B", "A", "D")
guesses = []
score = 0
ques_num = 0
for question in questions:
    print("------------------------------")
    print(question)
    for option in options[ques_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[ques_num]:
        score += 1
        print("CORRECT!!!")
    else:
        print("INCORRECT!!!")
        print(f"{answers[ques_num]} is the correct answer.")
    ques_num += 1

print("------------------------------")
print("RESULTS")
print("------------------------------")

print("Answers: ", end = "")
for answer in answers:
    print(answer, end = " ")
print()

print("Guesses: ", end = "")
for guess in guesses:
    print(guess, end = " ")
print()

score = int(score / len(questions) * 100)
print(f"YOUR SCORE IS {score}%")