import random

# Define options for the game
options = ["Rock", "Paper", "Scissors"]

def play_game():
  """
  This function plays a single round of Rock-Paper-Scissors
  """
  # Get user input
  user_choice = input("Choose Rock, Paper, or Scissors: ").capitalize()

  # Check for invalid input
  if user_choice not in options:
    print("Invalid choice. Please choose Rock, Paper, or Scissors.")
    return

  # Get computer's choice
  computer_choice = random.choice(options)

  # Determine winner
  if user_choice == computer_choice:
    print(f"You both chose {user_choice}. It's a tie!")
  elif (user_choice == "Rock" and computer_choice == "Scissors") or \
       (user_choice == "Paper" and computer_choice == "Rock") or \
       (user_choice == "Scissors" and computer_choice == "Paper"):
    print(f"You win! {user_choice} beats {computer_choice}.")
  else:
    print(f"You lose! {computer_choice} beats {user_choice}.")

# Play the game
while True:
  play_game()
  # Ask user if they want to play again
  play_again = input("Play again? (y/n): ").lower()
  if play_again != "y":
    break

print("Thanks for playing!")
