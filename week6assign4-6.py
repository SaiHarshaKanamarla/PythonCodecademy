def computepay(h,r):
    if(h<40):
        p = h * r
    else:
        p = r*40+(1.5*r*(h-40))
    return p


hrs = int(input());
hrs_st = float(hrs);
rate = float(input());
print (computepay(hrs_st,rate));
        
