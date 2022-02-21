from colorama import init, Fore, Back, Style

init(autoreset=True)

class WordMap:
    def __init__(self) -> None:
        pass
    
    
    @staticmethod
    def printMap(usedWordsArr,answer):
        for i in range(6):
            if i < len(usedWordsArr):
                print("+---+---+---+---+---+")
                print(WordMap.getRowUsedWord(usedWordsArr[i],answer))

            else:
                print("+---+---+---+---+---+")
                print("[  ][  ][  ][  ][  ]")
        print("+---+---+---+---+---+")
    @staticmethod   
    def getRowUsedWord(word,answer):
        """
            only 3 states:
            plomo: letra no en array
            verde: letra en palabra y en posicion correcta
            amarillo: letra en palabra pero no e posicion correcta
        """
        charFormatedList = []
        for i in range(len(word)):
            char = word[i]
            if char in answer:
                if char == answer[i]:
                    charFormatedList.append(Fore.BLACK + Back.GREEN + ' {} '.format(char) + Style.RESET_ALL)
                else:
                    charFormatedList.append(Fore.BLACK + Back.YELLOW + ' {} '.format(char) + Style.RESET_ALL)
            else:
                charFormatedList.append(Fore.BLACK + Back.LIGHTBLACK_EX + ' {} '.format(char) + Style.RESET_ALL)
        return "|" + "|".join(charFormatedList) + "|"

    @staticmethod   
    def getRowSummary(word,answer):
        """
            only 3 states:
            plomo: letra no en array
            verde: letra en palabra y en posicion correcta
            amarillo: letra en palabra pero no e posicion correcta
        """
        charFormatedList = []
        for i in range(len(word)):
            char = word[i]
            if char in answer:
                if char == answer[i]:
                    charFormatedList.append(Fore.GREEN + Back.GREEN + ' Z ' + Style.RESET_ALL)
                else:
                    charFormatedList.append(Fore.YELLOW + Back.YELLOW + ' Z ' + Style.RESET_ALL)
            else:
                charFormatedList.append(Fore.LIGHTBLACK_EX + Back.LIGHTBLACK_EX + ' Z ' + Style.RESET_ALL)
        return " ".join(charFormatedList)

    @staticmethod
    def printMapSummary(usedWordsArr,answer,attemps):
        for i in range(attemps):
            print(WordMap.getRowSummary(usedWordsArr[i],answer))
            print()
        

    