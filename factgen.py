import randfacts
def fact():
    global a
    print(randfacts.get_fact())
    a = input("continue? y if yes:  ")
fact()
while a == 'y':
    fact()
