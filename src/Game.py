import json
from src import console
from src.WordMap import WordMap
from src.Keyboard import Keyboard
from src.external import external
import datetime
import json
from src.external import cosmosDB

class Game:
    def __init__(self,dataSrc,name):
        self.dataSrc = dataSrc
        self.player = name
        #self.answer = "JOHAN" #respuesta para testing
        self.answer = self.getWord()
        self.attemps = 0
        self.usedLetters = []
        self.winingState = False
        self.usedWords = []
        self.attempsArr = []
        self.startTime = datetime.datetime.now().isoformat("T") + "Z"
    def getWord(self):
        while True:
            if self.dataSrc==1: #github
                word = external.getWordsGitHub(1)[0].upper()
            elif self.dataSrc==2: #local
                word = external.getWordsLocalFile(1)[0].upper()
            # can comment form here    
            with open('palabras_por_fecha.json') as json_file:
                data = json.load(json_file)
                usedWords = list(data.values())
            if word not in usedWords:
                with open('palabras_por_fecha.json',"r+") as file:
                    file_data = json.load(file)
                    dateToday = datetime.datetime.today().strftime('%Y-%m-%d')
                    file_data[dateToday] = word
                    file.seek(0)
                    json.dump(file_data, file, indent = 4)
                # to here
                return word


    def update(self,word):
        self.usedWords.append(word)
        self.updateUsedChars(word)
        #update data
        self.attemps += 1 # actualiza numero de intentos
        dateTime = datetime.datetime.now().isoformat("T") + "Z"
        self.attempsArr.append({"number":self.attemps,"word":word,"dateTime":dateTime})
    def renderVisuals(self):
        console.clearConsole()
        WordMap.printMap(self.usedWords,self.answer)
        print()
        Keyboard.printKeyboard(self.usedLetters, self.answer)
        print()

    def updateUsedChars(self,word):
        for char in word:
            if char not in self.usedLetters:
                self.usedLetters.append(char)
    def saveData(self):
        jsonData = {}
        jsonData["dateTime"] = self.startTime
        jsonData["name"] = self.player
        jsonData["answer"] = self.answer
        jsonData["result"] = "win" if self.winingState else "lose"
        jsonData["atempts"] = self.attempsArr
        cosmosDB.insertData(jsonData)
        self.write_json(jsonData)
    def renderSummary(self):
        console.clearConsole()
        print("GAME SUMMARY: ")
        print()
        WordMap.printMapSummary(self.usedWords,self.answer,self.attemps)
        print()
        input("Presione enter para continuar ...")
    def write_json(self,new_data, filename='records.json'):
        with open(filename,'r+') as file:
            file_data = json.load(file)
            file_data[self.startTime] = new_data
            file.seek(0)
            json.dump(file_data, file, indent = 4)
 