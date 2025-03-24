class Employee:

    def __init__(self):
        print('Employee created')

    def __def__(self):
        print('desructor called ')


def Create_obj():
    print('Making object :')

    obj = Employee()
    print('function end')
    del obj

print('Called create_obj() function ...')

obj= Create_obj

print('program end ...')