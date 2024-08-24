from bs4 import BeautifulSoup
import requests
import config
import urllib.parse
import os

def get_links_from_homepage(url: str) -> list[str]:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    return list(set([link["href"] for link in soup.find_all("a", href=True)]))


def update_seesaa_links():
    base_url: str = "https://anothereden.game-info.wiki/d/"
    endpoints: list[str] = [
        urllib.parse.quote(config.STAR5_TITLE.encode("euc-jp")),
        urllib.parse.quote(config.BUDDY_TITLE.encode("euc-jp"))
    ]

    try:
        os.remove("code/links/aewiki.txt")
    except OSError:
        pass

    for endpoint in endpoints:
        links = get_links_from_homepage(base_url + endpoint)
        links = [link for link in links if link.startswith(base_url)]
        with open("code/links/seesaa.txt", "a+", encoding="utf-8") as file:
            file.write("\n".join(links) + "\n")

def update_aewiki_links():
    base_url: str = "https://anothereden.wiki/w/"
    endpoints: list[str] = ["Characters", "Sidekick"]

    try:
        os.remove("code/links/aewiki.txt")
    except OSError:
        pass

    for endpoint in endpoints:
        links = get_links_from_homepage(base_url + endpoint)
        links = [link for link in links if link.startswith("/w/")]
        with open("code/links/aewiki.txt", "a+", encoding="utf-8") as file:
            file.write("\n".join(links) + "\n")

if __name__ == "__main__":
    os.makedirs("code/links", exist_ok=True)
    update_seesaa_links()
    update_aewiki_links()

