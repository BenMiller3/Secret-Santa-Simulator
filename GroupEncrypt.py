#For testing I used a group of my friends and created an encryption algorithm that will encrypt any three names chosen
#This is an idea to be built up upon and will be changed so that names will be able to be entered and these will be used
#Names must have a 3 character minimum, and names cannot be exactly the same.

import random

def gen(name1,name2,name3):
    code = name1
    salt1 = str(round(random.random()*9))
    salt2 = str(chr(round(random.random()*25)+65))
    salt3 = str(round(random.random()*9))

    x = 0

#Default names I had used for testing: [Julia,Emily,Ben,Jess,Brandon,George,Cal,Sydney,Cam,Cameron,Zach,]

    if(name1 == "julia"):
        p1 = "DOG"
    elif(name1 == "emily"):
        p1 = "CAT"
    elif(name1 == "ben"):
        p1 = "ANT"
    elif(name1 == "michelle"):
        p1 = "MIK"
    elif(name1 == "jess"):
        p1 = "JUG"
    elif(name1 == "brandon"):
        p1 = "BAR"
    elif(name1 == "george"):
        p1 = "JOB"
    elif(name1 == "cal"):
        p1 = "CAL"
    elif(name1 == "sydney"):
        p1 = "TIP"
    elif(name1 == "cam"):
        p1 = "MAC"
    elif(name1 == "cameron"):
        p1 = "HOW"
    elif(name1 == "zach"):
        p1 = "ZIP"
    else:
        p1 = "XXX"

    if(name2 == "julia"):
        p2 = str(10 + round(random.random()*7)*12)
    elif(name2 == "emily"):
        p2 = str(11 + round(random.random()*7)*12)
    elif(name2 == "ben"):
        p2 = str(12 + round(random.random()*7)*12)
    elif(name2 == "michelle"):
        p2 = str(13 + round(random.random()*7)*12)
    elif(name2 == "jess"):
        p2 = str(14 + round(random.random()*7)*12)
    elif(name2 == "brandon"):
        p2 = str(15 + round(random.random()*7)*12)
    elif(name2 == "george"):
        p2 = str(16 + round(random.random()*7)*12)
    elif(name2 == "cal"):
        p2 = str(17 + round(random.random()*7)*12)
    elif(name2 == "sydney"):
        p2 = str(18 + round(random.random()*7)*12)
    elif(name2 == "cam"):
        p2 = str(19 + round(random.random()*7)*12)
    elif(name2 == "cameron"):
        p2 = str(20 + round(random.random()*7)*12)
    elif(name2 == "zach"):
        p2 = str(21 + round(random.random()*7)*12)
    else:
        p2 = "00"
    num = str(round(random.random()*9))

    if(name3 == "julia"):
        x = round(random.random()*8)
        if(x%2!=0):
            x = x + 1
        y = 78+(random.random()*12)
        z = "L"
    elif(name3 == "emily"):
        x = round(random.random()*8)
        if(x%2!=0):
            x = x + 1
        y = 78+round(random.random()*12)
        z = "I"
    elif(name3 == "ben"):
        if(x%2==0):
            x = x + 1
        y = 65+round(random.random()*12)
        z = "N"
    elif(name3 == "michelle"):
        x = round(random.random()*8)
        if(x%2!=0):
            x = x + 1
        y = 78+round(random.random()*12)
        z = "C"
    elif(name3 == "jess"):
        x = round(random.random()*8)
        if(x%2!=0):
            x = x + 1
        y = 65+round(random.random()*12)
        z = "S"
    elif(name3 == "brandon"):
        if(x%2==0):
            x = x + 1
        y = 65+round(random.random()*12)
        z = "A"
    elif(name3 == "george"):
        if(x%2==0):
            x = x + 1
        y = 78+round(random.random()*12)
        z = "O"
    elif(name3 == "cal"):
        if(x%2==0):
            x = x + 1
        y = 78+round(random.random()*12)
        z = "L"
    elif(name3 == "sydney"):
        x = round(random.random()*8)
        if(x%2!=0):
            x = x + 1
        y = 65+round(random.random()*12)
        z = "D"
    elif(name3 == "cam"):
        if(x%2==0):
            x = x + 1
        y = 78+round(random.random()*12)
        z = "M"
    elif(name3 == "cameron"):
        if(x%2==0):
            x = x + 1
        y = 65+round((random.random()*12))
        z = "M"
    elif(name3 == "zach"):
        x = round(random.random()*8)
        if(x%2!=0):
            x = x + 1
        y = 65+round((random.random()*12))
        z = "C"
    else:
        x = 0
        y = "X"
        z = 0
    
    p1 = cc(p1)
    p2 = num + p2
    p3 = str(x) + str(chr(round(y))) + str(z)

    pepper1 = str(chr(round(random.random()*25)+65))
    pepper2 = str(round(random.random()*9))
    pepper3 = str(chr(round(random.random()*25)+65))
    
    return salt1+salt2+salt3+p1+p2+p3+pepper1+pepper2+pepper3

def main():
    name = ""
    name2 = ""
    name3 = ""
    loop = True
    while(name == (name2) or name == (name3) or name3 == (name2)):
        name = input("Enter the 1st name of the person you like, I'll encrypt it: ")
        name2 = input("Enter the 2nd name of the person you like, I'll encrypt it: ")
        name3 = input("Enter the 3rd name of the person you like, I'll encrypt it: ")
        if(name==name2 or name==name3 or name3==name2):
            print("You chose the same name twice, please pick three different names. /n")
    print("\n \n",gen(name,name2,name3))

def cc(message):
    crypt = 23
    code = ""
    for i in range(len(message)):
        temp = ord(message[i])
        temp2 = temp + crypt
        if(temp2>90):
            temp4 = temp2-90
            temp2 = 65 + temp4
        temp3 = chr(temp2)
        code = code + temp3
    return code

def verify(name):
    return name
    #USED TO VERIFY IF A NAME IS ON THE LIST OR NOT
