import random

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}",";",":","\\","|","'","\"","<",">",",",".","/","?","`","~", " "]
uniArr = []

for i in range(1000, 1100):
    uniArr.append(chr(i))
    
def encrypt(char, num):
    if char in alphabet:
        ogIndex = alphabet.index(char)
        newIndex = (ogIndex+num)
        return uniArr[newIndex]
        
message = input('Enter your message here!;\n').lower()
key = random.randint(1000000000, 10000000000)
print(f'This is your key! Keep it safe {key}')
print('Encrypted message;')

numList = [int(i) for i in str(key)]

while len(numList) < len(message):
        numList += numList

for (m, n) in zip(message, numList):
    print(encrypt(m,n), end='')
