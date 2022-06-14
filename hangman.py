
from invalidassignmentexception import InvalidAssignmentException

class Hangman:

    def __init__(self):
        self.word = ""
        self.display = "Lifes: 5 - Word: "
        self.dashes = []
        self.lifes = 5

    def set_word(self,word):
        self.word = word.upper()
        for i in range(len(self.word)):
            self.dashes.append("_ ")


    def show(self):
        word_dashes = "".join(self.dashes)
        self.display += word_dashes
        return self.display


    def assign(self,letter):
        posicion = 0
        letter_in_word = 0
        for j in self.word:
            if j == letter.upper():
                self.dashes[posicion] = letter + " " 
                letter_in_word += 1
            posicion += 1
        if letter_in_word == 0:
            self.lifes -= 1
            raise InvalidAssignmentException
        
    def winner(self):
        input_word = "".join(self.dashes)
        input_word = input_word.replace(" ", "")
        input_word = input_word.upper()
        if input_word == self.word and self.lifes > 0:
            return True
        else:
            return False

    def play(self):
        while self.lifes >0:
            try:
                self.assign(str(input("Ingrese una letra")))
                if self.winner():
                    return "Ganaste"
            except InvalidAssignmentException:
                pass
        return "Perdiste"
