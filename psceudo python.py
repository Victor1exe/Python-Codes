'''l2=["witcher","haunt","sickfellow","dasty"]
for er in l2:
    if "er" in er:
        print(er)'''

#encrytion and decryption
text=input("Enter a one-word,lowercase message:")
distance=int(input("Enter the distace value"))
code=""
for i in text:
    ordvalue=ord(i)
    ciperValue = ordvalue + distance
    if ciperValue > ord('z'):
        ciperValue = ord('a') + distance - ord('z') +ordvalue -1
    code+=chr(ciperValue)
print(code)

#decryption
code=input("Enter the coded text")
distance=int(input("Enter the distance value"))
text=""
for i in code:
    ordvalue=ord(i)
    cipervalue=ordvalue-distance
    if cipervalue<ord('a'):
        cipervalue=ord('z')+ord('a')-distance - ordvalue -1
    text += chr(cipervalue)
print(text)




