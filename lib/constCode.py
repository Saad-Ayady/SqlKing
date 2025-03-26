def get_unique_links(links):
    unique_links = []
    seen = set()
    for link in links:
        if link not in seen:
            unique_links.append(link)
            seen.add(link)    
    return unique_links

def validURL(url):
    if "javascript" in url or ".js" in url or ".css" in url:
        return False
    words = ["google", "microsoft", "bing", "yahoo", "duckduckgo", "youtube", "facebook", "instagram", "twitter", "linkedin", "pinterest", "tumblr", "reddit", "github", "gitlab", "bitbucket", "stackoverflow", "wikipedia", "fandom", "wikia", "amazon", "ebay"]
    for word in words:
        if word in url:
            return False
    return True
