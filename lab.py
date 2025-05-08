def main():
    calculate_bmi(weight=57, height=1.73)
    display_main_menu()
    arr = get_user_input()
    print("Min and Max: ", find_min_max(arr))
    print("Average:", calc_average(arr))
    print("Median", calc_median_temperature(arr))
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
def display_main_menu():
    print("Enter some numbers seperated by commas (e.g. 5, 67, 32)")
def get_user_input() -> list[float]:
    data = input()
    arr = data.split(",")
    for i in range(len(arr)):
        arr[i] = float(arr[i])
    return arr
def calc_average(arr: list[float]) -> float:
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total / len(arr)
def find_min_max(arr: list[float]):
    return [min(arr), max(arr)]
def sort_temperature(arr: list[float]):
    arr.sort()
    aaa = arr[:]
    return aaa
def calc_median_temperature(arr: list[float]):
    temperatures = sort_temperature(arr)
    if len(temperatures) % 2 == 0:
        a, b = temperatures[len(temperatures)//2], temperatures[len(temperatures)//2 + 1]
        return (a+b) / 2
    else:
        return temperatures[len(temperatures)//2]
if __name__ == "__main__":
    main()