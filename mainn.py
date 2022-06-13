import random
tutorials = input("Press 'Enter' key to learn how to play this game: ")
print("If the two players choose the same character it’s a tie, and the game repeats")
print("(R)Rock beats (S)Scissors")
print("(P)Paper beats (R)Rock")
print("(S)Scissors beats (P)Paper")


R = "Rock"
P = "Paper"
S = "Scissors"
while True:
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_actions)
    print(f"\nYou chose {player_choice}, computer chose {computer_choice}.\n")

    if player_choice == computer_choice:
        print(f"Both players selected {player_choice}. It's a tie!")
        player_choice = input("Enter a choice (rock, paper, scissors): ")
        computer_choice = random.choice(possible_actions)
        print(f"\nYou chose {player_choice}, computer chose {computer_choice}.\n")
    elif player_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif player_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
