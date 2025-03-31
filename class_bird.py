class Bird:

    def __init__(self):
        print('bird is ready')

    def Whoisthis (self):
        print('Bird')

    def swim(self):
        print('swim faster')


class Penguin(Bird):


    def __init__(self):
        super().__init__()
        print('penguin is ready')

    def Whoisthis(self):
        print('Penguin')

    def run(self):
        print('run faster')

peggy=Penguin()
peggy.Whoisthis()
peggy.swim()
peggy.run()