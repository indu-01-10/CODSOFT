import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return 'user'
    else:
        return 'computer'

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\n--- Rock, Paper, Scissors ---")
        user = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()

        if user == 'quit':
            print("Thanks for playing!")
            break
        if user not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose again.")
            continue

        computer = get_computer_choice()
        print(f"Computer chose: {computer}")

        result = determine_winner(user, computer)
        if result == 'tie':
            print("It's a tie!")
        elif result == 'user':
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1

        print(f"Scores -> You: {user_score}, Computer: {computer_score}")

        play_again = input("Would you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing,we will meet again!")
            break

if __name__ == "__main__":
    play_game()
