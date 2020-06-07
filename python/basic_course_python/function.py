import random


# for declaring function using def
def test_function():
    print("hello function")


test_function()


def test_function_parameter(parameter):
    print("hello function " + parameter)


test_function_parameter("teste parameter")

# function type get type variable
list = ["ade"]
print(type(list))

# function int formating string to int
string = "10"
print(int(string))

# function input receive a value entry from the user in version 3.X from python
age = input("Whats is your age?")
print(int(age))

# range of function return a iterable list of numbers, using in for
print(range(5))

# function help
# help() then the function name you want help

# format examples
# format float
# 7 is houses before the comma
# 2 is houses after the comma
# f format is float
print("R$ {:7.2f}".format(1234.50))
# integer using d
print("R$ {:07d}".format(4))
# format date
print("Data {:02d}/{:02d}".format(9, 4))

# number random
print(int(random.random() * 100))
# using range
print(random.randrange(1, 101))

# numero absoluto abs()
print(abs(10))
print(abs(-10))

# variable __name__
# content variable for "__main__" file run directly
if __name__ == "__main__":
    print("file run directly not imported !!")

# boll testing
bool(0)
bool("")
bool(None)
bool(1)
bool(-100)
bool(13.5)
bool("test")
bool(True)

# using find in string, return position OR -1 for not found
string = "test"
print(string.find("t"))
# using for witch string
for letter in string:
    print(letter)

# lower and upper
print(string.lower())
print(string.upper())
# first letter upper
print(string.title())

# remove spaces from string
string = "   test"
print(string.split())

# __file__ get complete path file
import os
print(__file__)
# dir of actual file
print(os.path.dirname(__file__))
