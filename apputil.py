import numpy as np
from IPython.display import clear_output
import time
import seaborn as sns
import matplotlib.pyplot as plt


def update_board(current_board):
    """
    Execute one step of Conway's Game of Life.

    Parameters
    ----------
    current_board : numpy.ndarray
        A binary 2D NumPy array where 1 = alive and 0 = dead.

    Returns
    -------
    numpy.ndarray
        The updated board after one Game of Life step.
    """
    rows, cols = current_board.shape
    updated_board = np.zeros((rows, cols), dtype=int)

    for i in range(rows):
        for j in range(cols):
            # count living neighbors
            living_neighbors = 0

            for x in range(max(0, i - 1), min(rows, i + 2)):
                for y in range(max(0, j - 1), min(cols, j + 2)):
                    if (x, y) != (i, j):
                        living_neighbors += current_board[x, y]

            # apply Conway's Game of Life rules
            if current_board[i, j] == 1:
                if living_neighbors == 2 or living_neighbors == 3:
                    updated_board[i, j] = 1
                else:
                    updated_board[i, j] = 0
            else:
                if living_neighbors == 3:
                    updated_board[i, j] = 1
                else:
                    updated_board[i, j] = 0

    return updated_board


def play_game_recursive():
    """
    Bonus exercise:
    Recursively play Conway's Game of Life starting from a random 10x10 board.
    Returns the final board once the game reaches a stable state.
    """
    initial_board = np.random.randint(2, size=(10, 10))

    def recurse(board):
        next_board = update_board(board)

        # stop when board no longer changes
        if np.array_equal(board, next_board):
            return next_board

        return recurse(next_board)

    return recurse(initial_board)


def show_game(game_board, n_steps=10, pause=0.5):
    """
    Show `n_steps` of Conway's Game of Life, given the `update_board` function.

    Parameters
    ----------
    game_board : numpy.ndarray
        A binary array representing the initial starting conditions for Conway's Game of Life.
        In this array, 1 represents a "living" cell and 0 represents a "dead" cell.
    n_steps : int, optional
        Number of game steps to run through, by default 10
    pause : float, optional
        Number of seconds to wait between steps, by default 0.5
    """
    for step in range(n_steps):
        clear_output(wait=True)

        # update board
        game_board = update_board(game_board)

        # show board
        sns.heatmap(game_board, cmap='tab20c_r',
                    cbar=False, square=True, linewidths=1)
        plt.title(f'Board State at Step {step + 1}')
        plt.show()

        # wait for the next step
        if step + 1 < n_steps:
            time.sleep(pause)