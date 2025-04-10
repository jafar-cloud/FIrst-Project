class Flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return (f"Word: {self.word}, Meaning: {self.meaning}")


while True:
    word = input("Enter the word: ")
    definition = input('enter it\'s def: ')

    ur_flashcard = Flashcard(word, definition)


    flash = []

    flash.append(ur_flashcard)

    continue_or_not = input("Do you want to continue? (y/n)")

    if continue_or_not.lower() == 'n':
        break


i = 0
while i < len(flash):
    print(flash[i])
    i += 1

