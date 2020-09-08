# your age in 2020
#
# Take age or year as input from user and tell them when will they be 100 years old !!(5)
# Dont use any module (-5)
# They can then optionally provide a year and program must tell their age in that particular year.(3)
# you should be handling all type of errors (2)
# --> You are not yet born
# --> you seem to be oldest person alive
# --> any other errors if possible

age_year = input("Enter your age or year of birth: ")
if len(age_year) == 2 or len(age_year) == 3:
    age = age_year
    print(f"The age is {age}")
else:
    year_of_birth = age_year
    print(f"The year of birth is {year_of_birth}")

def age_in_2020(year_of_birth):
    # print("your age in 2020 : ")
    # I have choosed the max age to be 120 !!
    age_2020 = 2020 - int(year_of_birth)
    if int(age_2020) < 0:
        print("you are not yet born")
    elif int(age_2020) > 120:
        print("Death Point !! No more in the world !! ")
    else:
        print(age_2020)

current_age = age_year
def age100(current_age):
    print("You will be 100 years after: ")
    age_100 = 100 - int(current_age)
    print(age_100)

if len(age_year) == 4:
    age_in_2020(year_of_birth)
else:
    age100(age)

print("Would you like to calculate age of anyone \n Enter the birth year: ")
year = int(input())
result = 2020 - int(year)
if result < 0 or result > 120:
    print("Invalid year input")
else:
    print("Age is ",result)
