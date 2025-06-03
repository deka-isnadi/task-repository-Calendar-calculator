# to determine what day is a date

# data validation
def input_validation():
    while True:
        try :
            date = int(input(" Enter Date (1-31) : "))
            if date <1 or date >31:
                print("Date must between 1-31, please try again") 
                continue
            
            month = int(input("Input month (1-12) : "))     
            if month <1 or date > 12:
                print ("Month must between 1-12!")
                continue
            
            year = int(input("Input Year (YYYY): "))
            if year <1 :
                print("Year number must bigger or equal to 1 !")
                continue
            return date, month, year

        except ValueError:
            print("Date must in numbers, please try again!")

# askin Valid Input
print("Please enter Date :")
date, month, year = input_validation()
print("_________________________________________________")
print("_________________________________________________")
print(" Date or month are valid")

print(f"Your date are : {date} - {month} - {year}")

# Leap Year YYYY/4 = no excess,  but of multiply of 100, it is not Leap Year
# operator modulus

if( year % 4 == 0 and year %100 != 0) or (year % 400 == 0):
    print(f"Year of {year} is a Leap Year")
else:
    print(f"Year of {year} is NOT a Leap Year")

# Zeller Congruence
# Month and year adjusted according to Zeller Congruence
# January (1) + 12 = 13
if month == 1 or month == 2:
    month += 12
    year -= 1
# K dan J
# K = year % 100, cth 2025 --> 25 (tahun)
# J = year//100 --> 2025//100 = 20 (abad)

J = year // 100
K = year % 100
h = (date + ((13 * (month+1)) // 5) + (K) + (K // 4) + (J // 4) - (2 * J)) % 7

print(f" Month Number according to Zeller Congruence : {month}")
print(f" Century number  : {J} ")
print(f" Year number  : {K}")
print(f" Day Number {h} ")
print(f" Zeller Congruence formula h= ( {date} + {((13*(month + 1))//5)} + {K} + {K//4} + {J//4} - {2*J} ) mod 7 ")
if h==2:
    print(f"Your date according to Zeller Congruence: {date} - {month} - {year} is MONDAY" )
if h==3:
    print(f"Your date according to Zeller Congruence: {date} - {month} - {year} is TUESDAY" )
if h==4:
    print(f"Your date according to Zeller Congruence: {date} - {month} - {year} is WEDNESDAY" ) 
if h==5:
    print(f"Your date according to Zeller Congruence: {date} - {month} - {year} is THURSDAY" )
if h==6:
    print(f"Your date according to Zeller Congruence: {date} - {month} - {year} is FRIDAY" )
if h==0:
    print(f"Your date according to Zeller Congruence: {date} - {month} - {year} is SATURDAY" )
if h==1:
    print(f"Your date according to Zeller Congruence: {date} - {month} - {year} is SUNDAY" )
