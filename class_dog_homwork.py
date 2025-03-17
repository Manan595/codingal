class dog:
    spices='dog'

    def __init__(self,name,bread):

        self.name=name
        self.bread=bread

tommy=dog('tommy','bulldog')
abi=dog('abi','german shepard')

print('black {} is a good friend'.format(tommy.spices))
print('White {} is a good friend'.format(abi.spices))


print('this dog is a {} and his name is {}'.format(tommy.bread,tommy.name))
print('this dog is a {} and his name is {}'.format(abi.bread,abi.name))