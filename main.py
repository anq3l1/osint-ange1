import time
import os

from colorama import init
from colorama import Fore

from art import tprint
from osinter import search_username

import instaloader
from bs4 import BeautifulSoup  # for future updates
import requests

init()


def instagram_account_info(username):  # Get Instagram account info
    il = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(il.context, username=username)

        print(Fore.YELLOW + 'Instagram: ' + Fore.RESET + f'\n* Profile info: {username}\n___________________________\n\n'
              f'+ Profile biography: {profile.biography}\n'
              f'* Profile media: {profile.mediacount}\n'
              f'+ Profile followers: {profile.followers}\n'
              f'* Profile followees: {profile.followees}\n\n'
              f'+ Profile link: https://www.instagram.com/{username}\n'
              f'___________________________')

    except instaloader.exceptions.ProfileNotExistsException:
        print(Fore.YELLOW + 'Instagram: ' + Fore.RESET + f'\n* Profile info: {username}\n___________________________\n'
              + Fore.RED + '\nUser info not found!' + Fore.RESET)


def info_tg_account(username):  # Get Telegram account info
    url = 'https://t.me/' + username
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    name = soup.find(class_='tgme_page_title')
    user = soup.find(class_='tgme_page_extra')
    bio = soup.find(class_='tgme_page_description')

    if name and user:
        bio_text = bio.text if bio else "None"
        print(Fore.BLUE + '\nTelegram:' + Fore.RESET + f'\n+ Profile info: {username}\n___________________________\n\n'
              f'* Name: {name.text}\n'
              f'+ Username: {user.text}\n'
              f'* Bio: {bio_text}\n\n'
              f'+ Profile link: {url}\n'
              f'___________________________')
    else:
        print(Fore.BLUE + '\nTelegram:' + Fore.RESET + f'\n+ Profile info: {username}\n___________________________\n'
              + Fore.RED + '\nUser info not found!' + Fore.RESET)


def osint():
    username = input('* Enter the user of the person you want to scan: ')
    search_username(username)
    
    return username


def main_menu():
    while True:
        choice = input("\nEnter 'e/E' to exit the program, 'i/I' for more info, or 'a/A' to try again: ").lower()
        if choice == 'a':
            return 'again'
        elif choice == 'i':
            return 'info'
        elif choice == 'e':
            return 'exit'
        else:
            print("Invalid input. Please try again.")


def main():
    os.system('cls')
    time.sleep(1)
    tprint('os1nt anqe1', font='small')
    print('\t\t\t', ' powered by ange1')
    print('__________________________________________________\n')

    while True:
        username = osint()

        while True:
            action = main_menu()

            if action == 'again':
                break  # Exit to outer loop to re-enter username
            elif action == 'info':
                instagram_account_info(username)
                info_tg_account(username)
            elif action == 'exit':
                print("Exiting...")
                return


if __name__ == '__main__':
    main()
