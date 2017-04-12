# Import argv module from sys.
from sys import argv
# Specify the argv unpack variables
script, filename = argv
# Assign txt variable to open the file that have been choosed.
txt = open(filename)
# Print the file name.
print ("Here is your file %r:" % filename)
# Print the contents of the file.
print (txt.read())
txt.close()

## Ask user to type the file name again.
#print ("Type the file name again:")
## Prompt the usert to enter the file name after > .
#file_again = input("> ")
#
## open the file again.
#txt_again = open(file_again)
#
## Print file contents again.
#print (txt_again.read())
