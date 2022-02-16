from src import transitions
from src.Game import Game
from src import console

# iniciamos juego
transitions.startGame()

game = Game()
while (game.attemps<6):
    game.renderVisuals() # imprime mapa y teclado
    word = console.enterData().upper()
    game.update(word) # actualiza estados internos cn datos ingresados
    
    if word == game.answer:
        game.winingState = True
        game.renderVisuals()
        break
    #game.saveData()
if game.winingState:
    # do something congraulating the player
    print("##################################")
    print("##################################")
    print("############ GANASTE #############")
    print("##################################")
    print("##################################")
    
else:
    # do something to say end game and ask if he wshes to play again
    print("##################################")
    print("##################################")
    print("############ PERDISTE ############")
    print("##################################")
    print("##################################")


