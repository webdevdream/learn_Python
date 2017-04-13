from sys import exit

# The temple function
def temple():
    print ("""You're inside the treasure room,
    The room is full of treasure chests,
    Too many chests, maybe over a 1000 chests
    How many you will take?""")

    choice = int(input("> "))

    if 0 < choice <= 10:
        print ("You will be able to take them out\nbefore the temple collapses,\nYou win!")
        exit(0)

    else:
        dead("Too greedy, the temple collapsed over your head.")

# The mountain function with 2 choices for the user.
def mountain():
    print ("""You're now in the great witch mountains area.
    You see high mountains with wide valleys in between.
    What you will do?
    climp a mountain, walk through a valley or doing something else?\n""")

    choice = input("> ").upper() # to collect user input and make it uppercase.

    if "CLIMP" in choice:
        dead("The great witch tranform you into a frog.") # print if word "climp" is in user input

    elif "WALK" in choice:
        print("Walk has no end, you returned to the same start point.") # print if word "walk" is in user input
        start() # if user input contains word "walk", he will sent back to the start.

    else:
        print ("You need to take a better decision.\n") # print if user took any other choice.
        mountain() # if user took a choice other than walk or climp, mountain function runs again.

# The stream function with 3 choices or back to start.
def stream():
    print ("""You're in front off a fast chilling water stream.
    What is your decision? Swim, use Kayak or passing the lettle far bridge.""")

    choice = input("> ").upper() # to collect user input and make it uppercase.

    if "SWIM" in choice:
        dead("Ice cold water, you're shaking beyond control.") # print if user iput contains the word swim.

    elif "KAYAK" in choice:
        dead("Water is too fast, you hit the rocks.") # print if user input contains the word kayak.

    elif "BRIDGE" in choice:
        print ("You suddenly find yourself in the jungle route.") # print if user input contains the word bridge.
        jungle() # call jungle function.

    else:
        print ("You better fishing next time.") # print if user made any other choice.
        start() # call start function to restart the game.

# The tiger function
bag_items = ["Knife", "Compass", "Dried meat", "rop", "ligher"]

def tiger():
    print ("That wasn't the safest choice, entrance door is closing behind you and you're facing a big tiger blocking jungle route.")
    print ("What you'll do? try running to bypass the tiger\nor check your bag for other idea.")

    choice = input("> ").upper()

    if "BAG" in choice:
        bag()

    else:
        dead("The tiger tears your head off.")

def bag():
    print ("Items in the bag:\n")
    items_count = len(bag_items)
    for i in range(0, items_count):
        print ("\t", i+1, "- ", bag_items[i])

    selected_item = input("What are You gone to use?> ").upper()

    if "KNIFE" in selected_item:
        dead("You couldn't kill the tiger with a knife.")

    elif "COMPASS" in selected_item:
        dead("Are you kidding? What the hell are you going to do with the comapss?!!")

    elif "DRIED MEAT" in selected_item:
        print ("The tiger moved, the intrance of jungle route is clear, hurry up.")
        jungle_route()

    elif "ROP" in selected_item:
        dead("You couldn't tie the big tiger with the rop.")

    elif "LIGHTER" in selected_item:
        dead("You can't scare a thiger with a lighter.")
    else:
        print ("You don't have this item in the bag, please select an item from the bag.")
        bag()

def dead(why):
    print (why, "Happy stroll.")
    exit(0)

def jungle_route():
    print ("You succeeded to pass the tiger safely, you're now in the 'Jungle route'.")
    print ("Nice place, lot of exotic birds and baboons, keep going.")

    choice = input("You reached the 'Golden Temple', will you go inside?").upper()

    if "YES" in choice:
        print ("Great decision.")
        temple()

    else:
        print ("That was a strange decision.")
        exit(0)

def jungle():
    print ("\nNice place, lot of exotic birds and baboons, keep going.")

    choice = input("You reached the 'Golden Temple', will you go inside?").upper()

    if "YES" in choice:
        print ("Great decision.")
        temple()

    else:
        print ("That was a strange decision.")
        exit(0)

def start():
    print ("START THE ADVENTURE")
    print ("\nTo start the adventure choose which direction to go, right, left or forward.\n")

    choice = input ("> ").upper()

    if "RIGHT" in choice:
        tiger()

    elif "LEFT" in choice:
        stream()

    elif "FORWARD" in choice:
        mountain()

    else:
        print ("That's not an option.")
        start()


# ------ to be removed ---------
# temple()
# mountain()
# stream()
# tiger()
# bag()
start()
# ------------------------------
