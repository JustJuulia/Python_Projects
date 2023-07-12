f = open('tasks.txt', "r")
print("your tasks atm: ")
num = 0
for i in f:
    print(num, ".  ", i)
    num +=1
f.close()
def pick():
    global choice
    choice = input("woudl you like to delete some tasks or add some tasks or nothing? d for delete a for add and n for nothng: ")
pick()
while choice != 'n':
    if choice == 'd':
        f = open('tasks.txt', "r")
        lines = f.readlines()
        f.close()
        delline = int(input("pick which line (number):  "))
        f = open('tasks.txt', 'w')
        for number, line in enumerate(lines):
            if number != delline:
                f.write(line)
        print("task deleted succsefully!")
    if choice == 'a':
        f = open('tasks.txt', 'a')
        newer = input("write a task:  ")
        f.write('\n' +  newer)
        f.close()
        print("added!")
    else:
        print("wrong letter dumdum")
    f = open('tasks.txt', "r")
    print("your tasks atm: ")
    num = 0
    for i in f:
        print(num, ".  ", i)
        num += 1
    f.close()
    pick()
