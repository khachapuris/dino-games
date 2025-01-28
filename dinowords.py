import pickle
import random
import sys
import dinterface


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
        with open(self.name, "r") as file:
            return [line.rstrip() for line in file]

    @show_file_errors
    def save_data(self, data):
        with open(self.name, "w") as file:
            file.write("\n".join(data))


class Word:
    def __init__(self, word):
        self.word = word
        self.ls = list("-" * len(word))
        self.memory = set()
        self.hearts = 8

    def try_letter(self, letter):
        if len(letter) != 1:
            print("Please, input a single letter.")
        elif not (letter.islower() and letter.isascii()):
            print("Please, enter a lowercase English letter.")
        elif letter in self.memory:
            print("You've already tried this letter.")
        elif letter in self.word:
            for letter_num in range(len(self.word)):
                curr = self.word[letter_num]
                if curr == letter:
                    self.ls[letter_num] = curr
            self.memory.add(letter)
        else:
            self.hearts -= 1
            self.memory.add(letter)
            print("That letter doesn't appear in the word.")

    def is_revealed(self):
        return "-" not in self.ls

    def is_playing(self):
        return self.hearts > 0 and not self.is_revealed()

    def show(self):
        print()
        print("^" * self.hearts + " " * (9 - self.hearts) + "".join(self.ls))


class Game:
    def __init__(self, filename):
        self.file = GameDataFile(filename)
        self.playwords = self.file.load_data()
        random.shuffle(self.playwords)
        self.scoreboard = [0, 0]
        self.rules = ["I will choose a word.",
                      "You have to guess it ",
                      "by inputting letters.",
                      " If  you  miss,  you ",
                      " loose a heart. You  ",
                      " have only 8 hearts. ",
                      "      Good luck!     "]
        self.word = None

    @staticmethod
    def plural(msg_before, num, unit, msg_after):
        if num % 10 == 1 and num != 11:
            print(msg_before, num, unit, msg_after)
        else:
            print(msg_before, num, unit + "s", msg_after)
        print()

    def add_one_word(self, wordlist):
        print()
        print("Please add a word to the word list before playing:")
        while True:
            word = input("> ")
            if word in wordlist:
                print(f"The word {word} is already in the list.")
            elif 5 <= len(word) <= 12 and word.isalpha():
                wordlist.append(word)
                break
            else:
                print("The word should have 5-12 English letters.")
        self.file.save_data(wordlist)
        print("Word added!")
        print("Thank you very much!")
        print()
        return wordlist

    def edit_wordlist(self, wordlist):
        print("Use 'add <word>' and 'del <word>', press Enter to exit.")
        added, deleted = 0, 0
        while True:
            inp = input("> ").split()
            if len(inp) != 2:
                break
            key, word = inp
            if key == "add":
                if word in wordlist:
                    print(f"The word {word} is already in the list.")
                elif 5 <= len(word) <= 12 and word.isalpha():
                    wordlist.append(word)
                    added += 1
                else:
                    print("The word should have 5-12 English letters.")
            elif key == "del":
                if word in wordlist:
                    wordlist.remove(word)
                    deleted += 1
                else:
                    print("There is no such word in the list.")
        print(f"Total: added {added}, deleted {deleted}")

    def play(self):
        if not self.playwords:
            allwords = self.file.load_data()
            if not allwords:
                dinterface.something_went_wrong("  I'm out of words! ",
                                                ' Type "add" or "exit"')
                answer = input()
                if answer == "exit":
                    sys.exit()
                self.edit_wordlist()
            else:
                dinterface.something_went_wrong("     I'm out of     ",
                                                "  different words!")
                print('Type "play" to guess words you have already tried;')
                print('Type "add" to add other words to the word list;')
                print('Type "exit" to quit:')
                answer = input()
                if answer == "exit":
                    sys.exit()
                elif answer == "add":
                    self.edit_wordlist()
                else:
                    self.playwords = random.shuffle(allwords)

        self.word = Word(self.playwords[0])
        del self.playwords[0]

        while self.word.is_playing():
            self.word.show()
            input_letter = input("Input a letter: ")
            self.word.try_letter(input_letter)

        if self.word.is_revealed():
            dinterface.you_win(" You guessed the word ",
                               f"       {self.word.word}!")
            self.scoreboard[0] += 1
        else:
            dinterface.you_lost()
            self.scoreboard[1] += 1

    def main(self):
        print("D I N O W O R D S")
        dinterface.hello('Type "play" or "edit"', "")
        global_action = input()

        if global_action == "edit":
            self.edit_wordlist(self.playwords)

        elif global_action == "play":
            action = "y"
            if self.playwords and len(self.playwords) < 100:
                self.add_one_word(self.playwords)
            dinterface.the_rules(self.rules)
            print("Start playing?")
            input()
            print("I suppose that means yes.")
            try:
                while action == "y":
                    self.play()
                    action = input("Play? (y/N): ")
            finally:
                dinterface.print_scoreboard(self.scoreboard,
                                            "You won ", "You lost")


Game("dinowords.txt").main()
