##1) take a list of 8 numbers
##lst = [1,2,3,4,5,6,7,8]
##and add the alternative numbers in list 
##
##after first iteration list should be [4,6,8,10,12,14]
##after second iteration [12,16,20,24]
##after third iteration [32,40]
##
##when list is having two elements print that list in the output
##




##lst = [1,2,3,4,5,6,7,8]
##b=[]
##while len(lst)!=2:
##    for i in range(len(lst)-2):
##        k=lst[i]+lst[i+2]
##        b.append(k)
##    lst=b
##    b=[]
##    print(lst)
##        


##a=int(input("enter: "))
##b=[]
##for i in range(1,a):
##    if a%i==0:
##        b.append(i)
##if(sum(b)==a):
##    print("perfect")
##else:
##    print("not")

##from math import factorial
##a=int(input())
##temp=a
##s=0
##while a>0:
##    d=a%10
##    s=s+factorial(d)
##    a=a//10
##if(temp==s):
##    print("strong")
##else:
##    print("not")
