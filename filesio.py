'''done with the with statement 
syntax
with open("","") as f:
    f.command()
    no use of f.close() in with statements

f=open("","r")
print(f.read())

f=open(""."w")
print(f.write(""))

with open("tem.c","r+") as f: #for update command use r+
    f.read()
    f.write("nike")

with open("tem.c","a") as f: 3for update command use a
        f.write("chappal leni h kya") '''