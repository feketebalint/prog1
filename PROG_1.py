#Eldönti hogy az adott szám prím-e
def prime(n):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                return False
    return True

def lnko(num1,num2):
    if num1 > num2:
        num1,num2 = num2,num1
    for i in range(num1+1,1,-1):
        if num1 % i == 0 and num2 % i == 0 and prime(i):
            return i
 #A kisebb számtóé visszafele megy a for ciklus, hogy hatékonyabb legyen a program.
