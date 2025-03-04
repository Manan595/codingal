num=int(input("you want odd and even numbers what under value? :"))

odd_list= [i for i in range (num) if i%2 !=0]
print('list of odd number!',odd_list,'\n')

even_list= [i for i in range (num) if i%2 == 0]
print('list of odd number!',odd_list,'\n')

fruits=['pinapple','mange','orage','grapes','coconut ']
fruit1=[x[0].upper()+x[1:]for x in fruits]
print(('fruits as proper nouns :',fruit1))