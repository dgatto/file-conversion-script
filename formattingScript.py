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
