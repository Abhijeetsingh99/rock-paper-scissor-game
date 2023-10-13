# rock-paper-scissor-game
I have written a Python code for Rock paper scissors game. Through this code have learned about Python syntax, keywords and libraries.
import random

# Define the options
options = ["rock", "paper", "scissors"]

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif player_choice == "rock":
        return "You win!" if computer_choice == "scissors" else "Computer wins!"
    elif player_choice == "paper":
        return "You win!" if computer_choice == "rock" else "Computer wins!"
    elif player_choice == "scissors":
        return "You win!" if computer_choice == "paper" else "Computer wins!"

# Main game loop
while True:
    # Get the player's choice
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    # Check if the player's choice is valid
    if player_choice not in options:
        print("Invalid choice. Please choose from rock, paper, or scissors.")
        continue

    # Generate a random choice for the computer
    computer_choice = random.choice(options)

    # Display the choices
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine the winner and display the result
    result = determine_winner(player_choice, computer_choice)
    print(result)

    # Ask the player if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
