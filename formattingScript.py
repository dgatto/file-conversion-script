# Data File Customization Script for BioChemistry Department at the University of North Carolina at Greensboro
# Author: Donald Gatto

import pandas as pd
import numpy as np
import fileinput # for processing files
import re as regex # for finding patterns in strings
import datetime

now = datetime.datetime.now()

# Declare file name to open
input_file  = ''
output_file = ''

has_error = False

# Declare colors
class colors:
    pink      = '\033[95m'
    blue      = '\033[94m'
    green     = '\033[92m'
    yellow    = '\033[93m'
    red       = '\033[91m'
    endcolor  = '\033[0m'
    bold      = '\033[1m'
    underline = '\033[4m'

# Replace ALL instances of a certain phrase in the file with given input
def replaceString(replace_input, filedata):

	# Remove all spaces from the input and split the string by each comma into separate values
    if (type(replace_input) is str):
        pattern = ',|;'
        replace_input = regex.split(pattern, replace_input)

	# Check if there is a consistency in the matching pairs
    if (len(replace_input) % 2 != 0):
        print(colors.yellow + '\nWARNING:' + colors.endcolor + ' Mismatched lengths. Please try again.\n')
        main()
        return

	# If only two parameters given, we can move on with replacing the string
    if (len(replace_input) == 2):
        # Replace the target string
        filedata = filedata.replace(replace_input[0], replace_input[1])

	# If we have more than one thing to find and replace (i.e., we have more than 2 inputs),
	# we loop through every two elements in the input and replace the current element, and the associate it with the one in the
	# succeeding index
    else:
        chunkSize = 2
        for i in range(0, len(replace_input), chunkSize):
            filedata = filedata.replace(replace_input[i], replace_input[i + 1])

    # Write the file out again
    with open(output_file, 'w') as file:
        print('writing file...')
        file.write(filedata)

# "Hides" (really it removes) a given row of data for all instances of it. CANNOT BE UNDONE (so you're not getting that data back),
# but the script creates a new file, so you won't *really* lose any data
# def hideRow(row_to_hide):
# 	with open(input_file, 'r') as input:
# 		with open(output_file, 'w') as output:
# 			splitLength = len(row_to_hide)
# 			numberResults = 0
# 			# Check each line in the file to see if the row is the row we want to remove
# 			for line in input:
# 				# Cut the line at the length of our input
# 				if line[:splitLength] != row_to_hide:
# 					output.write(line) # If it is NOT the row we're looking to remove, then write the current line to the output file, essentially rebuilding the original file
# 				else:
# 					numberResults = numberResults + 1 # If it IS the row we're looking for, increase the counter so we know we've found some hits
# 			# If the counter is 0, that shows us there wasn't any results
# 			if (numberResults == 0):
# 				print('\n\n-----------------\n***ERROR: That pattern was not found in this file! Did you spell it correctly?***\n-----------------\n\n')
# 				main()

def getFileName():
    global input_file
    global output_file

    print("What is the name of the file you're reading from?")
    input_file = input('> ') # Take in user input for file name
    output_file = now.strftime("%Y-%m-%d") + input_file # Make output file the input_file's name + current date

    with open(input_file, 'r') as file:
        filedata = file.read()

# Main function of the script - takes users input of their formatting choices and figures out which functions to call for
# formatting the file.
def main():
    global input_file
    global output_file

    if (input_file == ''):
        getFileName()
    else:
        input_file = output_file

    print('What would you like to do?\n\nCurrent options are: [' + colors.underline + 'Replace' + colors.endcolor + '] ALL instances of a given phrase.\nExit program with "CTRL + C"\n')
    action = input('> ') # Take in the user's input

	# Remove all spaces from the input and split the string by each comma into separate values
    commands = action.replace(' ', '')
    commands = commands.split(',')

    with open(input_file, 'r') as file:
        filedata = file.read()

    # For each command given, decide which functions to call based on user's input
    for command in commands:
        if (command.lower() == 'replace'):
            replace = input('Input your find and replace in this format, please. Multiple searches can semicolon-separated. Example: [Name,ID;PrecursorMZ,Precursor].\n')
            replaceString(replace, filedata)
        elif (command.lower() == 'remove'):
            row_to_hide  = input('Which row of data would you like to remove?\n')
            hideRow(row_to_hide)
        else:
            print('User inputted ' + action)
            print('\n\nPossible invalid input. Try again. Ctrl + C to quit.\n')

    main()

main()
