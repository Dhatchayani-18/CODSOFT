import random

print("Welcome to Rock, Paper, Scissors!\n")
player1_wins = 0
player2_wins = 0
while True:
    player1 = input("Enter a choice (rock, paper, scissors): ")
    choices = ["rock", "paper", "scissors"]
    player2 = random.choice(choices)
    print(f"\nYou chose {player1}, computer chose {player2}.")
    if player1 == player2:
        print(f"Both players selected {player1}. It is a tie!")
    elif player1 == "rock":
        if player2 == "scissors":
            print("Rock smashes scissors. You win!")
            player1_wins += 1
        else:
            print("Paper covers rock. You lose.")
            player2_wins += 1
    elif player1 == "paper":
        if player2 == "rock":
            print("Paper covers rock. You win!")
            player1_wins += 1
        else:
            print("Scissors cuts paper. You lose.")
            player2_wins += 1
    elif player1 == "scissors":
        if player2 == "paper":
            print("Scissors cuts paper. You win!")
            player1_wins += 1
        else:
            print("Rock smashes scissors. You lose.")
            player2_wins += 1
    print("You have " + str(player1_wins) + " wins")
    print("The computer has " + str(player2_wins) + " wins")
    repeat = input("\nPlay again? (yes/no): ")
    if repeat.lower() != "yes":
        print("Thank you! Have Fun!")
        break
