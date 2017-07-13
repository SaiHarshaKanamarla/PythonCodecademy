hrs = int(input())
rate = float(input())
pay = 0;

if(hrs<=40):
    pay = hrs*rate
else:
    pay = 40*rate + 1.5*rate*(hrs-40)
    
print(pay)
