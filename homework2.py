def squaredvalues(beg,end) :
    lst=[]
    
    for i in range(beg,end):
        lst.append(i**2)
    lst_even=[]
    lst_odd=[]
    for i in lst:
        if i % 2 == 0:
            lst_even.append(i)
        else:
            lst_odd.append(i)

    print("Here's a listf even squares within specified range",lst_even)
    print("Here's a listf even squares within specified range",lst_odd)


beg = int(input("enter a starting range:"))
end= int(input("enter a end range:"))

squaredvalues(beg,end)
    