#coffeebot2.py
#new coffeebot, reads from text files
#06.07.2016
import random
from twython import Twython

#initial stuff, needs refactored into something neater...
APP_KEY = ""
APP_SECRET = ""
OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

(size, flavor, attribute, topping) = [], [], [], []


def assign():
    #reads drink names from file, separates data from code
    global size
    global flavor
    global attribute
    global topping

    s = open("sizes.txt")
    f = open("flavors.txt")
    a = open("attributes.txt")
    t = open("toppings.txt")

    size = s.read().splitlines()
    flavor = f.read().splitlines()
    attribute = a.read().splitlines()
    topping = t.read().splitlines()

def post():
    #shuffles lists, makes post (not modular enough!!!)
    random.shuffle(size)
    random.shuffle(attribute)
    random.shuffle(flavor)
    random.shuffle(topping)

    #push out order. TODO: Make it ruder.
    twitter.update_status(status="#coffeebot Give me a %s %s %s, with %s."
        % (size[1], flavor[1], attribute[1], topping[1]))


assign()
post()
