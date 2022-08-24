#6.Find the mean of a list.

'''a=[1,2,3,4,5]
b=sum(a)
print(b)
c=len(a)
print(c)
d=b/c
print(d)'''

##7.Take a list and perform list operation
'''a=[1,2,3,4]
b=[9,8,7,6]
a.insert(5,6)
print(a)
a.append(8)
print(a)
a.extend(b)
print(a)
a.pop()
print(a)
c=b.copy()
print(c)
b.clear()
print(b)
a.reverse()
print(a)
a.sort()
print(a)
b=a.count(1)
print(b)'''
##8.Collatz Sequence
'''a=int(input("enter: "))
while a>1:
    if a%2==0:
        a=a//2
        print(a)
    else:
        a=3*a+1
        print(a)'''
    
##9.Find the midpoint of a line
'''a1=1
a2=2
b1=3
b2=4
a3=a1+a2
a4=b1+b2
c=a3/2,a4/2
print(c)'''
##10.Get the values in one list and keys in another from a dictionary.
'''a={1:"python",2:"java",3:"c"}
b=list(a.keys())
print(b)
c=list(a.values())
print(c)'''
