from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
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
    turn_left()
    while right_is_clear():
        fill_the_avenue()
        if facing_north():
            turn_right()
        else:
            turn_left()
        if front_is_clear():
            next_stage()
        if left_is_blocked():
            turn_right()
        else:
            turn_left()


def fill_the_avenue():
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
            move()
        else:
            move()


def next_stage():
    move()
    move()
    move()
    move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


if __name__ == "__main__":
    run_karel_program()
