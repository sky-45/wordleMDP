from src import console
from src.WordMap import WordMap
from src.Keyboard import Keyboard

class Game:
    def __init__(self):
        self.answer = "JOHAN" # replace with random word from dictionary
        self.attemps = 0
        self.usedLetters = []
        self.winingState = False
        self.usedWords = []

    def initscreen(self):
        console.clearConsole()
        #atempt = console.enterData()
    def update(self,word):
        self.usedWords.append(word)
        self.updateUsedChars(word)
        #update data
        self.attemps += 1 # actualiza numero de intentos
    def renderVisuals(self):
        console.clearConsole()
        WordMap.printMap(self.usedWords,self.answer)
        Keyboard.printKeyboard(self.usedLetters, self.answer)

    def updateUsedChars(self,word):
        for char in word:
            if char not in self.usedLetters:
                self.usedLetters.append(char)