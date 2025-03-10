from random import choice


def rock_paper_scissors():
    while True:
        user_choice = input("Enter rock paper or scissors ").lower()
        computed_choice = choice(['rock', 'paper', 'scissors'])

        if user_choice == computed_choice:
            print("You chose:", user_choice)
            print("COmputer chose:", computed_choice)
            print("It's a tie!")

        elif user_choice == 'rock' and computed_choice == 'paper':
            print("You chose:", user_choice)
            print("Computer chose:", computed_choice)
            print("Computer Wins!")
        
        elif user_choice == 'rock' and computed_choice == 'scissors':
            print("You chose:", user_choice)
            print("Computer chose:", computed_choice)
            print("You win!")
        
        elif user_choice == 'paper' and computed_choice == 'scissors':
            print("You chose:", user_choice)
            print("Computer chose:", computed_choice)
            print("Computer Wins!")
        
        elif user_choice == 'paper' and computed_choice == 'rock':
            print("You chose:", user_choice)
            print("Computer chose:", computed_choice)
            print("You Win!")
        
        elif user_choice == 'rock' and computed_choice == 'paper':
            print("You chose:", user_choice)
            print("Computer chose:", computed_choice)
            print("Computer wins!")
        
        elif user_choice == 'rock' and computed_choice == 'scissors':
            print("You chose:", user_choice)
            print("Computer chose:", computed_choice)
            print("You Win!")
        
        else:
            print("Invalid input!")