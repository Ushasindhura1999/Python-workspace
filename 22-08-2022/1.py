##a="abr"
##b="ka "
##c=" "
##for i in range(len(a)):
##    c+=a[i]+b[i]
##print(c)


##from math import factorial
##a=145
##temp=a
##b=0
##while a>0:
##    r=a%10
##    b=b+factorial(r)
##    a=a//10
##if(temp==b):
##    print("strong")
##else:
##    print("not")

from functools import reduce
a=5
b=reduce(lambda x,y:x*y,range(1,a+1))
print(b)
