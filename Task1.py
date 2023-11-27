#Function for logic
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

while True:
    year = int(input("Enter a year (enter 0 to exit): "))#input from the user
    
    if year == 0:
        print("Goodbye!")# Check if the user wants to exit
        break

    # Check if it's a leap year and print the result
    if leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
