yearAge = int(input("Enter your age or year of birth: "))
isAge = False
isYear = False

if len(str(yearAge)) == 4:
    isYear = True

else:
    isAge = True

if(yearAge < 1900 and isYear):
    print("You seem to be oldest person alive")
    exit()

if(yearAge > 2020):
    print("You are not yet born")

if isAge:
    yearAge = 2020 - yearAge
print(f"you wil be 100 years in {yearAge + 100}")
interestedYear = int(input("Enter year you want to know your age: "))
print(f"You will be {interestedYear - yearAge} yrs old in {interestedYear}")
