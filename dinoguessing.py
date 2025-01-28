import json
import random
import dinterface
import sys


def show_file_errors(method):
    def wrapper(self, *args):
        try:
            var = method(self, *args)
        except ModuleNotFoundError:
            dinterface.something_went_wrong(" I can't read the file ",
                                            "with data for the game!")
            sys.exit()
        except FileNotFoundError:
            dinterface.something_went_wrong(" I can't find the file ",
                                            "with data for the game!")
            sys.exit()
        return var

    return wrapper


class GameDataFile:
    def __init__(self, filename):
        self.name = filename

    @show_file_errors
    def load_data(self):
        with open(self.name) as file:
            return json.load(file)

    @show_file_errors
    def save_data(self, data):
        with open(self.name, "w") as file:
            json.dump(data, file, indent=4)


def parse(q):
    q = q.split()
    positive = True
    group1 = {"isn't": "is", "can't": "can"}
    group2 = {
        "has": "have",
        "lives": "live",
        "flies": "fly"
    }
    if q[0] in group1.values():
        if q[1] == "not":
            positive = False
            del q[1]
        q[0] = f"{q[0].capitalize()} it"
    elif q[0] in group1:
        q[0] = f"{group1[q[0]].capitalize()} it"
        positive = False
    elif q[0] in group2:
        q[0] = f"Does it {group2[q[0]]}"
    elif q[0:2] == ["does", "not"]:
        positive = False
        del q[0]
        del q[0]
        q[0] = f"Does it {q[0]}"
    elif q[0] == "doesn't":
        positive = False
        del q[0]
        q[0] = f"Does it {q[0]}"
    else:
        q[0] = f"Is it true that it {q[0]}"
    return " ".join(q), positive


def get_yes_no(question, default=None, **alternatives):
    while True:
        ans = input(question)
        if ans.lower().startswith("y"):
            return True
        if ans.lower().startswith("ok"):
            return True
        if ans.lower().startswith("n"):
            return False
        if ans in alternatives:
            return ans
        if default is not None:
            return default


class Game:
    def __init__(self, filename):
        self.file = GameDataFile(filename)
        self.animals = self.file.load_data()
        self.index = 0
        self.yes = None
        self.guessed = False
        self.guess = None
        self.scoreboard = [0, 0]

    def ask_question(self):
        next_guess = None
        ans = get_yes_no(f"{self.animals[self.index]['question']}? ", edit=True)
        if ans == "edit":
            q = input("Input the changed question text:\n").strip('? ')
            self.animals[self.index]["question"] = q
            self.file.save_data(self.animals)
            return None
        elif ans:
            self.yes = "yes"
        else:
            self.yes = "no"
        next_guess = self.animals[self.index][self.yes]
        if isinstance(next_guess, int):
            # Next guess is an id of the next question
            self.index = next_guess
        elif isinstance(next_guess, str):
            # Next guess is the name of a creature
            self.guessed = True
            self.guess = next_guess
        elif next_guess is None:
            # There is no next guess
            self.guessed = True

    def have_no_guess(self):
        dinterface.give_up()
        self.scoreboard[1] += 1
        animal = input("It is a")
        question = input(f"Tell me something about it.\nIt ")
        question, pos = parse(question)
        self.animals[self.index][self.yes] = len(self.animals)
        if pos:
            self.animals.append({
                "question": question,
                "yes": animal,
                "no": None,
            })
        else:
            self.animals.append({
                "question": question,
                "yes": None,
                "no": animal,
            })
        self.file.save_data(self.animals)


    def make_guess(self):
        if get_yes_no(f"Is it a{self.guess}? "):
            dinterface.i_win()
            self.scoreboard[0] += 1
        else:
            dinterface.give_up()
            self.scoreboard[1] += 1
            animal = input("It is a")
            question = input(f"How is it different from a{self.guess}?\nIt ")
            question, pos = parse(question)
            self.animals[self.index][self.yes] = len(self.animals)
            if pos:
                self.animals.append({
                    "question": question,
                    "yes": animal,
                    "no": self.guess,
                })
            else:
                self.animals.append({
                    "question": question,
                    "yes": self.guess,
                    "no": animal,
                })
            self.file.save_data(self.animals)

    def main(self):
        print("D I N O G U E S S I N G")
        dinterface.hello(" Let's play a quick  ", "    guessing game?")
        input()
        while True:
            input("Think of a creature and press Enter: ")
            while not self.guessed:
                self.ask_question()
            if self.guess is None:
                self.have_no_guess()
            else:
                self.make_guess()
            self.index = 0
            self.yes = None
            self.guessed = False
            self.guess = None
            if not get_yes_no("Play again? (y/N): ", default=False):
                break
            print()
        dinterface.print_scoreboard(self.scoreboard, "I won   ", "I lost  ")


Game("dinoguessing.json").main()
