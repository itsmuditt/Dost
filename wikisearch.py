import wikipedia
import URLsum
import talkngreet as tg
import initialize as i
import createURL


def wiki(conv):
    try:
        short = 4
        long = 8
        wik = conv.replace('search', 'wiki')
        wik = wik.replace('wiki', '')
        if 'short' in conv:
            parse = short
            wik = wik.replace('short: ', '')
        elif 'long' in conv:
            parse = long
            wik = wik.replace('long: ', '')
        else:
            tg.talk('Do you want it brief or elaborated?')
            ver = i.initialize()
            if 'elaborated' in ver:
                parse = long
            else:
                parse = short

        results = wikipedia.summary(wik, sentences=parse)
        return results

    except:
        query = conv
        url = createURL.enquiry(query)
        result = URLsum.summarize(url, 3)
        return result