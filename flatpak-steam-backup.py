#!/bin/python3


import os
import sys
from os import listdir
from os.path import isfile, join
import subprocess

user = os.environ.get('USER')
steam = 'com.valvesoftware.Steam'
steam_game_dir = '/home/' + user + '/.var/app/' + steam + '/.local/share/Steam/steamapps/common/'
files = os.listdir(steam_game_dir)


def help():
    print("Usage:\nflatpak-steam-backup.py <OPTIONS> <PATH>")
    print("\nOptions:")
    print("--backup\tBacks up game files from Steam directory TO <PATH>")
    print("--restore\tRestores game files TO Steam directory FROM <PATH>")
    print("--help\t\tShow help menu.")

def restore(path):
    subprocess.call(["rsync", "-axP", "--delete", path, steam_game_dir])

def backup(path):
    for i in files:
        subprocess.call(["rsync", "-axP", "--delete", steam_game_dir + i, path])

def check_if_path_valid(path):
    if os.path.isdir(path) != True:
        print("ERROR: Directory doesn't exist!")
        sys.exit()
    else:
        return path

def main():
    args = sys.argv
    for i in args:
        if i == "--help":
            help()
            sys.exit()
        elif i == "-h":
            help()
            sys.exit()

    if len(args) != 3:
        print("ERROR: INVALID NUMBER OF ARGUMENTS. SEE \"--help\"")
        sys.exit()

    path = args[2]

    if args[1] == "--backup":
        backup(check_if_path_valid(args[2]))
    elif args[1] == "--restore":
        restore(check_if_path_valid(args[2]))
    else:
        print("Invalid Command Line Option:")
        print("Valid <OPTION> are --backup or --restore")
        print("See \"--help\"")

main()