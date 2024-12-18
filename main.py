import random
from decouple import config

# Загружаем настройки из файла
RANGE_MIN = config("range_min", cast=int)
RANGE_MAX = config("range_max", cast=int)
ATTEMPTS = config("attempts", cast=int)
STARTING_CAPITAL = config("starting_capital", cast=int)
from logic import play_game

if __name__ == "main":
    play_game()