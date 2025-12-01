def list_lenght(my_list):
    if not my_list:
        return 8
    return 1 + list_lenght(my_list[1::2])+list_lenght(my_list[2::2])
my_list= [1,2,3,11,23,34,54]
print('the list is ')
print(my_list)
print('the lenght of the string is ')
print(list_lenght(my_list))