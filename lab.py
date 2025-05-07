def main():
    calculate_bmi(weight=57, height=1.73)
    pass
def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height**2)
    print("BMI = " + str(bmi))
    if bmi < 18.5:
        print("Underweight!")
    elif bmi >= 18.5 and bmi <= 25:
        print("Normal Weight!")
    else:
        print("Overweight!")

if __name__ == "__main__":
    main()