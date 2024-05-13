import tkinter as tk
from tkinter import Label, Button, Frame
import random

class TicTacToe:
    def __init__(self, window, data_loader):
        self.window = window
        self.data_loader = data_loader
        self.window.title("Tic-Tac-Toe")
        self.players = ["X", "O"]
        self.player = random.choice(self.players)
        self.buttons = [[None, None, None],
                        [None, None, None],
                        [None, None, None]]
        self.label = Label(text=f"{self.player} it is your turn", font=('times new roman', 40))
        self.label.pack(side="top")
        self.reset_button = Button(text="Restart", font=('times new roman', 20), command=self.new_game)
        self.reset_button.pack(side="top")
        self.frame = Frame(self.window)
        self.frame.pack()
        self.create_buttons()

    def create_buttons(self):
        for row in range(3):
            for column in range(3):
                self.buttons[row][column] = Button(self.frame, text="", font=('times new roman', 40), width=5, height=2,
                                      command=lambda row=row, column=column: self.next_turn(row, column))
                self.buttons[row][column].grid(row=row, column=column)

    def next_turn(self, row, column):
        if self.buttons[row][column]['text'] == "" and not self.check_winner():
            self.buttons[row][column]['text'] = self.player
            if self.check_winner():
                self.label.config(text=f"{self.player} wins!")
            elif self.empty_spaces():
                self.player = self.players[1] if self.player == self.players[0] else self.players[0]
                self.label.config(text=f"{self.player} it is your turn")
            else:
                self.label.config(text="It's a tie!")

    def check_winner(self):
        # Winning combinations
        win_combinations = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]

        for combination in win_combinations:
            cells = [self.buttons[row][column]['text'] for row, column in combination]
            if all(cell == 'X' for cell in cells) or all(cell == 'O' for cell in cells):
                return True

        return False

    def empty_spaces(self):
        for row in range(3):
            for column in range(3):
                if self.buttons[row][column]['text'] == "":
                    return True
        return False

    def new_game(self):
        for row in range(3):
            for column in range(3):
                self.buttons[row][column].config(text="")
        self.player = random.choice(self.players)
        self.label.config(text=f"{self.player} it is your turn")

class DataLoader:
    def load_data(self):
        try:
            with open("game_settings.txt", "r") as file:
                data = file.read()
            return data
        except FileNotFoundError:
            print("File not found.")
            return None
        except Exception as e:
            print(f"Error loading data: {e}")
            return None

def main():
    window = tk.Tk()
    game = TicTacToe(window, DataLoader())
    window.mainloop()

if __name__ == "__main__":
    main()
