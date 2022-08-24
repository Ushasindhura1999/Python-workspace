'''1) wap to print range of twin prime numbers by not using function'''
##for i in range(2,20):
##    for j in range(2,i):
##        if i%j==0:
##            break
##    else:
##        x=i+2
##        for k in range(2,x):
##            if x%k==0:
##                break
##        else:
##            print(i,x)
'''2) wap to print perimutations of the string "abc" by not using function.'''
##from itertools import permutations
##a="abc"
##print(list(permutations(a,3)))
'''3) wap to print even and odd numbers separatly from a list by using filter function.'''
##a=[1,2,3,4,5,6,7,8]
##b=list(filter(lambda a:a%2==0,a))
##c=list(filter(lambda a:a%2!=0,a))
##print(b,c)
'''4) wap to print range of fibonacci series by using recursion function.'''

##def fib(n):
##    if n<=1:
##        return 1
##    else:
##        return fib(n-1)+fib(n-2)
##n=10
##for i in range(1,n):
##    print(fib(i))
'''5) wap to print the strings from a list which are having the length of the list.'''
##a=["pyhon","java","c","d"]
##count=0
##for i in a:
##    count=count+1
##print(count)

