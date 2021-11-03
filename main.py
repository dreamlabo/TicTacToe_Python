# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from random import randrange


class Player:
    playerSymbol = ''
    playerName = ''
    wins = 0
    loses = 0
    draws = 0

    def __init__(self, playerSymbol, playerName):
        self.playerSymbol = playerSymbol
        self.playerName = playerName

    def getTotalGamesPlayed(self):
        return self.wins + self.loses + self.draws

    def getWinningPercentage(self):
        if self.getTotalGamesPlayed() == 0:
            return str(int(100 * (self.wins / 1 )))+ '%'  # prevent division by zero

        return str(int(100 * (self.wins / self.getTotalGamesPlayed()))) + '%'


def printBoard(board):
    print()
    for row in range(3):
        for column in range(3):
            print(' ', board[row][column], end='')
            if column < 2:
                print(" ", "|", end='')

        print()
        if row < 2:
            print(" ---", "  ---", "  ---")


def checkForWin(board, player):
    # Check Horizontal and Vertical
    for row in range(3):
        threeRow = 0
        threeColumn = 0
        for column in range(3):
            # Check Horizontal Three In A Row
            if board[row][column] == player.playerSymbol:
                threeRow += 1
                if threeRow == 3:
                    # print("Row")
                    return True

            # Check Vertical Three In A Row
            if board[column][row] == player.playerSymbol:
                threeColumn += 1
                if threeColumn == 3:
                    # print("Column")
                    return True

    # Check Diagonal Left To Right - Down
    threeDiagonal = 0
    for row in range(3):
        if board[row][row] == player.playerSymbol:
            threeDiagonal += 1
            if threeDiagonal == 3:
                # print('Diag1')
                return True

    # Check Diagonal Left To Right - Up
    column = 3
    threeDiagonal = 0
    for row in range(3):
        if board[row][column - 1] == player.playerSymbol:
            threeDiagonal += 1
            column -= 1
            if threeDiagonal == 3:
                # print('Diag2')
                return True

    return False


def getUserInput():
    validInput = False

    while not validInput:
        try:
            y = int(input("\tEnter Row:"))
            x = int(input("\tEnter Column:"))

            if (+0 <= x < 3) and (+0 <= y < 3):
                validInput = True
            else:
                print("Invalid Input! Please enter coordinates again.")
                print("(Coordinates must be 0, 1, 2.)")

        except ValueError:
            validInput = False
            print("Invalid Input! Please enter coordinates again.")

    return y, x


def getPlayerMove(board, player):
    validMove = False
    while not validMove:
        row, column = getUserInput()

        if board[row][column] == " ":
            board[row][column] = player.playerSymbol
            validMove = True
        else:
            print("Space is already Occupied! Please enter a different move.")


def getComputerMove(board, player):
    validMove = False
    while not validMove:
        row = randrange(3)
        column = randrange(3)
        if board[row][column] == " ":
            board[row][column] = player.playerSymbol
            validMove = True


def playerToggle(player, players):
    if player.playerSymbol == "X":
        return players[1]
    return players[0]


def playGame(players):
    # player_one = Player('X')
    # computer = Player('O')
    #
    # # players = [{'player_one': 'X', 'wins': 0, 'loses': 0, 'draws': 0},
    # #            {'computer': 'O', 'wins': 0, 'loses': 0, 'draws': 0}]
    #
    # players = [player_one, computer]

    gameBoard = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    endInDraw = True
    player = players[0]

    # print(player.playerSymbol)

    for i in range(9):
        if player.playerSymbol == "X":
            print("\n\nPlayer moves...")
            getPlayerMove(gameBoard, player)
        else:
            print("\n\nComputer moves...")
            getComputerMove(gameBoard, player)

        printBoard(gameBoard)

        if checkForWin(gameBoard, player):
            # print("Player", player.playerSymbol, "wins")
            endInDraw = False
            if player.playerSymbol == 'X':
                players[0].wins += 1
                players[1].loses += 1
                print('{} wins!'.format(players[0].playerName))
                # print('Computer loses:', players[0].loses)
            else:
                players[1].wins += 1
                players[0].loses += 1
                print('\n{} wins!'.format(players[1].playerName))
            break

        player = playerToggle(player, players)

    if endInDraw:
        print("\nGame ends in a draw")
        for player in players:
            player.draws += 1


def printScoreboard(playersList):
    SPACES = 20

    print()
    print('-' * SPACES, 'Scoreboard', '-' * SPACES)
    print("{:<17} {:<8} {:<9} {:<9} {:>5}".format("Player Name", "Wins", "Loses", "Draws", "Win%"))

    for player in playersList:
        print("{:<10} {:>11} {:>9} {:>9} {:>9}".format(player.playerName,
                                                      player.wins,
                                                      player.loses,
                                                      player.draws,
                                                      player.getWinningPercentage()))


if __name__ == '__main__':

    player_one = Player('X', 'Player One')
    computer = Player('O', 'Computer')

    players = [player_one, computer]

    printScoreboard(players)

    keepPlaying = 1
    while keepPlaying == 1:
        playGame(players)
        printScoreboard(players)
        keepPlaying = int(input("\nPress 1 to keep playing"))
