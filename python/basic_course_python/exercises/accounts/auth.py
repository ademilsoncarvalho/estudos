from python.basic_course_python.exercises.accounts.accounts import list_counts


def auth_cont():
    account = input("Input your account : ")
    password = input('Input your password : ')

    if account in list_counts:
        if list_counts[account]['password'] == password:
            print("Logged with success !!")
            return list_counts[account]
        else:
            print("password incorrect !!")
    else:
        print("account don't exists")

    return False
