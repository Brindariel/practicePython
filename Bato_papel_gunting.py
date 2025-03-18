import random

def play_rps():
    # List of possible choices
    choices = ["bato", "papel", "gunting"]

    # user's choice
    user_choice = input("Enter 'bato', 'papel', or 'gunting': ").lower()

    # Validation
    if user_choice not in choices:
        print("Invalid input!")
        return
    
    # Generate computer's choice randomly
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the outcome
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "bato" and computer_choice == "gunting") or \
         (user_choice == "papel" and computer_choice == "bato") or \
         (user_choice == "gunting" and computer_choice == "papel"):
        print("You win!")
    else:
        print("You lose!")

# Start the game
play_rps()

# mag tatanong kung gusto pang umulit ni player
while True:
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_rps()
    elif play_again == "no":
        print("Thanks for playing! Goodbye.")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
