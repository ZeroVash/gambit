#------------------------------------------------------------------------------
# Constant and Variables Values
#------------------------------------------------------------------------------
import re
import itertools

playerside = None
sideflip = None
diesides = 20
ownLP = 100
ownGold  = 5

def clear(card, x = 0, y = 0):
    mute()
    card.target(False)

	
def setDie(group, x = 0, y = 0):
    mute()
    global diesides
    num = askInteger("How many sides?\n\nFor Coin, enter 2.\nFor Chaos die, enter 6.", diesides)
    if num != None and num > 0:
      diesides = num
      dieFunct(diesides)

	  
def rollDie(group, x = 0, y = 0):
    mute()
    global diesides
    dieFunct(diesides)

	
def dieFunct(num):
    if num == 6:
      n = rnd(1, 6)
      if n == 1:
        notify("{} rolls 1 (PLANESWALK) on a 6-sided die.".format(me))
      elif n == 6:
        notify("{} rolls 6 (CHAOS) on a 6-sided die.".format(me))
      else:
        notify("{} rolls {} on a 6-sided die.".format(me, n))
    elif num == 2:
      n = rnd(1, 2)
      if n == 1:
        notify("{} rolls 1 (HEADS) on a 2-sided die.".format(me))
      else:
        notify("{} rolls 2 (TAILS) on a 2-sided die.".format(me))
    else:
      n = rnd(1, num)
      notify("{} rolls {} on a {}-sided die.".format(me, n, num))

	  
def add_lp(group, x = 0, y = 0):
	mute()
	global ownLP
	count = askInteger("Add how much LP?", 10)
	if count == None: return
	ownLP += count
	notify("{} adds {} LP. Current: {}.".format(me, count, ownLP))

	
def remove_lp(group, x = 0, y = 0):
	mute()
	global ownLP
	count = askInteger("Remove how many LP?", 10)
	if count == None: return
	ownLP -= count
	notify("{} removes {} LP. Current: {}.".format(me, count, ownLP))

	
def add_gold(group, x = 0, y = 0):
	mute()
	global ownGold
	count = askInteger("Add how much Gold?", 1)
	if count == None: return
	ownGold += count
	notify("{} adds {} Gold. Current: {}.".format(me, count, ownGold))

	  
def remove_gold(group, x = 0, y = 0):
	mute()
	global ownGold
	count = askInteger("Remove how much Gold?", 1)
	if count == None: return
	ownGold -= count
	notify("{} removes {} Gold. Current: {}.".format(me, count, ownGold))

 
def tap(card, x = 0, y = 0):
	mute()
	card.orientation ^= Rot90
	if card.orientation & Rot90 == Rot90:
		notify('{} taps {}.'.format(me, card))
	else:
		notify('{} untaps {}.'.format(me, card))

		
def play_flip(card, x = 0, y = 0):
	mute()
	card.moveToTable(0,0)
	card.isFaceUp = False
	notify('{} plays a card face/down.'.format(me))  

	
def flip(card, x = 0, y = 0):
	mute()
	if card.isFaceUp:
		card.isFaceUp = False
		notify('{} flips {}.'.format(me, card))
	else:
		card.isFaceUp = True
		notify('{} flips {}.'.format(me, card))

		
def shuffle(group, x = 0, y = 0):
    mute()
    for card in group:
        if card.isFaceUp:
            card.isFaceUp = False
    group.shuffle()
    notify("{} shuffled their {}".format(me, group.name))

	
def draw(group, x = 0, y = 0):
    mute()
    if len(group) == 0: return
    card = group[0]
    card.moveTo(card.owner.hand)
    notify("{} draws a card.".format(me))

	
def drawX(group, x = 0, y = 0):
    if len(group) == 0: return
    mute()
    count = askInteger("Draw how many cards?", 7)
    if count == None: return
    for card in group.top(count): card.moveTo(card.owner.hand)
    notify("{} draws {} cards.".format(me, count))