from time import sleep
from random import randint
import sys
import dinterface


class Game:
    def __init__(self):
        self.ps = "O"  # player symbol
        self.ds = "X"  # dino symbol
        self.grid = [[" "] * 3 for x in range(3)]
        self.scoreboard = [0, 0]

    def check_move(self, a1, b1, a2, b2, a3, b3, smb):
        grid = self.grid
        ox = smb + " " + smb * 2 + " "
        if grid[a1][b1] + grid[a2][b2] + grid[a3][b3] in ox:
            if grid[a1][b1] == " ":
                grid[a1][b1] = self.ds
            elif grid[a2][b2] == " ":
                grid[a2][b2] = self.ds
            elif grid[a3][b3] == " ":
                grid[a3][b3] = self.ds
            sys.exit()

    def check_win(self, a1, b1, a2, b2, a3, b3, smb):
        g = self.grid
        if g[a1][b1] == g[a2][b2] == g[a3][b3] == smb:
            sys.exit()

    def is_draw(self):
        draw = True
        for r in range(3):
            if " " in self.grid[r]:
                draw = False
        return draw

    def random_move(self):
        while True:
            row = randint(0, 2)
            el = randint(0, 2)
            if self.grid[row][el] == " ":
                self.grid[row][el] = self.ds
                break

    def go_player(self):
        print("Your turn!")
        while True:
            inp = input()
            if len(inp) != 2:
                print("You should enter a letter and a number!")
            elif not inp[0].isalpha():
                print("The first character should be a letter!")
            elif not inp[1].isdigit():
                print("The second character should be a number!")
            elif inp[0] not in "abc":
                print("First coordinate should be from a to c!")
            elif inp[1] not in "123":
                print("Second coordinate should be from 1 to 3!")
            elif self.grid["abc".find(inp[0])][int(inp[1]) - 1] != " ":
                print("This cell is occupied! Choose another one!")
            else:
                self.grid["abc".find(inp[0])][int(inp[1]) - 1] = self.ps
                break

    def go_dino(self):
        print("Hmm, let me think...")
        sleep(1.5)
        if randint(0, 15) == 10:
            self.random_move()
            return None
        sleep(0.5)
        try:
            for r in range(3):  # rows
                self.check_move(r, 0, r, 1, r, 2, self.ds)
            for c in range(3):  # columns
                self.check_move(0, c, 1, c, 2, c, self.ds)
            # diagonals
            self.check_move(0, 0, 1, 1, 2, 2, self.ds)
            self.check_move(0, 2, 1, 1, 2, 0, self.ds)
            for r in range(3):  # rows
                self.check_move(r, 0, r, 1, r, 2, self.ps)
            for c in range(3):  # columns
                self.check_move(0, c, 1, c, 2, c, self.ps)
            # diagonals
            self.check_move(0, 0, 1, 1, 2, 2, self.ps)
            self.check_move(0, 2, 1, 1, 2, 0, self.ps)
        except SystemExit:
            return None
        self.random_move()

    def print_grid(self):
        g = self.grid
        print()
        print("    1   2   3   ")
        print()
        print("a   {} | {} | {}   ".format(g[0][0], g[0][1], g[0][2]))
        print("   ---+---+---")
        print("b   {} | {} | {}   ".format(g[1][0], g[1][1], g[1][2]))
        print("   ---+---+---")
        print("c   {} | {} | {}   ".format(g[2][0], g[2][1], g[2][2]))
        print()

    def analyse_position(self, smb):
        try:
            for r in range(3):  # rows
                self.check_win(r, 0, r, 1, r, 2, smb)
            for c in range(3):  # columns
                self.check_win(0, c, 1, c, 2, c, smb)
            # diagonals
            self.check_win(0, 0, 1, 1, 2, 2, smb)
            self.check_win(0, 2, 1, 1, 2, 0, smb)
        except SystemExit:
            return "Win"
        if self.is_draw():
            return "Draw"
        return "Play"

    def play(self, dino):

        def go(player):
            if player == dino:
                self.go_dino()
            else:
                self.go_player()

        def win(player):
            if player == dino:
                dinterface.i_win()
                self.scoreboard[1] += 1
            else:
                dinterface.you_win()
                self.scoreboard[0] += 1

        def smb(player):
            if player == dino:
                return self.ds
            return self.ps

        player = 0
        while True:
            go(player)
            self.print_grid()
            situation = self.analyse_position(smb(player))
            if situation == "Win":
                win(player)
                break
            elif situation == "Draw":
                dinterface.draw()
                break
            player = (player + 1) % 2

    def main(self):
        print("D I N O   T I C - T A C - T O E ")
        dinterface.hello(" Let's play a quick  ", " game of Tic-Tac-Toe?")
        input()
        print("I suppose that means yes.")
        print(f"You will be '{self.ps}' and I will be '{self.ds}'")

        play = "y"
        while play == "y":
            self.grid = [[" "] * 3 for x in range(3)]
            dino_turn = randint(0, 1)
            self.print_grid()
            if dino_turn == 0:
                print("I go first!")
            self.play(dino_turn)
            play = input("Play? (y/N): ")
            print()

        dinterface.print_scoreboard(self.scoreboard, "You won ", "I won   ")


Game().main()
