def divide(ourdividend, ourdivisor):
    sign=(-1 if (ourdividend<0)^(ourdivisor <0)else 1);
ourdividend=abs(ourdividend);
ourdivisor=abs(ourdivisor);

Quotientnumber=0
tempnumber=0

for i in range(31,-1,-1):
    if (tempnumber+(ourdivisor<<i) <=ourdividend):
        tempnumber+= ourdivisor <<i
        Quotientnumber|=1<<i
        