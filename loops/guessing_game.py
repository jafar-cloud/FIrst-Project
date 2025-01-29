import random
computer_guess = random.randint(1,100)
keep_playing = True
guesses = 0
while keep_playing:
    user_guess = int(input("Guess: "))
    guesses += 1

    if guesses >= 10:
        print("You Lost!")
        break

    if user_guess < computer_guess:
        print("Too Low!")
    
    elif user_guess > computer_guess:
        print("Too High!")
    
    else:
        print("Congratulations! You Guessed The Number Right!")
        choice = int(input("1.Play Again 2.Quit"))

        if choice == 2:
            keep_playing = False
        elif choice == 1:
            computer_guess = random.randint(1,100)