from tkinter import Tk, Button, Label
import random

options = ["Rock", "Paper", "Scissors"]

def play(user_choice):
  computer_choice = random.choice(options)
  result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}")
  if user_choice == computer_choice:
    result_label.config(text=result_label.cget("text") + "\nIt's a tie!")
  elif (user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Paper" and computer_choice == "Rock") or (user_choice == "Scissors" and computer_choice == "Paper"):
    result_label.config(text=result_label.cget("text") + "\nYou win!")
  else:
    result_label.config(text=result_label.cget("text") + "\nYou lose!")

root = Tk()
root.title("Rock Paper Scissors")

title_label = Label(root, text="Rock Paper Scissors", font=("Arial", 20))
title_label.pack(pady=20)

def rock_button_click():
  play("Rock")
def paper_button_click():
  play("Paper")
def scissors_button_click():
  play("Scissors")

def reset_game():
  result_label.config(text="")

rock_button = Button(root, text="Rock", command=rock_button_click)
rock_button.pack(pady=10)

paper_button = Button(root, text="Paper", command=paper_button_click)
paper_button.pack(pady=10)

scissors_button = Button(root, text="Scissors", command=scissors_button_click)
scissors_button.pack(pady=10)

reset_button = Button(root, text="Reset Game", command=reset_game)
reset_button.pack(pady=10)

result_label = Label(root)
result_label.pack(pady=20)

root.mainloop()

