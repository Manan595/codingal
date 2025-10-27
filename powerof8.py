def powerof8(number):
    bitposition=0
    mask=1
    while (bitposition<=63):
        if (mask==number):
            return True
        bitposition+=3
        mask =1
    return False