class Iosstring():


    def __init__(self):
        self.str1 =""


    def get_string(self):
        self.str1=input('enter string :')


    def print_string(self):
        print(' Results is :',self.str1.upper())

str1= Iosstring()
str1.get_string()
str1.print_string()