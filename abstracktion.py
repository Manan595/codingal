from abc import ABC, abstractmethod

class ABclass(ABC):

    def print(self,x):
        print('passed value',x)

    @abstractmethod
    def task(self):
        print('WE are inside ABclass task ')
    
class test_class(ABclass):
    def task(self):
        print('we are inside of test_class talk')

test_obj= test_class()
test_obj.task()
test_obj=print(100)