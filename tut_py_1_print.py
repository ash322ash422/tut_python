# print(object(s), sep=separator, end=end, file=file, flush=flush)
# object(s)	Any object, and as many as you like. Will be converted to string before printed
# sep='separator'	Optional. Specify how to separate the objects, if there is more than one. Default is ' '
# end='end'	Optional. Specify what to print at the end. Default is '\n' (line feed)
# file	Optional. An object with a write method. Default is sys.stdout
# flush	Optional. A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False



# The print() function prints the specified message to the screen, or other standard output device.
# The message can be a string, or any other object, the object will be converted into a string before written to the screen.


print("Hello World")


print("Hello", "How you doing today ?")

print("Hello", "how are you?", sep="---")

# Printing Multiple Values
name = "Alice"
age = 30
print("Name:", name, "Age:", age)



# Using Concatenation
name = "Bob"
age = 25
print("Name: " + name + " Age: " + str(age))

# Using sep to Change Separator
print("apple", "banana", "cherry", sep="-")


#  Using str.format()
name = "David"
age = 50
print("Name: {}, Age: {}".format(name, age))


# print special character using / backslash
print("Hello\nWorld!")  # Newline
print("Hello\tWorld!")  # Tab

# print raw string
print(r"Hello\nWorld!")  # Outputs: Hello\nWorld!


message = 'Please wait while the program is loading...'
print(message)

name = 'Ashwani'
print(f"Hey {name}. How are you doing {name} ?. Its a good day {name} to do some kayaking today. What do you think {name} ?")

# Printing Unicode Characters
print("\u2764")  # Heart symbol

# Printing Multiple Lines Using Triple Quotes
print("""This is
a multiline
message!""")

