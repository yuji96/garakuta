import numpy as np


def play(player1, player2):
    """
    Play Rock–scissors–paper.

    Parameters
    ----------
    player1 : {'rock', 'scissors', 'paper'}
        Player 1 hand shape.
    player2 : {'rock', 'scissors', 'paper'}
        Player 2 hand shape.

    Returns
    -------
    result : {1, 0, -1}
        :1: Player 1 win
        :0: Draw
        :-1: Player 1 lose
        

    Examples
    --------
    >>> play('rock', 'rock')
    0
    >>> play('rock', 'paper')
    -1
    >>> play('rock', 'scissors')
    1

    """
    
    shape = {'rock':(1 ,0, 0), 'scissors':(0, 1, 0), 'paper':(0, 0, 1)}
    player1, player2 = shape[player1], shape[player2]
    re_array = np.cross(player1, player2)

    return re_array @ np.ones(3, dtype=int)