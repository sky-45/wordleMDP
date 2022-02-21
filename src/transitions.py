import time
from src import console
def startGame():
    time.sleep(2)
    console.clearConsole()
    print("\t #-------------------------------------------------#")
    time.sleep(0.5)
    print("\t #-------------------------------------------------#")
    time.sleep(0.5)
    print("\t #-------------------------------------------------#")
    time.sleep(0.5)
    print("\t #-------------------------------------------------#")
    time.sleep(0.5)
    print("\t #-------------- BIENVENIDO AL JUEGO --------------#")
    time.sleep(0.5)
    print("\t #------------------- NOT WORDLE ------------------#")
    time.sleep(0.5)
    print("\t #-------------------------------------------------#")
    time.sleep(0.5)
    print("\t #-------------------------------------------------#")
    time.sleep(0.5)
    print("\t #-------------------------------------------------#")
    time.sleep(0.5)
    print("\t #-------------------------------------------------#")
    print()
    print()
    input("\t Presione la tecla ENTER para continuar...")
    time.sleep(1)
def getData():
    console.clearConsole()
    name = input(" Ingrese su nombre: ")
    while(True):
        console.clearConsole()
        print("De donde quiere obtener las palabras: ")
        print("1. Github")
        print("2. LocalFile")
        dataSrcOption = input("Ingrese el numero de su opcion: ")
        #dataSrc = 1
        if dataSrcOption.isdecimal():
            if int(dataSrcOption) in [1,2]:
                return {"name":name,"option":int(dataSrcOption)}
            else:
                print("Solo puede seleccionar la opcion 1 o 2 !!!")
        else:
            print("Solo puede ingresar el numero correspondiente a la opcion !!!")
        
        time.sleep(3)
    
def initialScreen():
    pass
def loseGame(answer):
    time.sleep(5)
    console.clearConsole()
    print()
    print()
    print("\t #-------------------------------------------------#")
    time.sleep(0.5)
    print("\t #-------------------------------------------------#")
    time.sleep(0.5)
    print("\t #-------------------------------------------------#")
    time.sleep(0.5)
    print("\t #------------------- PERDISTE --------------------#")
    time.sleep(0.5)
    print("\t #-------------------------------------------------#")
    time.sleep(0.5)
    print("\t #-------------- RESPUESTA = {} ----------------#".format(answer))
    time.sleep(0.5)
    print("\t #-------------------------------------------------#")
    time.sleep(0.5)
    print("\t #-------------------------------------------------#")
    time.sleep(0.5)
    print("\t #-------------------------------------------------#")
    print()
    print()
    input("\t Presione la tecla ENTER para continuar")

def winGame(answer):
    time.sleep(5)
    console.clearConsole()
    print()
    print()
    print("\t #-------------------------------------------------#")
    time.sleep(0.5)
    print("\t #-------------------------------------------------#")
    time.sleep(0.5)
    print("\t #----------------- FELICIDADES -------------------#")
    time.sleep(0.5)
    print("\t #------------------- GANASTE  --------------------#")
    time.sleep(0.5)
    print("\t #-------------------------------------------------#")
    time.sleep(0.5)
    print("\t #-------------- RESPUESTA = {} ----------------#".format(answer))
    time.sleep(0.5)
    print("\t #-------------------------------------------------#")
    time.sleep(0.5)
    print("\t #-------------------------------------------------#")
    print()
    print()
    input("\t Presione la tecla ENTER para continuar")
    

def startNewGame():
    while True:
        console.clearConsole()
        print("Quisiera jugar un juego nuevo ? ")
        print("1. SI")
        print("2. NO")
        dataSrcOption = input("Ingrese el numero de su opcion: ")
        #dataSrc = 1
        if dataSrcOption.isdecimal():
            if int(dataSrcOption) == 1:
                return True 
            elif int(dataSrcOption) == 2:
                return False 
            else:
                print("Solo puede seleccionar la opcion 1 o 2 !!!")
        else:
            print("Solo puede ingresar el numero correspondiente a la opcion !!!")
        time.sleep(4)
    #print(data)
    option = True
    return option
