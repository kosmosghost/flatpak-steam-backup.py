#!/bin/python3


import os
from os import listdir
from os.path import isfile, join
import subprocess

user = os.environ.get('USER')
steam = 'com.valvesoftware.Steam'
steam_game_dir = '/home/' + user + '/.var/app/' + steam + '/.local/share/Steam/steamapps/common/'
backup_dir = '/mnt/backup/Steam/'
files = os.listdir(steam_game_dir)
for i in files:
    subprocess.call(["rsync", "-axP", "--delete", steam_game_dir, backup_dir])
