import random
secretnum=random.randint(1,20)
print("Im thinking of a num bitween 1 and 20")
for guessestaken in range(1,6):
    print("take a guess")
    guess=int(input("guess: "))
    if guess < secretnum:
        print("ur guess is too low...!")
    elif guess > secretnum:
        print("ur guess is too high")
    else:
        break
if guess == secretnum:
    print("Good job! u guessed my num in" + str(guessestaken) + "guess!")
else:
    print("Nope...! the num i was thinking was" + str(secretnum))
