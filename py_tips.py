class employee:

    def _init_(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salaryself.email = self.firstname + "." + self.lastname + "@kite.com"

    def giveRaise(self, salary):

        self.salary = salary

class developer(employee):

    def _init_(self, firstname, lastname, salary, programming_language):
            super()._init_(firstname, lastname, salary)
            self.prog_langs = programming_languages

    def addlanguage(self, lang):
            self.prog_langs += [lang]
    employee1 = employee ("jon" , "smith" , 80000)

print(employee1. salary)

employee1. giveRaise(100000)

print(employee1.salary)
dev1 = developer("Joe", "Montana", 100000, ["Python", "C"])

print(dev1.salary)

dev1.addlanguage("Java")

print(dev1.prog_langs)

