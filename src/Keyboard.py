from termcolor import colored
#print(colored(' hello ', 'white', 'on_red'))
from colorama import init, Fore, Back, Style
init(autoreset=True)


class Keyboard:
    row_1_letters = ["Q","W","E","R","T","Y","U","I","O","P"]
    row_2_letters = ["A","S","D","F","G","H","J","K","L","Ñ"]
    row_3_letters = ["Z","X","C","V","B","N","M"]
    #backgrounds: blanco(no descubiertas), plomo(no estan), verde(si estan)

    def __init__(self, keyword) -> None:
        pass

    @staticmethod
    def printKeyboard(usedLetters,answer):
        print("used letters received: ",usedLetters, "aswer received:",answer)
        #print("--- keyboard ---")
        for charsRow in [Keyboard.row_1_letters,Keyboard.row_2_letters,Keyboard.row_3_letters]:
            formatedRow = Keyboard.formatRow(charsRow,answer,usedLetters)
            print(formatedRow)

    @staticmethod
    def formatRow(arrChars,answer,usedLetters):
        newArrFormatedChars = []
        for char in arrChars:
            ## --- charForm = "[ {} ]".format(char)
            if char in usedLetters:
                if char in answer:
                    #print green
                    charForm = Fore.BLACK + Back.GREEN + "[ {} ]".format(char)
                else:
                    #print gray
                    charForm = Fore.BLACK + Back.LIGHTBLACK_EX + "[ {} ]".format(char)
                    
            else:
                #print white
                charForm = Fore.BLACK + Back.WHITE + "[ {} ]".format(char)
            newArrFormatedChars.append(charForm)

        if len(newArrFormatedChars)<10:
            return "       " + "".join(newArrFormatedChars)
        return "".join(newArrFormatedChars)
            

