
import random
import os
import sys
import time

from utils import curses
from custom_exceptions import WordListNotAvailable


def get_words_list():
    root = os.path.curdir
    file_name = "words-list.txt"
    path1 = os.path.join(root, file_name)
    path2 = os.path.join(root, "Wordle Game", file_name)
    url = "https://raw.githubusercontent.com/tabatkins/wordle-list/main/words"

    text = ""

    if os.path.exists(path1):
        with open(path1, "r") as file:
            text = file.read()
    elif os.path.exists(path2):
        with open(path2, "r") as file:
            text = file.read()
    else:
        import requests
        req_ob = requests.get(url)
        if req_ob.status_code == 200:
            text = req_ob.text

    words = text.splitlines()
    if not words:
        raise WordListNotAvailable()
    return words


def game(window):
    from colour_curses import W, RBU, RU, GU, B, Y, YU

    question_word = random.choice(get_words_list()).upper()
    length = len(question_word)
    level = {
        "easy" : 21,
        "medium" : 10,
        "hard" : 6
    }
    difficulty = [20, 9, 5]
    text_menu = """\rChoose your difficulty:
    \r      1. Easy
    \r      2. Medium
    \r      3. Hard
    \r
    \rYour Choice [1-3]: """

    window.nodelay(True)
    key = ""        # For Recording Key Strokes
    choice = -1

    window.clear()
    window.addstr(text_menu, W)
    print("Starting Game...", end= "\n\r")
    # time.sleep(1)

    while True:
        try:
            key = window.getkey()
            window.clear()
            window.addstr(text_menu, W)
            window.addstr(str(key))

            choice = str(key)
            if choice in {'1', '2', '3'}:
                choice = int(choice)
                time.sleep(0.5)
                break
            else:
                window.addstr("\n\rPlease enter a number from 1 to 3...", RBU)
        except Exception as e:
            pass

    choice = int(str(key))
    tries = difficulty[choice - 1]
    window.clear()
    window.addstr(f"You have {tries + 1} tries to guess the word.\n\rGood Luck!!\n\r\n\n", Y)


    while tries:
        chars = 0
        answer = ["_" for i in range(length)]
        # window.addstr(''.join(answer))
        # window.addstr(f"\rThe chars length is {chars} and input:{answer}")
        # og_message =
        while True:
            try:
                window.addstr(f"\rThe chars length is {chars} and input:{' '.join(answer)}", B)
                key = window.getkey()

                if key in ('KEY_BACKSPACE', '\b', '\x7f'):
                    if chars > 0:
                        chars -= 1
                        answer[chars] = "_"
                    continue

                if key == os.linesep:
                    if chars < length:
                        print("\a", end= "")
                        continue
                    else:
                        break

                if chars < length:
                    answer[chars] = str(key).upper()
                    chars += 1


                # window.clear()
                # window.addstr(f"\n\rYou have {tries + 1} tries remaining to guess the word.\n\r", W)

            except Exception as e:
                pass

        window.addstr("\r")
        for i in range(length):
            if answer[i] == question_word[i]:
                window.addstr(f"{answer[i]} ", GU)
            elif answer[i] in question_word:
                window.addstr(f"{answer[i]} ", YU)
            else:
                window.addstr(f"{answer[i]} ", RU)

        tries -= 1
        window.addstr("\n\r")





if __name__ == "__main__":
    # game()
    curses.wrapper(game)