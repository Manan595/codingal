tec_dict = {'condigal':2,'is':2,'best':2,'for':2,"coding":2}
print ('The oringal dictionary :'+str (tec_dict ))

k=2

res=0
for  key in tec_dict:
    if tec_dict[key]==k:
        res=res+1
print('frequncey of k is :'+ str (res))        