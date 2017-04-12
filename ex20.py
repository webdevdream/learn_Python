from sys import argv
# Following variables need to be given when running the file "ex20.py"
# script is the name of the file, input_file is another variable we will use.
script, input_file = argv
# Function to read file and print all it's contents
def print_all(f):
    print (f.read())
# Function to go to the begining of file.
def rewind(f):
    f.seek(0)
# Function to print a line from a file.
def print_a_line(line_count, f):
    print (line_count, f.readline())
# Opining the file that we select as input_file
current_file = open(input_file)

print ("First let's print the whole file:\n")
# calling print_all function.
print_all(current_file)

print ("Now let's rewind, kind of like a tape.")
# calling rewind function
rewind(current_file)

print ("let's print three lines.\n")
# Selecting 1 as a value for current_line to print line 1, and Calling "running" print_a_line function
current_line = 1
print_a_line(current_line, current_file)
# incrementing current_line value by 1 to print line 2
current_line += 1
print_a_line(current_line, current_file)
# incrementing current_line value by 1 to print line 3
current_line += 1
print_a_line(current_line, current_file)
