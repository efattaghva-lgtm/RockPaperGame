import tkinter as tk
import random

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x450")
root.resizable(False, False)

# Variables
choices = ["Rock", "Paper", "Scissors"]
player_score = 0
computer_score = 0

# Functions
def play(player_choice):
    global player_score, computer_score
    
    computer_choice = random.choice(choices)
    
    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        player_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1
    
    result_label.config(
        text=f"You chose: {player_choice}\nComputer chose: {computer_choice}\n\n{result}"
    )
    score_label.config(
        text=f"Player Score: {player_score}    Computer Score: {computer_score}"
    )

def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    result_label.config(text="Make your move!")
    score_label.config(text="Player Score: 0    Computer Score: 0")

# Title
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"))
title_label.pack(pady=20)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="Rock", width=10, height=2,
                     command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", width=10, height=2,
                      command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, height=2,
                         command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Result Label
result_label = tk.Label(root, text="Make your move!", font=("Arial", 12))
result_label.pack(pady=20)

# Score Label
score_label = tk.Label(root, text="Player Score: 0    Computer Score: 0",
                      font=("Arial", 12, "bold"))
score_label.pack(pady=10)

# Reset Button
reset_btn = tk.Button(root, text="Reset Game", width=15, command=reset_game)
reset_btn.pack(pady=20)

# Run app
root.mainloop()
