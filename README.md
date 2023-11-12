# flatpak-steam-backup.py

## Description:

This is a super simple script that will backup steam game files from the default Steam flatpak directory to a backup directory.

## Requirements:

The only requirements are:

- python3
- rsync

## Usage:

Usage:
flatpak-steam-backup.py <OPTIONS> <PATH>

Options:
--backup        Backs up game files from Steam directory TO <PATH>
--restore       Restores game files TO Steam directory FROM <PATH>
--help          Show help menu.
