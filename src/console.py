import os
import time
from src.external import external
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def enterData():
    while True:
        guess = input("Ingrese su respuesta: ")
        guess = guess.strip() #limpiamos espacios
        wordsAvaliable = external.getDictionary() #podemos comentar esto
        if validateInput(guess) and len(guess)==5 and guess in wordsAvaliable:
            return guess
        else:
            print("Palabra ingresada no valida :C !!!")
            time.sleep(1)

def validateInput(word):
    for char in word:
        if char.isalpha() == False:
            return False
    return True


