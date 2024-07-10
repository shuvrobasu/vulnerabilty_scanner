# Author: Shuvro, Basu
# Date: 2021-09-26
# Version: 1.0
# Description: A simple vulnerability scanner for a domain.
# Usage: python scanner.py


import requests
from requests.exceptions import RequestException
import os
from datetime import datetime
from urllib.parse import urlparse

# Color definitions for terminal output
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = '\033[96m'
RESET = "\033[0m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_WHITE = "\033[97m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"  # Bright magenta
ORANGE = "\033[38;5;208m"  # Orange
BRIGHT_CYAN = "\033[96m"  # Bright cyan
UNDERLINE = "\033[4m"  # Underline
BOLD = "\033[1m"  # Bold

# Banner
banner = BRIGHT_BLUE + BOLD + """ 
  _   __     __                  __   __      ___                  _        _______           __          
 | | / /_ __/ /__  ___ _______ _/ /  / /__   / _ \___  __ _  ___ _(_)__    / ___/ /  ___ ____/ /_____ ____
 | |/ / // / / _ \/ -_) __/ _ `/ _ \/ / -_) / // / _ \/  ' \/ _ `/ / _ \  / /__/ _ \/ -_) __/  '_/ -_) __/ 
 |___/\_,_/_/_//_/\__/_/  \_,_/_.__/_/\__/ /____/\___/_/_/_/\_,_/_/_//_/  \___/_//_/\__/\__/_/\_\\__/_/    
""" + RESET + BRIGHT_MAGENTA + UNDERLINE + r""" VULNERABILITY SCANNER FOR DOMAIN """ + RESET + BRIGHT_CYAN + "\n" + r"""(c) Shuvro, Basu, 2024. All rights reserved.""" + """
""" + BRIGHT_RED + """[!] Legal disclaimer: Usage of this tool without prior mutual consent is illegal.
    It is the end user's responsibility to obey all applicable local, state, and federal laws.
    Developer assumes no liability and is not responsible for any misuse or damage caused by this program.""" + RESET

print(banner)

def is_valid_domain(domain):
    """Check if the domain is valid."""
    try:
        response = requests.get(domain)
        response.raise_for_status()
        return True
    except RequestException:
        return False

def check_domain(domain):
    """Check the domain and return the domain."""
    if not domain.startswith("http://") and not domain.startswith("https://"):
        domain = "http://" + domain
    if not is_valid_domain(domain):
        print(BRIGHT_RED + f"[!] Domain {domain} does not exist or is not reachable. Trying HTTPS..." + RESET)
        domain = domain.replace("http://", "https://")
        if not is_valid_domain(domain):
            print(BRIGHT_RED + f"[!] Domain {domain} does not exist or is not reachable. Exiting." + RESET)
            return None
    return domain

def read_folders_from_file(file_path='def.vol'):
    """Read folders from a file if it exists, otherwise return default list."""
    try:
        with open(file_path, 'r') as file:
            folders = file.read().splitlines()
        return folders
    except FileNotFoundError:
        print(BRIGHT_RED + f"[!] File {file_path} not found. Using default folders." + RESET)
        return None

def scan_directory(domain, directories):
    """Scan the directories for the domain."""
    found_links = []
    for i, dir in enumerate(directories, start=1):
        url = f"{domain}/{dir}/"
        try:
            response = requests.get(url)
            status_code = response.status_code
            if status_code == 200:
                found_links.append(url)
                print(BRIGHT_GREEN + f"[+] Found: {url} {status_code} - {response.reason} - May be vulnerable !" + RESET)
            else:
                print(BRIGHT_RED + f"[-] Not Found: {url} {status_code} - {response.reason}" + RESET)
        except RequestException as e:
            print(BRIGHT_BLUE + f"[-] Error accessing {url}: {e}" + RESET)
    return found_links

def sanitize_filename(domain):
    """Sanitize the domain name for use in filenames."""
    return domain.replace("http://", "").replace("https://", "").replace("/", "_")

def save_to_file(domain, found_links):
    """Save the found links to a file."""
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    sanitized_domain = sanitize_filename(domain)
    filename = f"{sanitized_domain}_{timestamp}.vul.txt"

    with open(filename, "w") as file:
        file.write(f"Domain: {domain}\n")
        file.write(f"(c) Shuvro, Basu, 2024. Vulnerability Scanner for Domain\n")
        file.write(f"Scan date: {timestamp}\n\n")
        for link in found_links:
            file.write(link + "\n")
    print(GREEN + f"Results saved to {filename}" + RESET)

def main():
    """Main function to execute the scanner."""
    domain = input(BRIGHT_GREEN + "Enter the domain name (e.g., example.com) [Blank to Exit]: " + RESET).strip()
    if not domain:
        print(BRIGHT_RED + "No domain entered. Exiting." + RESET)
        return

    domain = check_domain(domain)
    if not domain:
        return

    case_option = input(BRIGHT_YELLOW + "Do you want to scan with lower case, upper case, or both? (l/u/b): " + RESET ).strip().lower()
    if case_option not in ['l', 'u', 'b']:
        print(BRIGHT_RED + "Invalid option. Exiting." + RESET)
        return

    directories = read_folders_from_file() or [
        "admin", "backup", "test", "old", "public", "tmp", "uploads", "includes",
        "cgi-bin", "private", "data", "beta", "staging", "secure", "web", "login",
        "wp-admin", "wp-content", "wp-includes"
    ]

    scan_directories = []
    if case_option in ['l', 'b']:
        scan_directories.extend(directories)
    if case_option in ['u', 'b']:
        scan_directories.extend([dir.upper() for dir in directories])

    found_links = scan_directory(domain, scan_directories)

    if not found_links:
        print(BRIGHT_RED + "[!] No vulnerabilities found." + RESET)
        return

    view_links = input(BRIGHT_YELLOW + "Do you want to see the links? (y/n): " + RESET).strip().lower()
    if view_links == 'y':
        for link in found_links:
            print(GREEN + link + RESET)

    save = input(BRIGHT_BLUE + "Do you want to save the found links to a file? (y/n): " + RESET ).strip().lower()
    if save == 'y':
        save_to_file(domain, found_links)

if __name__ == "__main__":
    main()
