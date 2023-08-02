import googlesearch


def dictionary(word):
    url = 'https://www.dictionary.com/browse/' + word
    return url


def enquiry(query):
    url = googlesearch.lucky(query)
    return url
