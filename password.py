#PSSWORD GENERATOR
import random
length = 0
alphabetnocapital = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','w','x','y','z']
alphabetcapital = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','W','X','Y','Z']
nums = ['0','1','2','3','4','5','6','7','8','9']
specialchar = ['@', '#', '%', '*', '&', '!']
def lenf():
    global length
    try:
        length = int(input("whats the desired length of the password (cannot be anything smaller than 1:  "))
    except:
        print("only ints!")
lenf()
while length <= 0:
    lenf()
fq = input("would you liek to have tehre non-capital alphabet letters? y if you would like to:  ")
sq = input("would you liek to have tehre capital alphabet letters? y if you would like to:  ")
tq = input("would you liek to have tehre numbers? y if you would like to:  ")
fourthq = input("would you liek to have tehre special characters? y if you would like to:  ")
if(fq,sq,tq,fourthq != 'y'):
    print("u gotta have something there ")
i = 0
password = ""
tables = []
if fq == 'y':
    tables.append("nocap")
if sq == 'y':
    tables.append("cap")
if tq == 'y':
    tables.append("num")
if fourthq == 'y':
    tables.append("spec")
while i < length:
    choice = random.choice(tables)
    if choice == "nocap":
        password += random.choice(alphabetnocapital)
    elif choice == "cap":
        password += random.choice(alphabetcapital)
    elif choice == "num":
        password += random.choice(nums)
    elif choice == "spec":
        password += random.choice(specialchar)
    i+= 1
print(password)
