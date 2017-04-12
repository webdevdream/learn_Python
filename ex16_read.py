from sys import argv
script, filename = argv

print ("The following is file contents:")
target = open(filename)
contents = target.read()
print (contents)
target.close()
