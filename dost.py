import datetime
import webbrowser
import pyjokes
import pywhatkit
import URLsum
import createURL
import initialize as i
import mail
import talkngreet as tg
import wikisearch

conv = ''


def respo(word):
    b = False
    if word == 'yes':
        b = True
    elif word == 'sure':
        b = True
    elif word == 'no':
        b = True
    return b


def repeat():
    global conv
    conv = i.initialize()
    dost(conv)


def dost(conversation):
    if 'play' in conversation:
        song = conversation.replace('play ', '')
        tg.talk('playing ' + song)
        pywhatkit.playonyt(song)
        tg.talk('I will let you listen to it now XD')
        con = i.initialize()
        if 'yes' or 'okay' or 'sure' in con:
            return
        else:
            dost(con)

    elif 'time' in conversation:
        time = datetime.datetime.now().strftime('%I:%M %p')
        tg.talk('Current time is ' + time)
        tg.talk('You want me to do something?')
        repeat()

    elif 'google' in conversation:
        query = conversation.replace('google ', '')
        tg.talk('Googling...')
        url = createURL.enquiry(query)
        result = URLsum.summarize(url, 4)
        tg.talk('According to Google, ' + result)
        tg.talk('Happy Now?')
        repeat()

    elif 'search' in conversation:
        tg.talk('Searching Wikipedia...')
        find = conversation.replace('search ', '')
        results = wikisearch.wiki(find)
        tg.talk('According to Wikipedia, ' + results)
        tg.talk('R u satisfied now?')
        repeat()

    elif 'meaning' in conversation:
        word = conversation.replace('what\'s the meaning of ', '')
        url = createURL.dictionary(word)
        webbrowser.open(url)
        tg.talk('Will there be anything else Sir?')
        repeat()

    elif 'who' in conversation:
        try:
            person = conversation.replace('who is', '')
            person = person.replace('who are', '')
            person = person.replace('who were', '')
            tg.talk('Let me search the web...')
            results = wikisearch.wiki(person)
            tg.talk(results)
            tg.talk('Anything else... Sir?')
            repeat()
        except:
            tg.talk('Oops! The program has bumped into an Exception :( Could u please repeat Sir?')
            return

    elif 'joke' in conversation:
        tg.talk(pyjokes.get_joke())
        tg.talk('Will there be anything else Sir?')
        repeat()

    elif 'thank' in conversation:
        tg.talk('Glad I could help Sir!')
        return

    elif respo(conversation):
        tg.talk('It was a rhetoric question, u stupid Hooman!')
        repeat()

    elif 'mail' in conversation:
        print('Who do you want to send a mail?\n')
        receiver = input()
        mail.sendmail(receiver)

    elif ('quit' or 'exit') in conversation:
        tg.talk('Have a Good Day Sir!')
        exit(0)

    else:
        try:
            query = conversation
            url = createURL.enquiry(query)
            result = URLsum.summarize(url, 3)
            tg.talk('According to Google, ' + result)
            tg.talk('Will there be anything else Sir?')
            repeat()
        except:
            tg.talk('Oops! The program has bumped into an Exception :( Could u please repeat Sir?')
            return
