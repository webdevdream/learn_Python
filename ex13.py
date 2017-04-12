#from sys import argv
#script, first, second, third = argv
#print ("This script is called:", script)
#print ("Your first variable is:", first)
#print ("Your second variable is:", second)
#print ("Your third variable is:", third)

from sys import argv
script, variety, grade = argv
print ("Variety: ", variety)
print ("Grade: ", grade)
season = input("Which season we will talk about?")
qty = input ("What is the production quantity of %r, grade %r?:" % (variety, grade))
print ("So your Palms are old enough to reach %r per season, that's wonderful!" % qty)
