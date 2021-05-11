# coding=utf-8
import random

GAME_STRING = "新的24点游戏！数字："

def generate_new_game():
    numbers = []
    for i in range(4):
        numbers.append(str(random.randint(1, 9)))
    return GAME_STRING + ", ".join(numbers)
