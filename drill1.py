from sys import exit

# crate the temple function
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

def mountain():
  print ("""You're now in the great witch mountains area.
  You see high mountains with wide valleys in between.
  What you will do?
  climp a mountain, walk through a valley or doing something else?\n""")

  choice = input("> ")

  if "climp" in choice:
    dead("The great witch tranform you into a frog.")

  elif "walk" in choice:
    print("Walk has no end.")
    # start()

  else:
    print ("You need to take a better decision.\n")
    mountain()

def stream():
  print ("""You're in front off a fast chilling water stream.
  What is your decision? Swim, use Kayak or passing the lettle far bridge.""")

  choice = input("> ").upper()

  if "SWIM" in choice:
    dead("Ice cold water, you're shaking beyond control.")

  elif "KAYAK" in choice:
    dead("Water is too fast, you hit the rocks.")

  elif "BRIDGE" in choice:
    print ("You suddenly find yourself in the golden route, you must see the temple any moment.")

  else:
    print ("You better fishing next time.")
    # start()


def dead(why):
  print (why, "Happy stroll.")

# temple()
# mountain()
stream()
