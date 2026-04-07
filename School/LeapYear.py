#This script checks to see if a year you inputed is a leap year or not

def leap(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")


leap(int(input("Enter a year: ")))
