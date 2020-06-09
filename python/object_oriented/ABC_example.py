from abc import ABCMeta, abstractmethod, ABC


class Software(metaclass=ABCMeta):
    @abstractmethod
    def __str__(self):
        return f'Software'

    @abstractmethod
    def version(self):
        return f'version is 1.0'


class Excel(Software):

    def __str__(self):
        return f'Excel'

    def version(self):
        return super().version()


if __name__ == '__main__':
    software = Excel()
    print(software.version())
    print(software)
