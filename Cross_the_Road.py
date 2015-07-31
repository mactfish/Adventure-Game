import random




print("Welcome to Cross the Road game!!!")

while 1:
    player=raw_input("What is your name? ")
    if player=="Satan":
        print("GOD HAS STRUCK YOU DOWN!")
        exit (0)
    if player=="Jesus":
        print("HALLELUJAH! HALLELUJAH!")
        break
    if player=="God":
        print("PPPPPFFFFFF! REALLY?! NAW! What is your REAL name?")
    else:
        break

print("Hi %s, thanks for playing!" % player)
gender="neither"
while not (gender=="boy" or gender=="girl" or gender=="alien" or gender=="gurl" or gender=="boi"):
    gender=raw_input("%s, are you a boy or a girl? " % player)
    if gender=="alien":
        print("WHOA! REALLY! OMG! THAT IS SO CRAZY!")
    if gender=="gurl":
        print("Ha! u SpEl BaD!")
    if gender=="boi":
        print("Ha! u SpEl BaD!")
print("Type 'help' for help, type 'bye' to quit.")
print("Have fun %s!" % player)

def yard(x,y,action):
    global can_mow
    if action=="help":
        print("ACTIONS: play, mow the lawn")
    if action=="play":
        print("You had loads of fun!")
        can_mow=can_mow+0.1
    if action=="mow the lawn":
        if can_mow > 0.9:
            print("Your mower blades spin around, cutting up all the helpless life forms below you... now your lawn is perfect!")
            can_mow=can_mow-1
        else:
            print("You already mowed the lawn, silly %s!" % player)
    return 1

def deck(x,y,action):
    global can_mow
    if action=="help":
	    print("ACTIONS: relax")
    if action=="relax":
        print("You relaxed dude.")
        can_mow=can_mow+0.1
        if gender=="alien":
            print("OMG IT'S A SPACESHIP COMING TO TAKE YOU HOME! BYE!")
            return 0
        return 1

def bathroom(x,y,action):
    global can_mow
    global can_pee
    global can_poop
    global can_eat
    if action=="help":
	    print("ACTIONS: pee, poop, shower")
    if action=="pee":
        if can_pee > 0:
            print("You got relief.")
            can_mow=can_mow+0.1
            can_pee=can_pee-1
        else:
            print("Nobody's bladder is that big!")
    	  	
    if action=="poop":
        if can_poop > 0:
            ill=random.randint(1,100)
            if ill < 20:
                print("Diarrhea cha cha cha! Diarrhea cha cha cha!")
                can_mow=can_mow+0.1
                can_eat=can_eat+1
                can_poop=can_poop-1
                can_pee=can_pee-1
                return 1
            elif ill < 40:
                print("PPPLLLRRRBBBRRRTTT")
            elif ill > 99:
                print("You mad such a massive poop that you, and everyone else on Earth suffocated in the giant brown blob.")
                return 0
            elif ill > 40:
                print("You crapped a ton.")
                can_eat=can_eat+1
                can_poop=can_poop-1
        else:
            print("You tried so hard, and got so far! But in the end, you couldn't even pooooooooop!")

    if action=="shower":
        print("You are very clean now and there is a big dirt ring around the tub!")
        can_mow=can_mow+0.1
    return 1

def kitchen(x,y,action):
    if action=="help":
	    print("ACTIONS: make food")
    if action=="make food":
        print("You cut off your hand and bled out.")
        return 0
    return 1

def dining(x,y,action):
    global can_mow
    global can_pee
    global can_poop
    global can_eat
    if action=="help":
	    print("ACTIONS: eat, drink")
    if action=="eat":
        if can_eat > 0:
            print("Yum!")
            can_mow=can_mow+0.1
            can_poop=can_poop+1
            can_eat=can_eat-1
        else:
            print("You ate so much that you went KABOOM!")
            return 0
    if action=="drink":
        print("Your thirst is satisfied.")
        can_mow=can_mow+0.1
        can_pee=can_pee+1
    return 1

def hall(x,y,action):
    if action=="help":
	    print("ACTIONS: none")
    return 1

def study(x,y,action):
    if action=="help":
        print("ACTIONS: study")
    if action=="study":
	    print("YOU HAVE BEEN ENLIGHTENED!!!YOU WIN %s!!!" % player)
	    return 0
    return 1

def room(x,y,action):
    global can_mow
    if action=="help":
        print("ACTIONS: watch tv")
    if action=="watch tv":
	    print("You watched cool shows!")
	    can_mow=can_mow+0.1
    return 1

def trash(x,y,action):
    global can_mow
    if action=="help":
	    print("ACTIONS: jump in, sniff")
    if action=="jump in":
        print("You were carried by a garbage truck and incinerated in the dump. How stupid are you %s!" % player)
        return 0
    if action=="sniff":
        print("Smells like a mountain breeze!(Not!)")
        can_mow=can_mow+0.1
    return 1

def forest(x,y,action):
    if action=="help":
	    print("ACTIONS: plant a tree, burn")
    if action=="plant a tree":
        print("YOU SAVED EARTH FROM THE APOCALYPSE! YOU WIN %s!!!" %player)
        return 0
    if action=="burn":
        print("EVERYONE DIED! WHAT THE HECK!")
        return 0

def chair(x,y,action):
    if action=="help":
	    print("ACTIONS: sit down")
    if action=="sit down":
        print("The chair has granted you magic powers and you are now %s, god of everything!" % player)
        return 0

def oyard(x,y,action):
    if action=="help":
        print("ACTIONS: climb a tree")
    if action=="climb a tree":
        print("You climbed to the top and now you can see the whole world!")
        return 1
        
def scary(x,y,action):
    if action=="help":
        print("ACTIONS: look around")
    if action=="look around":
        print("AAAAAAAHHHHHHH! YOU WERE KILLED BY JASON, FREDDY KREUGER, AND SAW AT THE SAME TIME!")
        return 0
        
def dry(x,y,action):
    global can_eat
    if action=="help":
        print("ACTIONS: die slowly, dig, eat a camel")
    if action=="die slowly":
        print("You slowly died of thirst")
        return 0
    if action=="dig":
        print("You found gold and stuff! You could get big bucks for this!")
    if action=="eat a camel":
        if can_eat > 0:
            print("NOM NOM NOM NOM")
            can_eat=can_eat-8
        else:
            print("You ate so much that you went KABOOM!")
            return 0
    return 1
    
def wet(x,y,action):
    if action=="help":
        print("ACTIONS: PARTY!")
    if action=="PARTY!":
        print("YOU PARTIED SO MUCH!")
    return 1
            




world = [
  [["yard", yard],         ["yard", yard],       ["deck", deck]],
  [["bathroom", bathroom], ["kitchen", kitchen], ["dining room", dining]],
  [["hallway", hall],      ["hallway", hall],    ["hallway", hall]],
  [["study", study],       ["hallway", hall],    ["living room", room]],
  [["trash can", trash],   ["forest", forest],   ["chair", chair]],
  [["backyard", oyard],    ["backyard", oyard],  ["backyard", oyard]],
  [["SCARY BASEMENT", scary], ["desert", dry],   ["oasis", wet]]
]

max_y=len(world)
max_x=len(world[0])

print("World dimensions are: %d/%d" % (max_x, max_y))

position_x=0
position_y=0

can_mow=1
can_pee=5
can_poop=5
can_eat=10

while 1:
	print("You are currently in %s at position %d/%d" % (world[position_y][position_x][0], position_y, position_x))
	action=raw_input("Move (forward, backward, right, left)? ")
	if action == "forward":
		position_y=position_y-1
		if position_y == -1:
			print("YOU CAN NOT GO HERE!!!")
			position_y=position_y+1
		continue
	if action == "backward":
		position_y=position_y+1
		if position_y == max_y:
			print("YOU CAN NOT GO HERE!!!")
			position_y=position_y-1
		continue
	if action == "left":
		position_x=position_x-1
		if position_x == -1:
			print("YOU CAN NOT GO HERE!!!")
			position_x=position_x+1
		continue
	if action == "right":
		position_x=position_x+1
		if position_x == max_x:
			print("YOU CAN NOT GO HERE!!!")
			position_x=position_x-1
		continue
	if action == "bye":
		break
	if world[position_y][position_x][1](position_x,position_y,action)==0:
		break	
		
