import random
low = 1
high = 100
guesses = 0
number = random.randint(low, high)
while True:
    guess = int(input(f"Enter a number between {low} - {high}: "))
    guesses += 1
    if guess < number:
        print("Go high.")
    elif guess > number:
        print("Go low.")
    elif guess == number:
        print("YOUR GUESS IS CORRECT!!!")
        break
print(f"This round took you {guesses} guesses to get it right!")