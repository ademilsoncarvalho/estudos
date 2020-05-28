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
