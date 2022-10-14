from utils import (
    curses,
    os,
    random,
    time
)
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


def get_word():
    return "ALABAMA"
    question_word = random.choice(get_words_list()).upper()
    return question_word



def choose_n_tries_window(window):
    from colour_curses import W, RBU, RU, GU, B, BU, Y, YU
    level = {
        "easy" : 10,
        "medium" : 8,
        "hard" : 6
    }
    difficulty = [10, 8, 6]
    text_menu = """\rChoose your difficulty:
    \r      1. Easy
    \r      2. Medium
    \r      3. Hard
    \r
    \rYour Choice [1-3]: """

    window.clear()
    window.addstr("\rPlease make sure your terminal is of size 10 lines or more to avoid any errors", RBU)
    window.addstr(text_menu, W)

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
    max_tries = difficulty[choice - 1]

    return max_tries



def game(window, question_word):
    from colour_curses import W, RBU, RU, GU, B, BU, Y, YU


    length = len(question_word)
    correct = 0

    window.nodelay(True)
    window.scrollok(True)
    key = ""        # For Recording Key Strokes

    max_tries = choose_n_tries_window(window)
    tries = 0


    window.clear()

    while tries < max_tries and correct != length:
        window.addstr(0, 0, f"You have {max_tries} tries to guess the word.\n\rGood Luck!!\n\r\n", Y)
        chars = 0
        answer = ["_" for i in range(length)]
        correct = 0

        while True:
            try:
                window.addstr(tries + 3, 0, f"\r({tries + 1}) ENTER WORD:{' '.join(answer)}", B)
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

            except Exception as e:
                # with open("Wordle Game/log.txt", 'w') as file:
                #     file.write(f"This {e} occurred at {tries} tries with key = {str(key)}")
                # time.sleep(0.1)
                if key == curses.KEY_RESIZE:
                    return "Resize Screen To a larger size or reduce font size in terminal."



        window.addstr("\r")
        for i in range(length):
            if answer[i] == question_word[i]:
                window.addstr(f"{answer[i]}", GU)
                window.addstr(" ")
                correct += 1
            elif answer[i] in question_word:
                if question_word.count(answer[i]) > 1:
                    window.addstr(f"{answer[i]}", BU)
                    window.addstr(" ")
                else:
                    window.addstr(f"{answer[i]}", YU)
                    window.addstr(" ")
            else:
                window.addstr(f"{answer[i]}", RU)
                window.addstr(" ")

        tries += 1
        try:
            window.addstr("\n\r")
        except curses.error:
            pass

    window.refresh()
    time.sleep(1)

    return correct == length





if __name__ == "__main__":
    # game()
    from colour import GU, YU, RU, B
    print(B("Starting Game..."), end= "\n\r")
    time.sleep(0.5)


    question_word = get_word()
    win = curses.wrapper(game, question_word)

    if win is True:
        print(GU("Congratulations!! You have guessed it right."))
        print(GU("You Won!!!"))

    elif win is False:
        print(YU(f"The correct answer was {question_word}."))
        print(RU("You lost."))
        print(YU("Keep trying, you will win eventually."))

    else:
        print("There has some error occured while running: ", win)