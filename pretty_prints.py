import os
from time import sleep

def cls():
    os.system('cls')

def print_with_cls(text_to_print):
    cls()
    print(text_to_print)

def sleep_with_cls(sleep_time):
    sleep(sleep_time)
    cls()
