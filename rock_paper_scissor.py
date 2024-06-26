import random

# Function to determine the winner of a single round
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play a single round of rock-paper-scissors
def play_round():
    print("\nWelcome to Rock-Paper-Scissors Game!")
    print("Choose your weapon: rock, paper, or scissors.")
    user_choice = input("Enter your choice: ").lower()
    
    # Validate user input
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Enter your choice: ").lower()
    
    # Generate computer's choice
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    
    # Display choices and result
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(f"Result: {result}")

    return result

# Function to keep track of scores and play multiple rounds
def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1
    
    while True:
        print(f"\n===== Round {round_number} =====")
        result = play_round()
        
        # Update scores
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        
        # Display current score
        print(f"\nCurrent Score - You: {user_score}, Computer: {computer_score}")
        
        # Ask if the user wants to play another round
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing!")
            break
        
        round_number += 1

# Entry point of the program
if __name__ == "__main__":
    play_game()