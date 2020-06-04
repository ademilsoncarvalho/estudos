## create bank account
from python.basic_course_python.exercises.bank_acount import utils
from python.basic_course_python.exercises.bank_acount.accounts import auth


def print_balance(saldo):
    print("Your balance is %s" % saldo)


def get_operation():
    print('Whats operation want ?')
    print('1 - Balance')
    print('2 - Deposit')
    print('3 - Withdraw')
    print('0 - Get Out')
    return input("Input operation want : ")


def deposit(conta):
    valor = input("Digite quanto deseja depositar : ")
    conta['value'] += int(valor)
    print_balance(conta['value'])


def withdraw(conta):
    valor = input("Digite quanto deseja sacar : ")
    if int(valor) <= conta['value']:
        conta['value'] -= int(valor)
    else:
        print("Não possui saldo diponivel")
    print_balance(conta['value'])


def exe_operation(account, is_continue, operation):
    if operation == '1':
        print_balance(account['value'])
    if operation == '2':
        deposit(account)
    if operation == '3':
        withdraw(account)

    elif operation == '0':
        is_continue = False
    input("Input <Enter> to continue ..")
    return is_continue


def main():
    utils.get_header()
    is_continue = auth.auth_cont()

    if is_continue:
        is_continue = True
        while is_continue:
            operation = get_operation()
            is_continue = exe_operation(is_continue, is_continue, operation)
            utils.clear_display()


main()
