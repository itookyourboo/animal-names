from enum import Enum


class State(Enum):
    MAIN_MENU = 0
    SEX = 1
    NAME = 2


State.ALL = tuple(State)
