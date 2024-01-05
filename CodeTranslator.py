################################################################################
# CODE TRANSLATOR
# ===============
# This program is used to encode and decode secret messages.
# Created by: Aiden Seay and Stef Storms, Winter '24
################################################################################
# IMPORTS
import Utilities.CodeTranslatorUtilities as CodeTranslatorUtilities
import Utilities.DecodeUtility as DecodeUtility
import Utilities.EncodeUtility as EncodeUtility
import os

################################################################################
# CONSTANTS
SUBDIRECTORY = "./"
ENCODE = "E"
DECODE = "D"

################################################################################
# MAIN FUNCTION
def main():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("CODE TRANSLATOR")
    print("===============\n")

    print("FILES IO")
    print("--------")
    print("Enter the .txt file used for input")
    #inputFile = CodeTranslatorUtilities.getFileName()
    inputFile = "miniTest.txt" # TEST
    print("\nEnter the .txt file used for output")
    #outputFile = CodeTranslatorUtilities.getFileName()
    outputFile = "out.txt" # TEST

    if(not os.path.exists( SUBDIRECTORY + inputFile)):
        print("\nInput file not detected: program aborted")
        return
    
    print("\nOPERATION")
    print("---------")
    dataInput = CodeTranslatorUtilities.readFile(inputFile)
    #operation = CodeTranslatorUtilities.getOperation()
    operation = "E" # TEST

    if(operation == ENCODE):
        EncodeUtility.encode(dataInput)
        print(f"\nEncoded results stored in {outputFile}")
    else:
        DecodeUtility.decode(dataInput)
        print(f"\nDecoded results stored in {outputFile}")

    

################################################################################
if __name__ == "__main__":
    main()