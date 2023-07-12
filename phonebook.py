f = open('phone.txt', "r")
print("all your data: ")
num = 0
for i in f:
    print(num, ".  ", i)
    num +=1
f.close()
def pick():
    global choice
    choice = input("woudl you like to delete some phone numebrs or add some or do nothing? d for delete a for add and n for nothng: ")
pick()
while choice != 'n':
    if choice == 'd':
        f = open('phone.txt', "r")
        lines = f.readlines()
        f.close()
        delline = int(input("pick which line (number):  "))
        f = open('phone.txt', 'w')
        for number, line in enumerate(lines):
            if number != delline:
                f.write(line)
        print("phone deleted succsefully!")
    if choice == 'a':
        f = open('phone.txt', 'a')
        phonenum = input("write a phone number:  ")
        nick = input("write how would ou like to get them named:  ")
        f.write('\n' +  nick + "   " + phonenum)
        f.close()
        print("added!")
    else:
        print("wrong letter dumdum")
    f = open('phone.txt', "r")
    print("your phone numebrs atm: ")
    num = 0
    for i in f:
        print(num, ".  ", i)
        num += 1
    f.close()
    pick()
