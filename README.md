# file-conversion-script
# Data File Customization Script for BioChemistry Department at the University of North Carolina at Greensboro

# README

The purpose of this script is to solve an issue where conventional text editors (Word, Notepad, even Excel) force the user to
save an '.msp' file as a text-only file. This causes errors with LipiDex. This script simply allows the user to find and
replace any and *all* given instances of a phrase in a file of their choosing, but doesn't save the file as text-only.

NOTE: If you'd rather not use this script, there IS a text editor that allows you to edit the files without complaining about text-only conversion. It's called Atom, you can download it [here](https://atom.io/)!

## _Installation_

1. Download this repository so you have the script on your computer. You can do that by clicking "Clone or Download" at the top of this page and downloading the ZIP file.
2. Install Python 3.7+. [here's the link!](https://www.python.org/downloads/)
3. Install Anaconda 5.3+. This is necessary for installing the Pandas package. [here's another link!](https://www.anaconda.com/download/#windows)
4. Install the Pandas package for python. You should be able to open a Python shell by going to the Start Menu and searching "Python". After the shell opens, type `conda install pandas`. 

Now you should be good to run the script!

## _Running_

1. Navigate to where you installed the script
2. Double click on it. A python shell should open up. This shell will prompt you through editing the file.
3. First you input the name of the file.
4. Next it will ask which option you would like to do. The only current option is 'Replace', but this gives the opprotunity to modify the script for more options in the future. Type `Replace` in the console.
5. Next it will ask which phrase you're finding, and what you're replacing it with. You input them separated by commas, like this: `phrase_to_find,phrase_to_replace_with`. You can do multiple replaces by separating by semicolons.
For example: `Name,ID;PrecursorMZ,Precursor`
6. After typing in your find/replace, the script will tell you it has written the file, and will give you an option to either replace again, or exit the program by typing "Ctrl+C".
