# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

salary = int(input("Enter your Salary"))
service = int(input("Enter your year's of service"))

if(service>=5):
    bonus = salary * 0.05
    print(f"your new Salary is: {bonus}")

else:
    print("No bonus")


# ********************************************************************

# Write a program to check whether a person is eligible for voting or not. (accept age from user) if age is greater than 17 eligible otherwise not eligible

age = int(input("Enter your age: "))

if (age > 17):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# ********************************************************************

# Write a program to check whether a number entered by user is even or odd.

num = int(input("Enter a number: "))

if (num % 2 == 0):
    print("The number is even.")
else:
    print("The number is odd.")


# ********************************************************************

# Write a program to check whether a number is divisible by 7 or not. Show Answer

num = int(input("Enter a number: "))

if (num % 7 == 0):
    print("The number is divisible by 7.")
else:
    print("The number is not divisible by 7.")


# ********************************************************************

# Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye".

num = int(input("Enter a number: "))

if (num % 5 == 0):
    print("Hello")
else:
    print("Bye")




# Take values of length and breadth of a rectangle from user and print if it is square or rectangle.

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

if (length == breadth):
    print("It is a square.")
else:
    print("It is a rectangle.")



# Take two int values from user and print greatest among them.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if (num1 > num2):
    print(f"{num1} is the greatest.")
else:
    print(f"{num2} is the greatest.")


# A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.

quantity = int(input("Enter the quantity: "))
cost_per_unit = 100
total_cost = quantity * cost_per_unit

if total_cost > 1000:
    total_cost *= 0.9 

print("Total cost is Rs.", total_cost)

# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A

marks = float(input("Enter your marks: "))

if (marks < 25):
    grade = "F"
elif (25 <= marks < 45):
    grade = "E"
elif (45 <= marks < 50):
    grade = "D"
elif (50 <= marks < 60):
    grade = "C"
elif (60 <= marks < 80):
    grade = "B"
else:
    grade = "A"

print("Your grade is:", grade)


# A student will not be allowed to sit in exam if his/her attendence is less than 75%.


classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

percentage = (classes_attended / classes_held) * 100
print(f"Attendance percentage: {percentage}%")

if percentage >= 75:
    print("You are allowed to sit in the exam.")
else:
    print("You are not allowed to sit in the exam.")


# Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

medical_cause = input("Do you have a medical cause? (Y/N): ")

if(medical_cause == 'Y' or medical_cause == "y"):
    print("Allow")

else:
    print("Not Allow")


# Write a program to check if a year is leap year or not.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.
# if employee is a male and age is in between 20 to 40 then he may work in anywhere
# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
# And any other input of age should print "ERROR"

age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
marital_status = input("Enter your marital status (Y/N): ")

if gender == 'F':
    print("You will work in urban areas only.")
elif gender == 'M':
    if 20 <= age <= 40:
        print("You may work anywhere.")
    elif 40 < age <= 60:
        print("You will work in urban areas only.")
    else:
        print("ERROR")
else:
    print("ERROR")

# Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria : Unit Price
# upto 100 units no charge Next 200 units Rs 5 per unit After 200 units Rs 10 per unit (For example if input unit is 350 than total bill amount is Rs.3500 (For example if input unit is 97 than total bill amount is Rs.0 (For example if input unit is 150 than total bill amount is Rs.750

electricity_bill = int(input("Enter your unit in 'Electricity Bill'"))

if(electricity_bill>100 and electricity_bill<=200):
    print(f"your bill with charges: {electricity_bill*5}")
elif(electricity_bill>200 and electricity_bill<=300):
    print(f"your bill with charges: {electricity_bill*10}")

else:
    print("No Charges")




# Take input of age of 3 people by user and determine oldest and youngest among them.

age1 = int(input("Enter age of person 1: "))
age2 = int(input("Enter age of person 2: "))
age3 = int(input("Enter age of person 3: "))

oldest = max(age1, age2, age3)
youngest = min(age1, age2, age3)

print("Oldest person age:", oldest)
print("Youngest person age:", youngest)