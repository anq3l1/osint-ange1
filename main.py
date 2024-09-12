import tqdm
import time
import os
from colorama import init
from colorama import Fore
from art import tprint
from osinter import search_username

init()

os.system('cls')
time.sleep(1)
tprint('os1nt anqe1', font='small')
print('\t\t\t', ' powered by ange1')
print('__________________________________________________\n')

def osint():
    username = input('* Enter the user of the person you want to scan: ')

    search_username(username)

def main():
    osint()

    def try_again():
        while True:
            again_or_exit = input('\nEnter \'e/E\' to exit the program, or enter \'a/A\' to try again: ')
            if again_or_exit.lower() == 'a':
                osint()
            if again_or_exit.upper() == 'A':
                osint()
            elif again_or_exit.lower() == 'e':
                print('Exiting...')
                break
            elif again_or_exit.upper() == 'E':
                print('Exiting...')
                break
            else:
                print('Invalid enter. Try again.')
                try_again()

    try_again()

if __name__ == '__main__':
    main()
