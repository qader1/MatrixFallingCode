import os
import sys
from sys import stdout
import random
from time import sleep
from string import ascii_letters, digits, punctuation
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-he', '--height', type=int, default=18, help='height of falling string')
parser.add_argument('-s', '--speed', type=float, default=.035, help='time between lines in seconds')
args = parser.parse_args()


os.system('cls')
STRING = ascii_letters + digits + punctuation


class Ansi:
    green = '32'
    reset = '0'
    bright = '1'
    dim = '2'
    normal = '22'
    lightgreen = '92'

    def __init__(self):
        for name in dir(self):
            if not name.startswith('_'):
                setattr(self, name, f'\033[{getattr(self, name)}m')


def falling_code(length=20, speed=.045):
    style = Ansi()
    cols = os.get_terminal_size().columns
    line = [0 for x in range(cols)]
    while True:
        cols = os.get_terminal_size().columns
        if len(line) != cols:
            os.system('cls')
            line = [0 for _ in range(cols)]
        new = random.choice([x for x in range(len(line)) if line[x] == 0])
        line[new] += 1
        for i in line:
            stdout.write(style.green)
            if i == length:
                stdout.write(style.reset + random.choice(STRING))
            elif i == 0:
                stdout.write(' ')
            elif 1 <= i <= length//4:
                stdout.write(style.dim + random.choice(STRING))
            elif length//4 < i <= round((length/4)*2):
                stdout.write(style.normal + random.choice(STRING))
            elif round((length/4)*2) < i < round((length/4)*3):
                stdout.write(style.bright + random.choice(STRING))
            else:
                stdout.write(style.reset + style.lightgreen + style.bright + random.choice(STRING))
            stdout.write(style.reset)
        line = [x+1 if x < length and x != 0 else 0 for x in line]
        sys.stdout.flush()
        sleep(speed)


if __name__ == '__main__':
    falling_code(length=args.height, speed=args.speed)


