class parrot:
    spices='bird'

    def __init__(self,name,age):
       

       self.age=age
       self.name=name
blu=parrot('Blu', 10)
woo= parrot ('woo', 15)

print('blu is a {}'.format(blu.spices))
print('woo is a {}'.format(woo.spices))

print("{}is your {} years old ".format(blu.name,blu.age))
print("{}is your {} years old".format(woo.name,woo.age))
