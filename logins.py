
def logging():
    f = open("logins.txt")
    global choice
    choice = input("log in or sign in? l for log in and s for sign in: ")

    if choice == "l":
        login = input("login: ")
        password = input("password: ")
        for textline in f:
            wordsList = textline.split(' ', 1)
            if login == wordsList[0]:
                if password == wordsList[1].strip():  # Remove trailing newline character
                    print("logged in!")
                    f.close()
                    return
                else:
                    print("incorrect password bro")
                    f.close()
                    return
        print("incorrect login bro")
        f.close()

    elif choice == 's':
        login = input("login: ")
        password = input("password: ")
        for textline in f:
            wordsList = textline.split(' ', 1)
            if login == wordsList[0]:
                print("login is already used")
                f.close()
                return
        f = open("logins.txt", "a")
        f.write('\n' + login + " " + password)
        f.close()
        print("done!")
logging()
while choice == 'l' or choice == 's':
    logging()
