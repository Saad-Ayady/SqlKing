from colorama import Fore, Style
import requests
import time
from concurrent.futures import ThreadPoolExecutor

ERROR_PATTERNS = {
    "syntax error", "mysql_error", "unclosed quotation mark",
    "SQL syntax", "unexpected T_SQL", "incomplete query",
    "unknown column", "unknown table", "incorrect syntax",
    "database connection error", "you have an error in your SQL syntax"
}

def load_payloads(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except Exception as e:
        print(f"Error reading payload file: {e}")
        return []

def contains_error(response_text):
    text_lower = response_text.lower()
    return any(pattern in text_lower for pattern in ERROR_PATTERNS)

def test_payload(payload, url, initial_response):
    full_url = url + payload
    try:
        start_time = time.time()
        response = requests.get(full_url, timeout=5)
        elapsed_time = time.time() - start_time

        if contains_error(response.text) or elapsed_time > 5:
            return True, payload
    except requests.RequestException:
        pass
    return False, None

def test_sqli(payloads, url):
    try:
        initial_response = requests.get(url, timeout=5).text
    except requests.RequestException:
        return False, None
    try :
        with ThreadPoolExecutor(max_workers=10) as executor:
            results = executor.map(lambda p: test_payload(p, url, initial_response), payloads)
        for is_vulnerable, payload in results:
            if is_vulnerable:
                return True, payload
    except KeyboardInterrupt:
        print(f"\n{Style.BRIGHT }User Interrupted")
        exit(1)
    return False, None

if __name__ == "__main__":
    print(Fore.RED + Style.BRIGHT + "Error Not Allowed Run Tool From This File.")
