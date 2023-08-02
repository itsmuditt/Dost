import talkngreet as tg
import initialize as i
import dost as d
#second commit

tg.greet()
text = 'I am Dost. How may I be of service?'
tg.talk(text)


def begin():
    wakeup = i.initialize()
    if 'dost' in wakeup:
        conv = i.initialize()
        d.dost(conv)
        print('Program has returned!')
    else:
        tg.talk('I would love it sir if you could also greet me XD')
        begin()


begin()

while True:
    wak = i.initialize()
    d.dost(wak)
    print('Program has returned!')
    print('.')
