def romanToint(romaninput):
   

  roman={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}

  result_integer=0

  for i in range(0,len(romaninput)-1):
      if roman[romaninput[i]]< roman[romaninput[i+1]]:
        result_integer -= roman[romaninput[i]]
      else:
        result_integer+= roman[romaninput[i]]
  return result_integer + roman[romaninput[-1]]
roman=input("input roman numberal :")
print('integer equilent :',romanToint(roman))