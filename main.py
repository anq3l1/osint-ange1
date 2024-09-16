import time
import os

from colorama import init
from colorama import Fore

from art import tprint
from osinter import search_username

import instaloader
from bs4 import BeautifulSoup # for next updates
import requests

init()

def instagram_account_info(username): # get info Instagram account
    il = instaloader.Instaloader()

    profile = instaloader.Profile.from_username(context=il.context, username=username)

    print(Fore.YELLOW + 'Instagram: ' + Fore.RESET + f'\n* Profile info: {username}\n___________________________\n\n+ Proflie biography: {profile.biography}\n* Proflie media: {profile.mediacount}\n+ Profile followers: {profile.followers}\n* Profile followees: {profile.followees}\n\n+ Profile link: https://www.instagram.com/' + username, '\n___________________________')

def info_tg_account(username): # get info Telegram account
    url = 'https://t.me/' + username

    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')

    name = soup.find(class_='tgme_page_title')
    user = soup.find(class_='tgme_page_extra')
    bio = soup.find(class_='tgme_page_description')

    if bio is not None:
        print(Fore.BLUE + '\nTelegram:' + Fore.RESET + f'\n+ Profile info: {username}\n___________________________\n\n* Name: {name.text}\n+ Username: {user.text}\n* Bio: {bio.text}\n\n+ Profile link: {url}\n___________________________')
    else:
        print(Fore.BLUE + '\nTelegram:' + Fore.RESET + f'\n+ Profile info: {username}\n___________________________\n\n* Name: {name.text}\n+ Username: {user.text}\n* Bio: None\n\n+ Profile link: {url}\n___________________________')

os.system('cls')
time.sleep(1)
tprint('os1nt anqe1', font='small')
print('\t\t\t', ' powered by ange1')
print('__________________________________________________\n')

def osint():
    global username
    username = input('* Enter the user of the person you want to scan: ')

    search_username(username)

def main():
    osint()

    def try_again():
        while True:
            again_or_exit_or_info = input('\nEnter \'e/E\' to exit the program, or \'i/I\' for more info, or enter \'a/A\' to try again: ')
            if again_or_exit_or_info.lower() == 'a':
                osint()
            if again_or_exit_or_info.upper() == 'A':
                osint()
            elif again_or_exit_or_info.lower() == 'i':
                print('More info:\n')
                instagram_account_info(username=username)
                info_tg_account(username=username)
            elif again_or_exit_or_info.lower() == 'I':
                print('More info:\n')
                instagram_account_info(username=username)
                info_tg_account(username=username)
            elif again_or_exit_or_info.lower() == 'e':
                print('Exiting...')
                break
            elif again_or_exit_or_info.upper() == 'E':
                print('Exiting...')
                break
            else:
                print('Invalid enter. Try again.')
                try_again()

    try_again()

if __name__ == '__main__':
    main()
