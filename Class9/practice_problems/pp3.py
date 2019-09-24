# inheritance


class Person:
    def __init__(self, name):
        self.name = name

    def introduction(self):
        print("My name is: %s" % self.name)
        return self.name


class SecretAgent:
    def __init__(self, codename):
        self.codename = codename

    def steal_information(self):
        print("I Stole Info!")

    def codename_introduction(self):
        print("My name is: %s" % self.codename)
        return self.codename


class Employee(Person, SecretAgent):
    def __init__(self, name, codename):
        self.name = name
        self.codename = codename


Jane = Employee("Jane", "Mrs. Dangerous!")
Jane.steal_information()
Jane.codename_introduction()









