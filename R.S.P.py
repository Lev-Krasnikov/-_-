import random

print("Rock, Scissors, Paper...")

def try_again():
    R_S_P = ["Rock","Scissors","Paper"]
    computer = random.choice(R_S_P)

    player = input("your choice: ").lower().capitalize()


    if computer == "Rock":
        if player == "Rock":
            print(f"I chose {computer}, you chose {player}\nit's a tie!")
        elif player == "Paper":
            print(f"I chose {computer}, you chose {player}\nYou win!")
        elif player == "Scissors":
            print(f"I chose {computer}, you chose {player}\nI win!")

    elif computer == "Paper":
        if player == "Rock":
            print(f"I chose {computer}, you chose {player}\nI win!")
        elif player == "Paper":
            print(f"I chose {computer}, you chose {player}\nIt's a tie!")
        elif player == "Scissors":
            print(f"I chose {computer}, you chose {player}\nYou win!")


    elif computer == "Scissors":
        if player == "Rock":
            print(f"I chose {computer}, you chose {player}\nYou win!")
        elif player == "Paper":
            print(f"I chose {computer}, you chose {player}\nI win!")
        elif player == "Scissors":
            print(f"I chose {computer}, you chose {player}\nIt's a tie")


    play_again = input("Do you want to play again? yes or no: ").lower().capitalize()
    if play_again == "Yes":
        try_again()
    elif play_again == "No":
        print("Goodbye")

try_again()
