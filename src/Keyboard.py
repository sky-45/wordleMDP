from termcolor import colored
from colorama import init, Fore, Back, Style

init(autoreset=True)


class Keyboard:
    row_1_letters = ["Q","W","E","R","T","Y","U","I","O","P"]
    row_2_letters = ["A","S","D","F","G","H","J","K","L","Ñ"]
    row_3_letters = ["Z","X","C","V","B","N","M"]

    def __init__(self, keyword) -> None:
        pass

    @staticmethod
    def printKeyboard(usedLetters,answer):
        for charsRow in [Keyboard.row_1_letters,Keyboard.row_2_letters,Keyboard.row_3_letters]:
            formatedRow = Keyboard.formatRow(charsRow,answer,usedLetters)
            print(formatedRow)

    @staticmethod
    def formatRow(arrChars,answer,usedLetters):
        newArrFormatedChars = []
        for char in arrChars:
            if char in usedLetters:
                if char in answer:
                    charForm = Fore.BLACK + Back.GREEN + "[ {} ]".format(char)
                else:
                    charForm = Fore.BLACK + Back.LIGHTBLACK_EX + "[ {} ]".format(char)
            else:
                charForm = Fore.BLACK + Back.WHITE + "[ {} ]".format(char)
            newArrFormatedChars.append(charForm)

        if len(newArrFormatedChars)<10:
            return "       " + "".join(newArrFormatedChars)
        return "".join(newArrFormatedChars)
            

