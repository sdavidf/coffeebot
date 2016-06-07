#coffeebot.py
#post nonsense coffee orders to a twitter
#06.06.16

import random
from twython import Twython

APP_KEY = ""
APP_SECRET = ""
OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


def coffee():
	#these lists are under constant revision
    sizes = ["tall", "grande", "venti", "trenta"]
    attributes = ["soy", "half-caff", "decaf", "iced", "double-shot"]
    drinktype = ["latte", "frappucino", "tea", "Americano", "Mocha"]
    whip = ["with whip", "no whip", "with foam"]
	#yeah, foam != whip, but this is the place where a request for foam is
	#most syntactically valid
	#random generator
    random.seed()
    #randomize lists
    random.shuffle(sizes)
    random.shuffle(attributes)
    random.shuffle(drinktype)
    random.shuffle(whip)
    #pop the first element
    s = sizes[1]
    a = attributes[1]
    d = drinktype[1]
    w = whip[1]
	#push out order. TODO: Make it ruder.
    twitter.update_status(status="#coffeebot Give me a %s %s %s, %s." % (s, a, d, w))
    print "OK"

coffee()
