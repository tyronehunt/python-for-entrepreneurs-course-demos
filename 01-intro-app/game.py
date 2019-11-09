import os
import random
import time
import colorama

import sys


class Game:
    def __init__(self):
        self.history = []
        self.plays = [
            (colorama.Fore.RED + 'Red', 'r'),
            (colorama.Fore.YELLOW + 'Yellow', 'y'),
            (colorama.Fore.GREEN + 'Green', 'g'),
            (colorama.Fore.CYAN + 'Blue', 'b')
        ]

    def show_level(self):
        self.clear()
        for h in self.history:
            print(h[0], end='  ')
            # flush output (as not using an inline print)
            sys.stdout.flush()
            time.sleep(1)

        self.clear()

    def add_move(self):
        """

        :rtype:
        """
        self.history.append(random.choice(self.plays))

    # noinspection PyMethodMayBeStatic
    def test_player(self) -> object:
        print(colorama.Fore.WHITE + "{} moves:".format(len(self.history)))
        for t, v in self.history:
            guess = input("Next [r,g,b,y]: ")
            if guess != v:
                return False

        return True

    # noinspection PyMethodMayBeStatic
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')