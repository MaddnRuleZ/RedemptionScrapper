import re

import Utilö
from Scrapper import Scrapper

base_url = "https://app.trendrocket.io/brands/discover"


def find_matches(text):
    pattern = r'css-18ipzgs">(.*?)</h6>'
    matches = re.findall(pattern, text)
    return matches


def print_hi():
    print()
    scrapper = Scrapper(base_url)
    scrapper.searchRoutine("tom@rozeedigital.com", "RuneScape05%")
    x = input()

def scan_for_match():
    lines = Utilö.read_text_file("firstm.trxt")
    matches = []
    for line in lines:
        match = find_matches(line)
        for m in match:
            print(m)
            matches.append(m)

    print("#### Done")
    for match in matches:
        print(match)




if __name__ == '__main__':
    print_hi()
    # print_hi('PyCharm')

