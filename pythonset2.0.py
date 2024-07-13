'''n=int(input("Enter the number :"))

for i  in range (1,11):
    print( str(n)+ "\t"+ 'multiplied by'+ "\t" + str(i) + "\t" +'is =', n*i)'''

'''l1=["Harry","Sachin","Sohan","Rahul"]
i=0
while i in range (len(l1)):
    if("S" in l1[i]):
        print("Good Morning" + " " + l1[i])
    i=i+1'''

'''n=int(input("Enter the number here :"))
i=0
while(i<=10):
    print(str(n) + " " + "multiplied by"+" " + str(i) + " is =", n*i )
    i=i+1'''

'''n=2
i=1
while (i<100):
    if( (n%2) and (n%3) and (n%5) and (n%7) != 0):
        print(n)
    if(n in [2,3,5,7]):
        print(n)
    n=n+1
    i=i+'''

'''n=1
sum = 0
p=int(input("Enter upto what terms you want to sum:"))
i=0
while (i<p):
    sum = sum + n
    n=n+1
    i=i+1
print(sum)'''
  

'''for i in range(0,5) :
    for j in range(0,5):
        print('*',end=" ")
        j=j+1
        
    print('\n')
    for k in range(0,5):
        print('$',end=" ")

    print('\n')
i=i+1'''


'''n=int(input("Enter the number whose factorial you want :"))
sum=1
for i in range(0,n):
    if (n>=0):
        sum = sum*(n-i)
print(sum)'''

'''chr ='*'
for i in range(0,3):
    for j in range(0,5):
        print(chr,end=" ")
    print('\n')'''

'''s=int(input())
for i in range(s):
    print(" "*(s-i-1),end=" ")
    print("*"*(2*i+1),end=" ")  #end is used to print in same line'''

'''for i in range(3):
    for j in range(3):
        if(i==1 & j==1):
            print(" ")
        else:
            print('*',end=" ")
    print('\n')'''
      
'''num=int(input("Enter the number:"))
for i in range(10,0,-1):
    print(str(num) +'*'+ str(i) +'=',num*i)'''

