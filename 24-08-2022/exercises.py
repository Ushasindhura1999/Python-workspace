##11) WAPP to reverse internal content of every second word present in the given String.
##a="Hello python people".split()
##while len(a)>0:
##    if a%2!=0:
##        b=a[i]
##        c=reversed(b)
##        for j in c:
##            print(j,end="")
##    else:
##        print(a[i],end=" ")
##            

##12) WAPP for the following requirements
##    input->a3z2b4
##    output->aaabbbbzz(sorted string).


'''a="z3a2b4"
b=" "
for i in a:
    if i.isalpha():
        x=i
    else:
        c=int(i)
        b=b+x*c
        c=sorted(b)
print("".join(c))'''
   
    
    
    
##13)WAPP  to extract year ,month,date and time using lambda Function.



##14)WAPP to find the values of length six in given list using lambda Function.

##15)WAPP to find factorial of number using closure Function.

def hello(fact):
    def hi():
      fact=1
      for i in range(1,6):
          fact=fact*i
      return fact
    return hi()
print(hello(5))



