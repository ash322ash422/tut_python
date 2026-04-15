# Make sure you install pytest
# python -m pip install pytest 

def add_numbers(a, b):

    return a + b
 
def subtract_numbers(a, b):

    return a - b
 
def main():

    num1 = float(input("Enter first number: "))

    num2 = float(input("Enter second number: "))
 
    addition = add_numbers(num1, num2)

    subtraction = subtract_numbers(num1, num2)
 
    print("Addition:", addition)

    print("Subtraction:", subtraction)
 
if __name__ == "__main__":

    main()
 