import numpy as np
from random import randint


def play(shape1, shape2):
    """
    Play Rock–scissors–paper.

    Parameters
    ----------
    shape1 : {'rock', 'scissors', 'paper'}
    shape2 : {'rock', 'scissors', 'paper'}

    Returns
    -------
    result : {1, 0, -1}
        :1: shape1 win
        :0: Draw
        :-1: shape1 lose
        

    Examples
    --------
    >>> play('rock', 'rock')
    0
    >>> play('rock', 'paper')
    -1
    >>> play('rock', 'scissors')
    1

    """
    
    to_one_hot = {'rock':(1, 0, 0), 'scissors':(0, 1, 0), 'paper':(0, 0, 1)}
    shape1, shape2 = to_one_hot[shape1], to_one_hot[shape2]
    re_array = np.cross(shape1, shape2)

    return re_array @ np.ones(3, dtype=int)



index = int(input("choose shape\n0: rock\n1: scissors\n2: paper\n"))
shape = ('rock', 'scissors', 'paper')[index]
com1 = ('rock', 'scissors', 'paper')[randint(0, 2)]
print(f"you: {shape}")
print(f"com: {com1}")
print(play(shape, com1))