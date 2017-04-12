# This one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print ("arg1: %r, arg2: %r" % (arg1, arg2))

# ok, That *args is actually pointless, we can just do This
def print_two_again(arg1, arg2):
    print ("arg1: %r, arg2: %r" % (arg1, arg2))

# This just take one argument

def print_one(arg1):
    print ("arg1: %r" % arg1)

# This one takes no argument

def print_none():
    print ("I got nothing.")

print_two("Ghada", "Omar")
print_two_again("Sara", "Haidi")
print_one("Abdelhamid")
print_none()
