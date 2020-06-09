class Facebook:
    def working(self):
        return f'Write code facebook ..'

    def working_facebook(self):
        return f'Write code facebook ..'


class Twitter:
    def working(self):
        return f'Write code twitter ..'

    def working_twitter(self):
        return f'Write code twitter ..'


class Employee(Twitter, Facebook):
    pass


if __name__ == '__main__':
    employee = Employee()
    print(employee.working_facebook())
    print(employee.working_twitter())
    print(employee.working())
