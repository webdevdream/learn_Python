name = 'Abdelhamid Shokrof'
age = 42 # getting old
height_cm = 185 # cm
height_in = height_cm * 0.39 # inch
weight_kg = 83 # kg
weight_po = weight_kg * 2.20462 # pounds
eys = 'Light Brown'
teeth = 'White'
hair = 'Black'

print ("Let's talk about %s." % name)
print ("He is %d cm tall, that equals to %d inches." % (height_cm, height_in))
print ("He is %d kg heavy, that equals to %d pounds." % (weight_kg, weight_po))
print ("Actually that's not heavy.")
print ("He's got %s eyes and %s hair." % (eys, hair))
print ("His teeth is usually %s depending on the coffee." % teeth)
# this line is tricky, try to get it exactly right
print ("If I add %d, %d and %d I get %d." % (age, height_cm, weight_kg, age + height_cm + weight_kg))
