from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    # pass
    while front_is_clear():
        one_line()
        if facing_east():
            turn_left()
        else:
            turn_right()
        if front_is_clear():
            move()
            if right_is_blocked():
                turn_left()
            else:
                turn_right()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def one_line():
    while front_is_clear():
        move()
        put_beeper()
        if front_is_clear():
            move()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
