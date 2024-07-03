import random

def gerador_dados(size):
    return [random.randint(0, 1000000) for _ in range(size)]