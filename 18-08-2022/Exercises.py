##1).Write a Python program to remove and print every third number from a list of numbers until the list becomes empty

'''l=[1,2,3,4,5,6,7]
a=len(l)
index=0
position=3-1
while a>0:
    index=(index+position)%a
    print(l.pop(index))
    a-=1'''




##2).. Write a Python program to count the number of students of individual class.
##Sample Output:
##Counter({'VI': 3, 'V': 2, 'VII': 1})



'''from collections import Counter
classes=(('V',1),('VI',1),('V',2),('VI',1),('VI',3),('VII',1))
students=Counter(i for i,j in classes)
print(students)'''




##3).Write a Python program to concatenate all elements in a list into a string and return it
'''a=[10,20,30,40,50]
for i in a:
    print(i,end= "")'''
##4).Write a Python program to convert a float to ratio. 
##
##Expected Output :
##
##21/5

##
##5).Write a Python function that prints out the first n rows of Pascal’s triangle
'''a=int(input("enter the number"))
l=[[0 for x in range(a)] for y in range(a)]
n=1
low=0
high=a-1
count=int(a+1)//2
for i in range(count):
    for j in range(low,high+1):
        l[i][j]=n
        n+=1
    for j in range(low+1,high+1):
        l[j][high]=n
        n+=1
    for j in range(high-1,low-1,-1):
        l[high][j]=n
        n+=1
    for j in range(high-1,low,-1):
        l[j][low]=n
        n+=1
    low+=1
    high-=1
for i in range(a):
    for j in range(a):
        if i==0 or j==0 or i==a-1 or j==a-1:
            print(l[i][j],end=" ")
            n+=1
        else:
            print(" ",end=" ")
    print()'''
        
