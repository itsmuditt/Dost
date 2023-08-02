import requests
import bs4 as bs
from summarizer import FrequencySummarizer

total_parse = 4


def fromURL(url):
    t = requests.get(url)
    soup = bs.BeautifulSoup(t.text, "html.parser")
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    text = text.replace('Â', '').replace('â', '')
    return text


def summarize(url, total_parse):
    ut = fromURL(url)
    fs = FrequencySummarizer()

    summary = fs.summarize(ut.replace("\n", " "), total_parse)
    return " ".join(summary)
