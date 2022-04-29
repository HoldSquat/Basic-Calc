# Created by HoldSquat @ github; L. Mercado
# A simple Python Calculator for computing two numbers

#importing csv to be able to write/read files

import csv

#Creating class for program

class function:
    def __init__(self, firstNumberFloat, secondNumberFloat, resDictionary):
        self.firstNumberFloat = firstNumberFloat
        self.secondNumberFloat = secondNumberFloat
        self.resDictionary = resDictionary
    
    def Sum(self):
        total = self.firstNumberFloat + self.secondNumberFloat
        print("////////////Heres your results!!!//////////")
        print("The result of", self.firstNumberFloat, '+', self.secondNumberFloat, "=",total)
        print()
        print("Lets go again!")

    def Sub(self):
        totalSub = self.firstNumberFloat - self.secondNumberFloat
        print("////////////Heres your results!!!//////////")
        print("The result of", self.firstNumberFloat, '-', self.secondNumberFloat, "=",totalSub)
        print()
        print("Lets go again!")

    def Multi(self):
        totalMulti = self.firstNumberFloat * self.secondNumberFloat
        print("////////////Heres your results!!!//////////")
        print("The result of", self.firstNumberFloat, '*', self.secondNumberFloat, "=",totalMulti)
        print()
        print("Lets go again!")

#Using divideError and if statments to check for errors 0=no error
    def Divide(self):
        try:
            totalDivide = self.firstNumberFloat/self.secondNumberFloat
            print("////////////Heres your results!!!//////////")
            print("The result of", self.firstNumberFloat, '/', self.secondNumberFloat, "=", totalDivide)
            print()
            print("Lets go again!")
        except(ZeroDivisionError):
            print("The result of", self.firstNumberFloat, '/', self.secondNumberFloat, "=", "Can't divide by zero!")
            print()
            print("Lets go again!")

    def allOpt(self):
        print("////////////Heres your results!!!//////////")
        print()
        print(self.firstNumberFloat, "+",self.secondNumberFloat, "=",self.resDictionary['Add'])
        print(self.firstNumberFloat, "-",self.secondNumberFloat, "=",self.resDictionary['Sub'])
        print(self.firstNumberFloat, "*",self.secondNumberFloat, "=",self.resDictionary['Multi'])
        print(self.firstNumberFloat, "/",self.secondNumberFloat, "=",self.resDictionary['Divide'])
        print()
        print(self.resDictionary)
        print()
        print("Lets go again!")

    def writeFile(self):
        with open("written_file.txt","w") as outFile:
            allOut = str(self.resDictionary)
            outFile.write(allOut)
        outFile.close()
        print("written_file.txt created!")

        
    def scalc(p1):
        scalc2 = p1.split(",")
        print(scalc2)
        firstNumberFloat = float(scalc2[0])
        secondNumberFloat = float(scalc2[1])
        if scalc2[2] == "+":
            print(firstNumberFloat + secondNumberFloat)
        if scalc2[2] == "-":
            print(firstNumberFloat - secondNumberFloat)
        if scalc2[2] == "*":
            print(firstNumberFloat * secondNumberFloat)
        if scalc2[2] == "/":
            try:
                print(firstNumberFloat / secondNumberFloat)
            except(ZeroDivisionError):
                print("Cannot divide by zero!")

            
