'''def greet(name="stranger"):
    gr='hello'+name
    return gr
print(greet())
print(greet('nakul'))'''
#outoput
#hellostranger
#hellonakul
'''
name=str(input("Enter your name here :"))
def greet(name="stranger"):
    gr='hello'+name
    return gr
print(greet(name))
#output
#hello if name is not entered
#hello + name given'''

#recursion
'''
i=int(input("Enter the number :"))
def factorial(i):
    if(i==0|i==1):
       return 1
    else:
        return i*factorial(i-1)
print(factorial(i))'''

'''i=int(input("Enter the number :"))
def powerloop(i):
    if(i==0):
       return "Error"
    elif(i==1): #dangerous output 
       return 1
    else:
       return i**powerloop(i-1)
print(powerloop(i))'''
