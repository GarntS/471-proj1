#! /usr/bin/env python3
# file:     baby_driver.py
# author:   <your_umbc_email_here>
# date:     02/02/2020
# desc:     python3 minmax-ab implementation for use with chess eval functions,
#           CMSC471 project 1.

# imports
import chess
import random
#TODO(y'all): import any new evaluation functions on the line below
from eval_funcs import test_eval, eval_countpieces, eval_weightpieces

# minimax() runs an iteration of minimax-ab with the specified max depth
# @param depth          set to the maximum depth we want to evaluate, decreases
#                       over recursions until it reaches 0 at the bottom of the
#                       tree.
# @param board          the python-chess board object at the root node.
# @param alpha          the alpha value we're using. You can play with this.
# @param beta           the beta value we're using. You can play with this too.
# @param is_maximizing  is the current iteration the maximizing player?
# @param eval_func      the evaluation function used to evaluate the current
#                       position.
# @return               A 2-tuple containing the score of the subtree and its
#                       respective move.
def minimax(depth, board, alpha, beta, is_maximizing, eval_func):
    # end the recursion if this is the maximum depth we want to reach
    if depth == 0:
        if board.result() == "1-0":
            return float("inf", board.peek())
        if board.result() == "0-1":
            return (float("-inf"), board.peek)
        return (-eval_func(board), board.peek())

    # populate the possible moves that can be made from the current board state
    possible_moves = []
    # iterate through the generator because we can only shuffle a list
    for move in board.legal_moves:
        possible_moves.append(move)
    # shuffle the order of the moves
    random.shuffle(possible_moves)

    # if we're the maximizing player
    if is_maximizing:
        # track the current best move. start with the worst move imaginable.
        best_score = float("-inf")
        best_move = None

        # iterate over all available moves
        for x in possible_moves:
            # commit the move to the board state
            move = chess.Move.from_uci(str(x))
            board.push(move)

            # recurse to find the best move
            pair = minimax(depth - 1, board, alpha, beta, not is_maximizing, eval_func)
            best_score = max(best_score, pair[0])
            if pair[0] == best_score:
                best_move = board.peek()
            board.pop()
            alpha = max(alpha, best_score)

            # prune the sub-tree via alpha-beta
            if beta <= alpha:
                return (best_score, best_move)

        # return the best move we found
        return (best_score, best_move)

    # if we're the minimizing player
    else:
        # track the current best move. start with the worst move imaginable.
        best_score = float("inf")
        best_move = None

        # iterate over all available moves
        for x in possible_moves:
            # commit the move to the board state
            move = chess.Move.from_uci(str(x))
            board.push(move)

            # recurse to find the best move
            pair = minimax(depth - 1, board, alpha, beta, not is_maximizing, eval_func)
            best_score = min(best_score, pair[0])
            if pair[0] == best_score:
                best_move = board.peek()
            board.pop()
            beta = min(beta, best_score)

            # prune the sub-tree via alpha-beta
            if(beta <= alpha):
                return (best_score, best_move)

        # return the best move we found
        return (best_score, best_move)

# play_game() pits two ai's against each other in a game of chess
# @param white_eval     The evaluation function to be used by the white team.
# @param white_depth    The search depth to be used by the white team.
# @param black_eval     The evaluation function to be used by the black team.
# @param black_depth    The search depth to be used by the white team.
# @return               A string containing the result of the game, in points.
def play_game(white_eval, white_depth, black_eval, black_depth):
    board = chess.Board()

    # while the game is still going, play it
    while not board.is_game_over():
        # if it's white's turn
        if board.turn == chess.WHITE:
            # determine the best move to make via minimax-ab
            best_pair = minimax(white_depth, board, float("inf"), float("-inf"), True, white_eval)
            # make that move and pass the turn
            board.push(best_pair[1])

        # if it's black's turn
        else:
            # determine the best move to make via minimax-ab
            best_pair = minimax(black_depth, board, float("-inf"), float("inf"), False, black_eval)
            # make that move and pass the turn
            board.push(best_pair[1])

        # print the board at the end of each turn
        print(board)
        print("----------------")

    # print the final board state and return the result of the game
    print(board)
    return board.result()

# main() is the entry point
def main():
    # play an example game
    results = []
    for i in range(10):
        results.append(play_game(eval_countpieces, 3, eval_weightpieces, 3))
    print(results)
    #TODO(y'all):   Run some tests on a combination of evaluation complexity and
    #               search depth to determine what their effects are. You can
    #               run those games and collect those results here. An example
    #               loop to run games is demonstrated above.

# python is a dirty language and this is necessary
if __name__ == "__main__":
        main()
