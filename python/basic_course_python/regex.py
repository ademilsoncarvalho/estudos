import re

## basic regex
string_find = "find"
all_string = "find the text"
result = re.match(string_find, all_string)
## result is object OR error case not found string
print(result.group())

## regex to uppercase and lowercase
string_find = "[fF]ind"
all_string = "Find the text"
result = re.match(string_find, all_string)
print(result.group())

##regex to like result
string_find = "[A-Za-z]ind"
all_string = "Find the text"
result = re.match(string_find, all_string)
print(result.group())

##regex to find list result
string_find = "[A-Za-z]ind"
all_string = "Find the text Find"
results = re.findall(string_find, all_string)
print(results)

##regex to find all word
# string_find = "[A-Za-z]i[A-Za-z]+"
string_find = "\w+i\w+"
all_string = "Find the text Find"
result = re.match(string_find, all_string)
print(result.group())