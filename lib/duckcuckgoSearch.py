import requests
from bs4 import BeautifulSoup
import urllib.parse
import sys
from colorama import init, Fore, Style
import time
from lib.constCode import validURL, get_unique_links

init(autoreset=True)

def duckduckgo_search(dork: str, b: int, max_retries: int = 7):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Referer": "https://duckduckgo.com/"
    }
    
    url = f"https://duckduckgo.com/html/?q={urllib.parse.quote(dork)}&b={str(b)}"
    retries = 0  # Initialize retry counter
    links = []
    while retries < max_retries:
        try:
            with requests.Session() as session:
                response = session.get(url, headers=headers, timeout=10, allow_redirects=True)
                if response.status_code == 202:
                    print(Fore.YELLOW + f"Request accepted for processing (202 status code), retrying... ({retries + 1}/{max_retries})")
                    retries += 1
                    time.sleep(3)
                    continue 

                if response.status_code != 200:
                    print(Fore.RED + f"Failed to fetch search results. Status code: {response.status_code}")
                    return []
                soup = BeautifulSoup(response.text, "html.parser")
                links = []
                results = soup.select("a.result__a")
                
                for link in results:
                    href = link.get("href")
                    if href:
                        links.append(href)

                return links 
        except requests.exceptions.Timeout:
            print(Fore.RED + f"Request timed out. Retrying... ({retries + 1}/{max_retries})")
            retries += 1
            time.sleep(3)  # Add delay before retrying
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"An error occurred: {e}")
            return []

    print(Fore.RED + "Max retries reached. Aborting search.")
    return links if links else []

def duckduckgo(dork: str, max_pages: int = 1000):
    links = []
    c = 1
    loop = True
    dots = "."
    print(Fore.YELLOW + Style.BRIGHT + "[+] Starting Search In DuckDuckGo")
    print(Fore.GREEN + Style.BRIGHT + "[+] Search Valid.", end="", flush=True)  
    while loop:
        results = duckduckgo_search(dork, c)
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
                c += 50  # DuckDuckGo paginates in increments of 50
            time.sleep(1)  # Adding delay between requests to avoid rate limiting
        except Exception as e:
            print(Fore.RED + str(e))
            loop = False
    print()
    return get_unique_links(links)

if __name__ == "__main__":
    print(Fore.RED + Style.BRIGHT + "Error Not Allowed Run Tool From This File.")
