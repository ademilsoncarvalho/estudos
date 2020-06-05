def execute():
    odd_number = int(input("Insert odd number:"))

    verify_number_pair(odd_number)
    string = "*"
    # init matrix
    matrix = [[string for number in range(odd_number)]]

    for number in range(odd_number):

        number_string_for_add = (number * 2) + 2
        if number_string_for_add >= odd_number:
            break
        new_line = [string for number in range(odd_number - number_string_for_add)]
        # divide it by two to add half of the types at the beginning and half at the end
        number_space_justify_string = [str(" ") for number in range(int(number_string_for_add / 2))]

        for space_string in number_space_justify_string:
            # add space in init and final
            new_line.append(space_string)
            new_line.insert(0, space_string)

        # add line
        matrix.append(new_line)
        matrix.insert(0, new_line)

    for item in matrix:
        print(''.join(item))


def verify_number_pair(number):
    if (number % 2) == 0:
        print("number informed is pair")
        exit()


if __name__ == '__main__':
    execute()
