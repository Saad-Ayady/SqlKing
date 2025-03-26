import sys
from googlesearch import search
from colorama import init, Fore, Style
from lib.constCode import validURL, get_unique_links

init(autoreset=True)

def google_search(dork: str, num_results: int):
    try:
        results = []
        for result in search(dork, num_results=num_results):  # Removed stop=num_results argument
            results.append(result)
        return results
    except Exception as e:
        print(Fore.RED + f"An error occurred while fetching results: {e}")
        return []

def google(dork: str, max_results: int = 100):
    links = []
    print(Fore.YELLOW + Style.BRIGHT + "[+] Starting Search In Google")
    print(Fore.GREEN + Style.BRIGHT + "[+] Search Valid.", end="", flush=True)
    
    try:
        results = google_search(dork, max_results)
        for link in results:
            if validURL(link):
                links.append(link)
        print()  # New line after progress dots
    except Exception as e:
        print(Fore.RED + str(e))
    
    return get_unique_links(links)

if __name__ == "__main__":
    print(Fore.RED + Style.BRIGHT + "Error Not Allowed Run Tool From This File.")
