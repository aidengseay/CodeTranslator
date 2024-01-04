################################################################################
# CODE TRANSLATOR - ENCODE
# ========================
# This file consists of all the encoding operations
# Created by: Aiden Seay and Stef Storms, Winter '24
################################################################################
# IMPORTS
import math
import random
import string

################################################################################
# CONSTANTS
NULL = '0'
SPACE = " "
ASCII = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
         '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';',
         '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
         'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
         'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b','c', 'd', 'e',
         'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
         't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
ASCII_LEN = 95


################################################################################
# ENCODE FUNCTION
def encode(data):
    
    inputSize = countCharacters(data)
    sideSize = findOptimalGridSize(inputSize)
    diagArr = diagonalize(data,sideSize)

    encodedData = readDiagonalArray(diagArr)

    sizeKey, amount, frequency = generateKey(inputSize)

    print(F"Message: {encodedData}")
    print(f"Size Key: {sizeKey}")
    print(f"shift amount: {amount}")
    print(f"shift frequency: {frequency}")

    encodedData = shiftValues(amount, frequency)

    encodedData = insertKey(sizeKey, encodedData)

################################################################################
# SUPPORTING FUNCTIONS

def countCharacters( dataIn ):

    charCounter = 0

    for word in dataIn:
        for character in word:
            charCounter += 1

    charCounter += ( len( dataIn ) - 1 )
    return charCounter



def diagonalize( dataIn, sideSize ):

    diagonalArr = initializeDiagonalArray( sideSize )
    rowStart = 0
    colStart = 0
    rowIndex = 0
    colIndex = 0
    characters = 0

    for word in dataIn:
        for character in word:
            characters += 1
            diagonalArr[rowIndex][colIndex] = character
            rowIndex, colIndex, rowStart, colStart = (
                            incrementDiagonalArray(sideSize, rowIndex, 
                                                  colIndex, rowStart, colStart))
            
        diagonalArr[rowIndex] [colIndex] = SPACE
        characters += 1

        rowIndex, colIndex, rowStart, colStart = (
                            incrementDiagonalArray(sideSize, rowIndex, 
                                                  colIndex, rowStart, colStart))
    return diagonalArr



def findOptimalGridSize(characters):
    
    return math.ceil(math.sqrt( characters))



def generateKey(size):

    shift = size % ASCII_LEN

    if( shift % 2 == 0):
        whereShift = 2
    else:
        whereShift = 4

    sizeCode = str(hex(size))[2:]

    return sizeCode, shift, whereShift




def incrementDiagonalArray(sideSize, rowIndex, colIndex, rowStart, colStart):

    rowIndex -= 1
    colIndex += 1

    if(rowIndex < 0 and rowStart < sideSize - 1):
        rowStart += 1
        rowIndex = rowStart
        colIndex = 0

    elif(colIndex == sideSize):
        colStart += 1 
        colIndex = colStart
        rowIndex = sideSize - 1

    return rowIndex, colIndex, rowStart, colStart



def initializeDiagonalArray(sideSize):
    
    characters = string.ascii_letters + string.digits
    rows = sideSize
    cols = sideSize
    return [[random.choice(characters) for x in range(cols)]
                                                           for y in range(rows)]


def insertKey(sizeKey, encodedData):
    ...



def readDiagonalArray(array):
    
    output = ""
    for row in array:
        for column in row:
            output += column
    return output



def shiftValues(amount, frequency):
    ...



################################################################################