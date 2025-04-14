class India():
    def capital(self):
        print("New Delhi is the captial of India")

    def language(self):
        print('hindi is the most spoken language in India')

    def type(self):
        print('India is a developing contry')

class usa():
    def capital(self):
        print("Washington D.C is the captial of usa")

    def language(self):
        print('the language in USA is english')

    def type(self):
        print('India is a developed contry')

obj_ind = India()
obj_usa = usa()

for contry in (obj_ind, obj_usa):
    contry.capital()
    contry.language()
    contry.type()
