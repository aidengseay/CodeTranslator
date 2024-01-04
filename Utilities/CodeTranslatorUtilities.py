################################################################################
# CODE TRANSLATOR - UTILITIES
# ===========================
# This file consists of all the other supporting functions
# Created by: Aiden Seay and Stef Storms, Winter '24
################################################################################
# IMPORTS

################################################################################
# CONSTANTS
EXTENSION = -4
CORRECT_EXTENSION = ".txt"

################################################################################
# SUPPORTING FUNCTIONS

def getFileName():

    correctInput = False

    while not correctInput:

        fileName = input("File: ")

        if(fileName[EXTENSION:] != CORRECT_EXTENSION):
            print("Error: Must be .txt file")
        else:
            correctInput = True

    return fileName



def getOperation():

    correctInput = False

    print("Enter <E> for encode or <D> for decode.")

    while not correctInput:

        operation = input("Operation: ").upper()

        if( operation == 'D' ):
            correctInput = True

        elif( operation == 'E' ):
            correctInput = True

        else:
            print( "Unrecognized input, try again")

    return operation



def readFile( fileName ):
    
    dataIn = []

    with open( fileName, 'r' ) as file:

        for line in file:
            line = line.strip()
            words = line.split()  
            dataIn.extend( words )

    return dataIn



################################################################################