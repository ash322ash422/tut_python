# Assignment 1: Student Report Card using f-strings

# Storing student details
name = input("Student name:")
roll_number  = input("Roll number:")

# Marks in subjects
math_marks    = int(input("Math marks:"))
science_marks = int(input("Science marks:"))


# Calculations
total_marks = math_marks + science_marks 
average_marks = total_marks / 2

# Printing the report card using f-strings
print(f"Student Name  : {name}")   
print(f"Roll Number   : {roll_number}")
print(f"Math marks    : {math_marks}")
print(f"Science marks : {science_marks}")
print(f"Total marks   : {total_marks}")
print(f"Average       : {average_marks}")
