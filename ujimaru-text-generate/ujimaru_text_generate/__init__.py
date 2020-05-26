__version__ = '0.1.0'

import requests
import sys


def get(country: str) -> str:
    url = f"https://corona-stats.online/{country}?minimal=true"
    response = requests.get(url, headers={'user-agent': 'curl'})
    return response.text


def main() -> None:
    country = sys.argv[1] if len(sys.argv) > 1 else ""
    print(get(country))
