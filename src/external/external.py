import requests
import random

############################################
# Functions to handle the words avaliable for the game

# fecth data from repo

def getRandomWord(src= "github"):
    if src == "github":
        return getWordsGitHub(1)
    else:
        return getWordsLocalFile(1)

def getWordsGitHub(n):
    """
        This function retrieves 365 random words from 
        the github repo and clean the words
    """
    urlWords = "https://raw.githubusercontent.com/javierarce/palabras/master/listado-general.txt"
    r = requests.get(urlWords)
    words = r.text.split("\n")
    words = [cleanWord(word) for word in words if len(word)==5]
    words_5 = random.sample(words, 365)
    return random.sample(words_5,n)
def getDictionary():
    urlWords = "https://raw.githubusercontent.com/javierarce/palabras/master/listado-general.txt"
    r = requests.get(urlWords)
    words = r.text.split("\n")
    words = [cleanWord(word) for word in words if len(word)==5]
    return words
def getWordsLocalFile(n):
    """
        This function retrieves 365 random words from 
        the .TXT file in root
    """
    file1 = open("palabras5.txt","r+") 
    lines = file1.readlines()
    words_5 = [line[:-1] for line in lines]
    file1.close()
    return random.sample(words_5,n)

#-----helpers
def cleanWord(word):
    """
        eliminamos tildes de una palabra
    """
    incorrectWords = {
        "á":"a",
        "é":"e",
        "í":"i",
        "ó":"o",
        "ú":"u",
    }
    newWord = word + ""
    for vocalTilde in incorrectWords:
        if vocalTilde in word:
            newWord = newWord.replace(vocalTilde,incorrectWords[vocalTilde])
    return newWord
def saveWordsFile():
    """
        This function saves the 365 random words to a text File
    """
    words = getWordsGitHub(365)
    file1 = open("palabras5.txt","w")
    words_newline = [k+"\n" for k in words]
    file1.writelines(words_newline)
    file1.close()
