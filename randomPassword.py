#importing the modules
import random
import string

#storing all charactor in variable
charbunch = string.ascii_letters+ string.digits+string.punctuation
#taking size input
size = int(input("ENTER THE SIZE OF PASSWORD : "))
password = ""

#generating random password
for i in range(size):
    password += random.choice(charbunch)

#printing password
print("Your Password is : ",password)