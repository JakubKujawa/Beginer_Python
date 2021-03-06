# Author: CodePlayer
# Date: 23.02.2021
# ADMINISTRATOR PRIVILEGES REQUIRED!!!
from pathlib import Path
import platform

blocked_sites = []
website = Path('website.txt')
redirect = "127.0.0.1"


def h_path():   # Returns the path to the hosts file depending on your system
    if platform.system() == 'Windows':
        path = r"C:\Windows\System32\drivers\etc\hosts"
    elif platform.system() == 'Linux':
        path = "/etc/hosts"
    return path


def load_file():   # Loads/Creates 'website.txt'
    global blocked_sites
    if Path.is_file(website):
        with open(website, 'r') as f:
            lines = f.read().split('\n')
            blocked_sites = [line.strip() for line in lines if len(line) > 0]
    else:
        print("File 'website.txt' is missing\nCreating file...")
        with open(website, 'w') as f:
            pass


def save_file():   # Saves the file
    with open(website, 'w') as f:
        for site in blocked_sites:
            f.write(f"{site}\n")


def input_sites():   # Ability to enter websites to block
    global blocked_sites
    done = 1
    print("Enter either the page to be blocked or 'q' to complete the data entry")
    while done:
        site = input("> ")
        if site.lower() in {'q', 'quit', 'stop'}:
            done = 0
        else:
            blocked_sites.append(site)

    blocked_sites = list(filter(str.strip, blocked_sites))


def block():   # Overwrites the hosts file 
    load_file()
    input_sites()
    path = h_path()
    with open(path, 'r+') as hostfile:
        hosts = hostfile.read()
        for site in blocked_sites:
            if site not in hosts:
                hostfile.write(f"{redirect} {site}\n")
    print("\nBlocked websites:")
    for _, site in enumerate(blocked_sites):
        print(f"> {site}")

    save_file()
    input("\nEnter anything to exit\n> ")


if __name__ == '__main__':
    block()
