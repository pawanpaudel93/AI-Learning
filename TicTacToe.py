# Gardai xu vako xaina
import random


class TicTacToe:
    def __init__(self):
        """initialise a empty board"""
        self.board = [
            " ", " ", " ",
            " ", " ", " ",
            " ", " ", " "
        ]

    def showBoard(self):
        print("""
        {} | {} | {}
        ----------
        {} | {} | {}
        ----------
        {} | {} | {}
        """.format(*self.board))

    def clearBoard(self):
        self.board = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]

    def whoWon(self):
        if self.checkWin() == 'X':
            return 'X'
        elif self.checkWin() == 'O':
            return 'O'
        elif self.gameOver():
            return 'Nobody'

    def get_availableMoves(self):
        """Return empty spaces on the board"""
        moves = []
        for i in range(0, len(self.board)):
            if self.board[i] == " ":
                moves.append(i)
        return moves

    def get_moves(self, player):
        """Get all moves made by a given player"""
        moves = []
        for i in range(0, len(self.board)-1):
            if self.board == player:
                moves.append(i)
        return moves

    def make_move(self, player, position):
        self.board[position] = player

    def checkWin(self):
        winning_combos = ([0, 1, 2], [3, 4, 5], [6, 7, 8],
                          [0, 3, 6], [1, 4, 7], [2, 5, 8],
                          [0, 4, 8], [2, 4, 6])
        for player in ("X", "O"):
            positions = self.get_moves(player)
            for combo in winning_combos:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player

    def gameOver(self):
        if self.checkWin():
            return True
        for i in self.board:
            if i == " ":
                return False
        return True

    def minMax(self, node, depth, player):
        if depth == 0 or node.gameOver():
            if node.checkWin() == "X":
                return 0
            elif node.checkWin() == "O":
                return 100
            else:
                return 50

        if player == "O":
            bestValue = 0
            for move in node.get_availableMoves():
                node.make_move(player, move)
                moveValue = self.minMax(node, depth-1, changePlayer(player))
                node.make_move(" ", move)
                bestValue = max(bestValue, moveValue)
            return bestValue

        if player == "X":
            bestValue = 100
            for move in node.get_availableMoves():
                node.make_move(player, move)
                moveValue = self.minMax(node, depth-1, changePlayer(player))
                node.make_move(" ", move)
                bestValue = min(bestValue, moveValue)
            return bestValue


def changePlayer(player):
    if player == "X":
        return "O"
    else:
        return "X"


def make_best_move(board: TicTacToe, depth, player):
    neutralValue = 50
    choices =[]
    for move in board.get_availableMoves():
        board.make_move(player, move)
        moveValue = board.minMax(board, depth-1, changePlayer(player))
        board.make_move(" ", move)

        if moveValue > neutralValue:
            choices = [move]
        elif moveValue == neutralValue:
            choices.append(move)
    print("choices: ", choices)
    if len(choices) > 0:
        return random.choice(choices)
    else:
        return random.choice(board.get_availableMoves())


if __name__ == "__main__":
    game = TicTacToe()
    game.showBoard()

    while not game.gameOver():
        person_move = int(input("You are X: Choose number from number 1-9: "))
        game.make_move("X", person_move-1)
        game.showBoard()

        if game.gameOver():
            break

        print("Computer choosing move...")
        ai_move = make_best_move(game, -1, "O")
        game.make_move("O", ai_move)
        game.showBoard()
    print("Game Over. " + game.whoWon() + " Won")



