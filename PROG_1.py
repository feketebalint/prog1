#Írjon függvényt, amely két szám esetén meghatározza a legnagyobb közös prím
#osztójukat. Készítsen hatékony implementáció, hogy közel valós időben tetszőleges
#agy számokra is lefusson a program.

def prime(n):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                return False
    return True
