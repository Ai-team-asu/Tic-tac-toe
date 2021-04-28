  def alphabeta(self, node):
        val = self.min_val(node, -oo, oo)
        return val

    def max_val(self, node, alpha, beta):
        if self.gameOver():
            b = self.whoWon()
            if b == "O":
                return 1
            elif b == "X":
                return -1
            else:
                return 0
        val = -oo
        for child in self.availableMoves():
            self.makeMove(child, "O")
            val = max(val, self.min_val(node, alpha, beta))
            self.makeMove(child, " ")
            if val >= beta:
                return val
            alpha = max(alpha, val)
        return val

    def min_val(self, node, alpha, beta):
        if self.gameOver():
            b = self.whoWon()
            if b == "O":
                return 1
            elif b == "X":
                return -1
            else:
                return 0
        val = oo
        for child in self.availableMoves():
            self.makeMove(child, "X")
            val = min(val, self.max_val(node, alpha, beta))
            self.makeMove(child, " ")
            if val <= alpha:
                return val
            beta = min(beta, val)
        return val


def changePlayer(player):
    """Returns the opposite player given any player"""
    if player == "X":
        return "O"
    else:
        return "X"


def make_best_move(board, depth, player):
    """
    Controllor function to initialize minimax and keep track of optimal move choices
    board - what board to calculate best move for
    depth - how far down the tree to go
    player - who to calculate best move for (Works ONLY for "O" right now)
    """
    neutralValue = 0
    choices = []
    for move in board.availableMoves():
        board.makeMove(move, player)
        #moveValue = board.minimax(board, depth - 1, changePlayer(player))
        moveValue = board.alphabeta(board)
        board.makeMove(move, " ")

        if moveValue > neutralValue:
            choices = [move]
            break
        elif moveValue == neutralValue:
            choices.append(move)
    print("choices: ", choices)

    if len(choices) > 0:
        return random.choice(choices)
    else:
        return random.choice(board.availableMoves())
