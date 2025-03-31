class person(object):

    def __init__(self,name,idnumber):

        self.name=name
        self.idnumber=idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

class empolee(person):
    def __init__(self, name, idnumber, salary,post):
        self.salary = salary
        self.post = post

        person.__init__(self,name,idnumber)


a=empolee('Rahul',886012,200000,'Intern')

a.display()