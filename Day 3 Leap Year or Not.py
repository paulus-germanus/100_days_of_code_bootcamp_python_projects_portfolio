def is_leap(year):
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        print(f"{year} is a leap year")
    elif year % 4 == 0 and year % 100 == 0:
        print(f"{year} is NOT a leap year")
    elif year % 4 == 0:
        print(f"{year} is a leap year")

print(is_leap(int(input("Enter a year to check if it's (was) a leap year.\n"))))