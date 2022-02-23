from src import transitions
from src.Game import Game
from src import console


# iniciamos juego
transitions.startGame()

# revisamos si el juego ya se jugo hoy
transitions.checkTodayGame()

gameIsRunning = True

while gameIsRunning:
    data = transitions.getData()
    game = Game(data["option"],data["name"])

    while (game.attemps<6):
        game.renderVisuals() # imprime mapa y teclado
        word = console.enterData().upper()
        game.update(word)
        if word == game.answer:
            game.winingState = True
            game.renderVisuals()
            break
    if game.winingState:
        # do something congratulating the player
        transitions.winGame(game.answer)

    else:
        # do something to say end game and ask if he wishes to play again
        game.renderVisuals()
        transitions.loseGame(game.answer)
    
    game.saveData()
    game.renderSummary()
    gameIsRunning = transitions.startNewGame()


