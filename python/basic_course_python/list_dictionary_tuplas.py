## list example
list = ["item", 10, "item"]
print(list)
print(list[0])
## append item in list
list.append("testappend")
print(list)
## remove item list
list.remove("testappend")  ## using value, not position
print(list)
## declaring tuples
## tuples are imutables lists
## dont possible concatenate tuples and lists
tuple = ("tuple", "tuple")
print(tuple)
concat_tuple = ('one') + ('two')
print(concat_tuple)
## dictionary
## using dictionary for declaring lists with key and value
dictionary = {'one': 1, 'two': 2}
print(dictionary['one'])
print(dictionary.keys())
print(dictionary.values())
