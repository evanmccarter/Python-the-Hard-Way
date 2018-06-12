from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"
    
    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number")
    
    if how_much < 50:
        print "Nice, youre not greedt, you win"
        exit(0)
    else:
        dead("You greedy boy")

def bear_room():
    print "There is a bear here"
    print "The bear has a lot of honey"
    print "The fat bear is in front of a door"
    print "How are u going to move the bear?"
    bear_moved = False
    
    while True:
        next = raw_input("> ")
        
        if next == "take honey":
            dead("Bear slaps ur face")
        elif next == "taunt bear" and not bear_moved:
            print "Bear moved to door"
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("You pissed off the bear")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "What?"
        
def cthulhu_room():
    print "You see the evil cthulhu"
    print "Do u flee or eat head"
    
    next = raw_input("> ")
    
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty")
    else:
        cthulhu_room()
    
def dead(why):
    print why, "Good Job!"
    exit(0)

def start():
    print "You are in a dark room"
    print "Theres a door to ur right and left"
    print "Which one do u take?"
    
    next = raw_input("> ")
    
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("Stumble arounf until u starve")
    
start()