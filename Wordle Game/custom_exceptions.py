
class WordListNotAvailable(Exception):
    def __init__(self, message= None, file_name= "words-list.txt"):
        if message is None:
            message = f"Please create a new \"{file_name}\" inside \"Wordle Game\" folder to collect words for the game."

        self.message = message

    def __str__(self):
        return str(self.message)