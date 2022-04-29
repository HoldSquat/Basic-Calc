
# Created by HoldSquat @ github; L. Mercado
# A simple Python Calculator for computing two numbers

#Importing classes

from mylib2 import *

#Menu list to choose options from
menuList = ['1) Add two numbers',
            '2) Substiute two numbers',
            '3) Divide two numbers',
            '4) Multiply two numbers',
            '5) All of the above',
            '6) Scalc',
            '7) Write to file',
            '8) Read from a file',
            '9) Restart']

loop = "yes"
option = 0

#Creating list to turn into a dictionary later
res = ["Add","Sub","Multi","Divide"]

while loop == "yes":
    print("Hey! Lets add, subtract, multiplay or divide some numbers!")
    print()
    print("Please enter your numbers!")
    
    try:
        firstNumber = input("Enter your first number please:")
        firstNumberFloat = float(firstNumber)

        secondNumber = input("Enter your second number please:")
        secondNumberFloat = float(secondNumber)

#listing results
        result = [firstNumberFloat + secondNumberFloat,
                  firstNumberFloat - secondNumberFloat,
                  firstNumberFloat * secondNumberFloat,
                  firstNumberFloat/secondNumberFloat]

#creating dictionary by zipping together the res and result list
        resDictionary = dict(zip(res,result))

#Delete Hash below to test dictionary creation
#        print(resDictionary)
        
        for n in menuList:
            print(n)
            print()
        print("Ok we have", firstNumberFloat,"and", secondNumberFloat)
        print("What would you like to do with the two numbers?")

        option = int(input("Pick from 1-9:"))

        while option != 0:
            if option == 1:
                A1 = function(firstNumberFloat, secondNumberFloat, resDictionary)
                A1.Sum()
                option = int(input("Pick from 1-9:"))
                
            elif option == 2:
                S1 = function(firstNumberFloat, secondNumberFloat, resDictionary)
                S1.Sub()
                option = int(input("Pick from 1-9:"))
                
            elif option == 3:
                D1 = function(firstNumberFloat, secondNumberFloat, resDictionary)
                D1.Divide()
                option = int(input("Pick from 1-9:"))
                
            elif option == 4:
                M1 = function(firstNumberFloat, secondNumberFloat, resDictionary)
                M1.Multi()
                option = int(input("Pick from 1-9:"))
              
            elif option == 5:
                All = function(firstNumberFloat, secondNumberFloat, resDictionary)
                All.allOpt()
                option = int(input("Pick from 1-9:"))
                
            elif option == 6:
                print("Running scalc now!!!!")
                print()
                p1 = input("Enter two numbers and an operator, each separated by a comma: ")
                function.scalc(p1)
                print("Now let's go back to the beginning!")
                option = 0

            elif option == 7:
                writeF = function(firstNumberFloat, secondNumberFloat, resDictionary)
                writeF.writeFile()
                print()
                print("Lets go again!")
                option = int(input("Pick from 1-9:"))

            elif option == 8:
                try:
                    readf = open("written_file.txt","r")
                    for x in readf:
                        print(x)
                    readf.close()
                    print()
                    print("End of file!!!")
                    print()
                except(FileNotFoundError):
                    print()
                    print("File Not Found!!!")
                    print("Restarting Now!!!")
                    print()
                
                option = int(input("Pick from 1-9:"))
                
            elif option == 9:
                print("restarting now!!!")
                option = 0 
                
            elif option <= 10:
                print()
                print("/////////Not a valid option/////////")
                print()
                option = 0

            elif option >= 0:
                print()
                print("/////////Not a valid option/////////")
                print()
                option = 0

    except(ValueError, NameError):
        print()
        print("//////////Input Numbers only!!!!////////////")
        print()
        print("Restarting program now!")
        print()  
#encase of a ZeroDivisionError                
    except(ZeroDivisionError):
        print("Can't divide by zero")
        
loop = (input("Would you like to run this program again? (yes or no)"))
if loop == "yes":
    loop = "yes"
    print("Alright! Starting form the beginning!")
elif loop == "no":
    print("////////////////////////")
    print("Terminating program now!")
    print("\\\\\\\\\\\\\\\\\\\\\\\\")
    
#Just using a print line to give a space
print()
print("Thanks for using my calculator! Have an awesome day!")
