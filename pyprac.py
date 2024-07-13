'''n=0
for i in range(5):
    print('*'*(2*n+1))
    n=n+1

n=5
for i in range(6):
    print('*'*(2*n+1))
    n=n-1'''


'''n=0
for i in range(5):
    print(" "*(5-n) + '*'*(2*n+1) + " "*(5-n))
    n=n+1

n=5
for i in range(6):
    print(" "*(5-n) + '*'*(2*n+1) + " "*(5-n))
    n=n-1'''

#anomalous
'''n=0
for i in range(6):
    print(" "*(5-n) + '*'*(2*n+1) + " "*(5-n))
    n=n+1

n=5
for i in range(5):
    print(" "*5 + '*'*n)
    n=n-1'''
'''n=5
m=0
for i in range(5):
    print(" "*m + '*'*n + " "*5)
    n=n-1
    m=m+1'''

#anomalous
'''n=0
m=5
for i in range(6):
    print(" "*m +'*'*(n))
    n=n+1
    m=m-1

n=5
for i in range(5):
    print(" "*5 + '*'*n)
    n=n-1'''  
    
'''sentence=str(input("Enter the sentence:"))
for i in sentence:
    a=i
    c=ord(a) + 5
    d=chr(c)
    print(d,end=" ")'''


#anomalous
import random
a=randominteger
print(a)

