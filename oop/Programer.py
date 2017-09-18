# coding=utf-8

class Programer(object):
    hobby = "Play Computer"

    @classmethod
    def get_hobby(cls):
        return cls.hobby

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    @property
    def get_weight(self):
        return self.__weight

    def self_introduction(self):
        print 'My Name is %s \nI am %s years old\n' % (self.name, self._age)

class BackendProgramer(Programer):
    def __init__(self, name, age, weight, language):
        super(BackendProgramer, self).__init__(name, age, weight)
        self.language = language

if __name__ == "__main__":
    programer = BackendProgramer('Albert', 10, 80, 'Python')
    print dir(programer)
    print programer.__dict__
    print programer.get_weight
    # print programer.get_weight()
    # print programer._Programer__weight
    print type(programer)
    print isinstance(programer, Programer)
