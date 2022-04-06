def classes():
    #BMI Scale
    if (bmi<18.6):
        print()

        print("Underweight")

        print()

        print("Please increase weight")

    elif (bmi>18.6 and bmi<=24.9):
        print()

        print("Healthy")

        print()

        print("Please maintain weight")

    elif (bmi>25 and bmi<=29.9):
        print()

        print("Overweight")

        print()

        print("Please reduce weight")

    elif (bmi>30 and bmi <=34.9):
        print()

        print("Obese class I")

        print()

        print("Please reduce weight")

    elif (bmi>35 and bmi <=35.9):
        print()

        print("Obese class II")

        print()

        print("Please reduce weight")

    else:
        print()

        print("Not in range")

        print()
    return

while True:
    
    print()
    name = input("Enter your name:")

    print()
    weight = float(input("Enter your weight (in kgs):"))

    print()
    height = float(input("Enter your height (in meters):"))

    #BMI Calculation
    print()
    bmi = weight / (height*height)
    bmi = round(bmi, 2) #Rounds up the calculation to 2 decimal place
    print(name + ", your BMI is", bmi)
    
    classes()

    #Allows User to calculate again if they choose to do so
    print()
    print("Would you like to calculate again? y/n")
    data = input()
    if str.lower(data) == 'n':
        break


