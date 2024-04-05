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


def rm_duplicates():
    list = Utilö.read_text_file("firstm.trxt")
    for l in list:
        Utilö.append_no_duplicates("cleaned.txt", l)

def get():
    print()
    scrapper = Scrapper(base_url)
    scrapper.login("tom@rozeedigital.com", "RuneScape05%")
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

def rmdupli():
    lines = Utilö.read_text_file("final.txt")
    finalLines = Utilö.remove_duplicates(lines)
    for line in finalLines:
        Utilö.append_string_to_file("final2.txt", line)

if __name__ == '__main__':
    print_hi()

