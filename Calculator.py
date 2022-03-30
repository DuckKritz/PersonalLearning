import math

calculatelist = []

operation = ["1.Add","2.Subtract","3.Multiply","4.Divide","5.Square","6.Squareroot","7.Replay"]

def op():
    print("Select operation.")
    print(operation[0])
    print(operation[1])
    print(operation[2])
    print(operation[3])
    print(operation[-3])
    print(operation[-2])
    print(operation[-1])
    print()
    
#Main Programme for Addition
def choice1():
    first_no = float(input("Enter first number:"))
    print()
    second_no = float(input("Enter second number:"))
    addition = first_no + second_no 
    Add = (str(first_no) + " + " + str(second_no) + " = " + str(addition))
    print(first_no,"+", second_no, "=",addition)#Shows full equation and answer
    calculatelist.append(Add)#Puts in the equation and answer into the list
    print()
    op()
    
#Main Programme for Subtract
def choice2():
    first_no = float(input("Enter first number:"))
    print()
    second_no = float(input("Enter second number:"))
    subtraction = first_no - second_no
    Subtract = (str(first_no) + " - " + str(second_no) + " = " + str(subtraction))
    calculatelist.append(Subtract)#Puts in the equation and answer into the list
    print(first_no,"-", second_no, "=",subtraction)#Shows full equation and answer
    print()
    op()
    
#
def choice3():
    first_no = float(input("Enter first number:"))
    print()
    second_no = float(input("Enter second number:"))
    multiply = first_no * second_no
    Multiplication = (str(first_no) + " * " + str(second_no) + " = " + str(multiply))
    print(first_no,"*", second_no, "=", multiply)#Shows full equation and answer
    calculatelist.append(Multiplication)#Puts in the equation and answer into the list
    print()
    op()
    

def choice4():
    first_no = float(input("Enter numarator:"))
    print()
    second_no = float(input("Enter denominator:"))
    division = first_no/second_no
    Divide = (str(first_no) + " / " + str(second_no) + " = " + str(division))
    print(first_no,"/" ,second_no,"=", division)#Shows full equation and answer
    calculatelist.append(Divide)#Puts in the equation and answer into the list
    print()
    op()
    
def choice5():
    first_no = float(input("Enter a number:"))
    square = math.pow(first_no,2)
    Squared = ("Square of " + str(first_no) + " = " + str(square))
    print("Square of " + str(first_no) + " = " + str(square))#Shows full equation and answer
    calculatelist.append(Squared)#Puts in the equation and answer into the list
    print()
    op()

def choice6():
    first_no = float(input("Enter a number:"))
    print()
    squareroot = math.sqrt(first_no)
    Root = ("Square root of " + str(first_no) + " = " + str(squareroot))
    print("Square root of " + str(first_no) + " = " + str(squareroot))#Shows full equation and answer
    calculatelist.append(Root)#Puts in the equation and answer into the list
    print()
    op()
    
op()

#Main Programme
while True:
    
    choice = input("Enter choice(1/2/3/4/5/6/7):")
    
    if ((choice == 0) or (choice > "7")):
        print("reenter")
        print()

    elif (choice == "1"):
        print()
        choice1()
        
    elif (choice == "2"):
        print()
        choice2()
        
    elif (choice == "3"):
        print()
        choice3()


    elif (choice == "4"):
        print()
        choice4()
            
    elif (choice == "5"):
        print()
        choice5()
        
    elif (choice == "6"):
        choice6()
        print()

            
    elif (choice == "7"):
        for a in calculatelist:
            print(a)
        break