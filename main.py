# week3_homework_functions.py

# Exercise Lab 1: Printing Multiplication Tables

def mulitiplication_table(number):
    print("\nMultiplication Table")
    for i in range (13):
        print(f"{number} * {i} = ", i * number)

mulitiplication_table(9)

# Exercise Lab 2: Finding the Max

def find_max(number_list):
    number_list.sort()
    return(number_list[-1])

number_list = [0, -2, 3, 77, 5, 16]
max = find_max(number_list)
print(f"The largest number is {max}")

# Exercise Lab 3: Converting Numbers to Months
def convert_number_to_month(number):
    if number == 1:
        month = "January"
    elif number == 2:
        month = "February"
    elif number == 3:
        month = "March"
    elif number == 4:
        month = "April"
    elif number == 5:
        month = "May"
    elif number == 6:
        month = "June"
    elif number == 7:
        month = "July"
    elif number == 8:
        month = "August"
    elif number == 9:
        month = "September"
    elif number == 10:
        month = "October"
    elif number == 11:
        month =  "November"
    elif number == 12:
        month =  "December"
    else:
        month =  "Invalid Entry"
    print(month)

month = convert_number_to_month(200)
convert_number_to_month(9)
