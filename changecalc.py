total_amount= int(input('enter your total amount'))
list_of_notes=[1000,500,100,50,20,10,5]

for i in list_of_notes:
    number_of_notes=total_amount//i
    total_amount%=i
if number_of_notes !=0:
    print('the number of notes',i,'is',number_of_notes)
