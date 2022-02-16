from termcolor import colored
#print(colored(' hello ', 'white', 'on_red'))
from colorama import init, Fore, Back, Style

init()

class WordMap:
    def __init__(self) -> None:
        pass
    
    
    @staticmethod
    def printMap(usedWordsArr,answer):
        #receive two arrays, one with the green letters and one with the not included letters
        #[j,h,n]
        #[e,z,p,r]
        for i in range(6):
            if i < len(usedWordsArr):
                #print row with words
                print("+---+---+---+---+---+")
                print(WordMap.getRowUsedWord(usedWordsArr[i],answer))

            else:
                print("+---+---+---+---+---+")
                print("[  ][  ][  ][  ][  ]")
                #print row without words
        print("+---+---+---+---+---+")
    @staticmethod   
    def getRowUsedWord(word,answer):
        """
            only 3 states:
            plomo: letra no en array
            verde: letra en palabra y en posicion correcta
            amarillo: letra en palabra pero no e posicion correcta
        """
        #TODO: FORMAT TEXT TO BLACK
        charFormatedList = []
        for i in range(len(word)):
            char = word[i]
            if char in answer:
                if char == answer[i]:
                    #print verde char
                    charFormatedList.append(Fore.BLACK + Back.GREEN + ' {} '.format(char))
                else:
                    #print amarillo char 
                    charFormatedList.append(Fore.BLACK + Back.YELLOW + ' {} '.format(char))
            else:
                #print plomo char
                charFormatedList.append(Fore.BLACK + Back.LIGHTBLACK_EX + ' {} '.format(char))
                #"\033[0;30;47m {}".format(char)
        return "|" + "|".join(charFormatedList) + "|"