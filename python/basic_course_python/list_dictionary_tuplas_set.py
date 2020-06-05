# list example
list_test = ["item", 10, "item"]
print(list_test)
print(list_test[0])
# append item in list
list_test.append("testappend")
print(list_test)
# remove item list
list_test.remove("testappend")  ## using value, not position
print(list)
# declaring tuples
# tuples are imutables lists
# dont possible concatenate tuples and lists
tuple2 = ("tuple", "tuple")
print(tuple2)
concat_tuple = ('one') + ('two')
print(concat_tuple)
# dictionary
# using dictionary for declaring lists with key and value
dictionary = {'one': 1, 'two': 2}
print(dictionary['one'])
print(dictionary.keys())
print(dictionary.values())
# using list for numbers
list_number = [1, 2, 3, 4]
print(max(list_number))
print(min(list_number))
print(len(list_number))
# count number of itens in list
list_cont = [0, 0, 1, 2, 35]
print(list_cont.count(0))
# using .index return num of index of element in list
# case not found generate error
print(list_cont.index(0))
# transform list in tuple or tuple in list
new_tuple = tuple(list_test)
print(new_tuple)
new_list = list(new_tuple)
print(new_list)
# using set for collection witch uniques elements
# A set is an unordered collection of elements
# set has no index
list_set = {"ade", "ade"}  # use { for init set
list_set.add("teste")
print(list_set)
