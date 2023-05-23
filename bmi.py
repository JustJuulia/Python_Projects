try:
    weight = float(input("Your weight in kilograms: "))
    height = float(input("Your height in meters: "))
    BMI = weight / (height * height)
    norm = " "
    if(BMI < 18.5):
        norm = "underweight"
    elif (BMI <= 24.9):
        norm = "normal"
    elif (BMI <= 30):
        norm = "overweight"
    elif (BMI <= 34.9):
        norm = "obese"
    elif (BMI >= 35):
        norm = "extremely obese"

    print("Your BMI: ", round(BMI, 2), " ", norm)
except ZeroDivisionError:
    print("your height cannot be 0")
except ValueError:
    print("float not something else")
except Exception as e:
    print(e)
