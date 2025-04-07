class myclass:
    __privateVar=37;
    def __privatemeth(self):
        print("i am inside the class")

    def hello(self):
        print("private variable value:",myclass.__privateVar)


foo = myclass()
foo.hello()
foo.__privatemeth