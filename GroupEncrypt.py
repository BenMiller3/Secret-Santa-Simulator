#For testing I used a group of my friends and created an encryption algorithm that will encrypt any three names chosen
#This is an idea to be built up upon and will be changed so that names will be able to be entered and these will be used
#Names must have a 3 character minimum, and names cannot be exactly the same.

import random

def gen(name1,name2,name3,names):
    code = name1
    salt1 = str(round(random.random()*9))
    salt2 = str(chr(round(random.random()*25)+65))
    salt3 = str(round(random.random()*9))

    x = 0

# The list of names must be 12 names long for now.
# 3 char long code given for each name. a total of 32^3 combinations for naming mechanisms available
    if(name1 == names[0]):
        p1 = "DOG"
    elif(name1 == names[1]):
        p1 = "CAT"
    elif(name1 == names[2]):
        p1 = "ANT"
    elif(name1 == names[3]):
        p1 = "MIK"
    elif(name1 == names[4]):
        p1 = "JUG"
    elif(name1 == names[5]):
        p1 = "BAR"
    elif(name1 == names[6]):
        p1 = "JOB"
    elif(name1 == names[7]):
        p1 = "CAL"
    elif(name1 == names[8]):
        p1 = "TIP"
    elif(name1 == names[9]):
        p1 = "MAC"
    elif(name1 == names[10]):
        p1 = "HOW"
    elif(name1 == names[11]):
        p1 = "ZIP"
    else:
        p1 = "XXX"

# If the names are the same then insert random
    if(name2 == names[0]):
        p2 = str(10 + round(random.random()*7)*12)
    elif(name2 == names[1]):
        p2 = str(11 + round(random.random()*7)*12)
    elif(name2 == names[2]):
        p2 = str(12 + round(random.random()*7)*12)
    elif(name2 == names[3]):
        p2 = str(13 + round(random.random()*7)*12)
    elif(name2 == names[4]):
        p2 = str(14 + round(random.random()*7)*12)
    elif(name2 == names[5]):
        p2 = str(15 + round(random.random()*7)*12)
    elif(name2 == names[6]):
        p2 = str(16 + round(random.random()*7)*12)
    elif(name2 == names[7]):
        p2 = str(17 + round(random.random()*7)*12)
    elif(name2 == names[8]):
        p2 = str(18 + round(random.random()*7)*12)
    elif(name2 == names[9]):
        p2 = str(19 + round(random.random()*7)*12)
    elif(name2 == names[10]):
        p2 = str(20 + round(random.random()*7)*12)
    elif(name2 == names[11]):
        p2 = str(21 + round(random.random()*7)*12)
    else:
        p2 = "00"
    num = str(round(random.random()*9))

    if(name3 == names[0]):
        x = round(random.random()*8)
        if(x%2!=0):
            x = x + 1
        y = 78+(random.random()*12)
        z = "L"
    elif(name3 == names[1]):
        x = round(random.random()*8)
        if(x%2!=0):
            x = x + 1
        y = 78+round(random.random()*12)
        z = "I"
    elif(name3 == names[2]):
        if(x%2==0):
            x = x + 1
        y = 65+round(random.random()*12)
        z = "N"
    elif(name3 == names[3]):
        x = round(random.random()*8)
        if(x%2!=0):
            x = x + 1
        y = 78+round(random.random()*12)
        z = "C"
    elif(name3 == names[4]):
        x = round(random.random()*8)
        if(x%2!=0):
            x = x + 1
        y = 65+round(random.random()*12)
        z = "S"
    elif(name3 == names[5]):
        if(x%2==0):
            x = x + 1
        y = 65+round(random.random()*12)
        z = "A"
    elif(name3 == names[6]):
        if(x%2==0):
            x = x + 1
        y = 78+round(random.random()*12)
        z = "O"
    elif(name3 == names[7]):
        if(x%2==0):
            x = x + 1
        y = 78+round(random.random()*12)
        z = "L"
    elif(name3 == names[8]):
        x = round(random.random()*8)
        if(x%2!=0):
            x = x + 1
        y = 65+round(random.random()*12)
        z = "D"
    elif(name3 == names[9]):
        if(x%2==0):
            x = x + 1
        y = 78+round(random.random()*12)
        z = "M"
    elif(name3 == names[10]):
        if(x%2==0):
            x = x + 1
        y = 65+round((random.random()*12))
        z = "M"
    elif(name3 == names[11]):
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

#Names given must be those that are within the list, if they are not then there will be an error.

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
    
def nameGen(n):             # This function is used to let the user generate a list of unique names to draw from
	names = [""]*n          # Defines the list of length n
	for i in range(n):      
		success = False     # Begins False, set to True at beginning, but if the name has been used it becomes False and repeats
		while(success==False):  # While the name is not unique
			names[i] = input("Enter name: ")    # Asks the user to input the name of the person in the list
			success = True                      # Sets success to True (will stay True if the name is unique to the list names)
			for j in range(i):
				if(names[j] == names[i]):       # If not unique, set success to False and prompt the user to enter a different name
					success = False
					print("This name has already been chosen. Please choose another.")  # Informs the user the name is in the list
	return names

