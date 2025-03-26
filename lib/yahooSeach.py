import requests
from bs4 import BeautifulSoup
import urllib.parse
import sys
from colorama import init, Fore, Style
from lib.constCode import validURL, get_unique_links

init(autoreset=True)

def yahoo_search(dork: str, b: int):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    url = "https://search.yahoo.com/search?p=" + urllib.parse.quote(dork) + "&b=" + str(b)
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            raise Exception("Failed to fetch search results")
    except requests.exceptions.Timeout:
        print(Fore.RED + "Request timed out")
        return []
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"An error occurred: {e}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    results = soup.select("a")
    
    for link in results:
        href = link.get("href")
        if href and "r.search.yahoo.com" in href and "RU=" in href:
            decoded_link = urllib.parse.unquote(href.split("RU=")[1].split("/RK=")[0])
            links.append(decoded_link)
    
    return links

def yahoo(dork: str, max_pages: int = 1000):
    links = []
    c = 1
    loop = True
    dots = "."
    print(Fore.YELLOW + Style.BRIGHT + "[+] Starting Search In Yahoo")
    print(Fore.GREEN + Style.BRIGHT + "[+] Search Valid.", end="", flush=True)  
    while loop:
        results = yahoo_search(dork, c)
        sys.stdout.write(f"\r{Fore.GREEN + Style.BRIGHT}[+] Search Valid{dots}")  
        sys.stdout.flush()
        dots += "." 
        try:
            if links and results and results[-1] == links[-1] or (not results) or c >= max_pages:
                loop = False
            for link in results:
                if validURL(link):
                    links.append(link)
            if c == 1:
                c += 1
            else:
                c += 7
        except Exception as e:
            print(Fore.RED + str(e))
            loop = False
    print()
    return get_unique_links(links)

if __name__ == "__main__":
    print(Fore.RED+Style.BRIGHT+"Error Not Allowed Run Tool From This File.")
