## declaring variable
variable_test = 1
print(variable_test)
## declaring multiple variables in unique line
variable_test, variable_test1 = (1, 2)
print(variable_test, variable_test1)
##tybes numbers
int= 1
float = 1.3
complex = 10J
string = 'string'
string2 = "string2"
## format string
print(string2[0:5])
## concat string
print(string + string2)
## concat string with number
print(string  + ' int numer %s' % (int))
## print string using format, replace parameters following the order
string = "minha idade é {}"
print(string.format(12))
