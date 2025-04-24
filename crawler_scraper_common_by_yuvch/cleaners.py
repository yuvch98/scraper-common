import html
from bs4 import BeautifulSoup


def clean_html(raw_html) -> str:
    if raw_html is None:
        return ""  # or return "No content"
    unescaped = html.unescape(raw_html)
    soup = BeautifulSoup(unescaped, "html.parser")
    return soup.get_text(separator="\n")
