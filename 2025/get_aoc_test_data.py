from bs4 import BeautifulSoup
import requests


def get_aoc_example(year, day, session):
    url = f"https://adventofcode.com/{year}/day/{day}"
    cookies = {"session": session}
    r = requests.get(url, cookies=cookies)
    
    soup = BeautifulSoup(r.text, "html.parser")

    # Find the first <pre><code>...</code></pre>
    code_block = soup.find("pre").get_text("\n").strip()
    return code_block
