from lib.yahooSeach import yahoo
from lib.duckcuckgoSearch import duckduckgo
from lib.googleSearch import google
from sys import argv
from lib.constCode import get_unique_links
from colorama import init,Style, Fore as Fo
from lib.scaner import test_sqli, load_payloads
from lib.pagels import Panels

init(autoreset=True)

def handlet_args():
    if len(argv) >= 3:
        Panels.get_help()
        exit(1)
    elif len(argv) == 1:
        if argv[1] == "-h" or argv[1] == "--help":
            Panels.get_help()
            exit(1)
        if argv[1] == "-v" or argv[1] == "--version":
            print(f"{Style.BRIGHT }SQLKing Version: {Panels.get_version()}")
            exit(1)
        if argv[1] == "-n" or argv[1] == "--name":
            print(f"{Style.BRIGHT }Tool Name: {Panels.get_name()}")
            exit(1)
        if argv[1] == "-a" or argv[1] == "--author":
            print(f"{Style.BRIGHT }Author: {Panels.get_author()}")
            exit(1)
        if argv[1] == "-d" or argv[1] == "--description":
            print(f"{Style.BRIGHT }Description: {Panels.get_description()}")
            exit(1)
        if argv[1] == "-l" or argv[1] == "--license":
            print(f"{Style.BRIGHT }License: {Panels.get_license()}")
            exit(1)
        if argv[1] == "-u" or argv[1] == "--last-update":
            print(f"{Style.BRIGHT }Last Update: {Panels.get_last_update()}")
            exit(1)
        else:
            dork = argv[1]
            pages = None
    elif len(argv) == 2:
        dork = argv[1]
        pages = int(argv[2])
    else:
        Panels.get_help()
        exit(1)
    return dork, pages

try :
    panel = Panels()
    print(panel.panel())
    dork,panel = handlet_args()
    res = google(dork,pages)
    res+= yahoo(dork,pages) 
    res+= duckduckgo(dork,pages)
    res = get_unique_links(res)
    try:
        py = load_payloads('./lib/db.txt')
    except Exception as e:
        print(f"{Fo.RED}{Style.BRIGHT }[-] Error reading payload file: {e}")
        py = []
        exit(1)
    for re in res :
        if py == []:
            exit(1)
        vulnerable, payload = test_sqli(py, re)
        if vulnerable:
            print(f"{Style.BRIGHT }[+] SQL Injection Vulnerability Found: {re} with payload: {payload}")
        else:
            pass
except KeyboardInterrupt:
    print(f"\n{Style.BRIGHT }[-] User Interrupted")
except Exception as e:
    print(f"\n{Style.BRIGHT }[-] An error occurred: {e}")