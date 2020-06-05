import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# write file
# file = open(BASE_PATH + '/' + 'file_test.dat', 'w')
# file.write('test_word')
# file.write('\n')
# file.close()

# append file
# file = open(BASE_PATH + '/' + 'file_test.dat', 'a')
# file.write('test_word2')
# file.write('\n')
# file.close()

# read file
# file = open(BASE_PATH + '/' + 'file_test.dat', 'r')
# print(file.readline().strip()) # strip remove '/n' of string
# print(file.readlines())
# file.close()

# read file witch "with", python close file automatic
# with open(BASE_PATH + '/' + 'file_test.dat') as file:
#     for row in file:
#         print(row)
