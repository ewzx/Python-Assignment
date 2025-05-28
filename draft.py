def login():
    t = 3 #login attemps
    login = 1 #to check if they had logined previously
    while True:
        if t > 0 and login == 0: #when they had logged in wrongly previously
            print("\nIncorrect Credentials, Please Try Again.")
        elif t <= 0: #they had logged in wrongly for 3 times
            print("\nLogin Failed, Please Try Again Later.\n")
            exit()

        print("\nPlease Enter Your Username and Password.")
        username = input("Username: ")
        password = input("Password: ")

        with open("userdata.txt", "r") as f: #create a txt file as f
            for line in f: #to read the lines in the file
                global gu
                global gp
                gu, gp, c = line.strip().split(":") #u, p, c = username, password, clearance; .rstrip is to remove \n on line 87; .split is to split the three data in txt file
                if username == gu and password == gp: #check if the user's input is the same in the csv file
                    print("Login Successfully!\n")
                    if c == "a": #check user's clearance in csv file
                        admin() #call def admin()
                        exit()
                    elif c == "r":
                        receptionist() #call def receptionist()
                        exit()
                    elif c == "c":
                        coach() #call def coach()
                        exit()
                    elif c == "te":
                        trainee() #call def trainee()
                        exit()
            t -= 1 #they have wrongly inputted user n password
            login = 0 #they have inputted user n password previously

def readlist(txt):
    userlist = [] #establish a list
    with open(f"{txt}.txt", "r") as f:
        for line in f: #for loop, every line in the file
            x = line.strip().split(":") #getting the information
            userlist.append(x) #adding it to the list
    return userlist #return the list

def alrdexist(item):
    exist = 0
    with open("userdata.txt") as f:
        for line in f:
            u, p, c = line.strip().split(":")
            if item == u and c != "te": #checking if the username is already taken while also checking if it is a trainee
                exist = 1 #marking it as previously existed
                return 2 #returning the info
            elif item == u: #only checking if the username is already taken
                exist = 1
                return 1
    if exist == 0: #it doesn't exit
        return 0

def write(list, txt):
    cnt = 0
    with open(f"{txt}.txt", "w") as f:
        for cnt in range(len(list)):
            combine = ":".join(list[cnt]) + "\n"
            f.write(combine)
    return list

def update(list, user, x):
    if x == 5:
        cnt = 0
        for line in list: 
            if line[0] == user:
                list.pop(cnt)
            cnt += 1
        return list

    elif x >= 0 and x != 1:
        found = -1
        row = 0
        totalprogram = []
        for line in list:
            if (user in line[0]):
                found = row
                totalprogram.append(list[found][1])
            row += 1

        if found != -1:
            cnt = 1
            print(f"Username: {user}")
            print("Training Programs:")
            for program in totalprogram:
                print(f"No.{cnt}:", program)
                cnt += 1
            
        actionzero = True
        if x == 3:
            actionzero = False
            confirmtxt = f"\nAll of {user}'s Training Programs Will be \033[1mDELETED\033[0m, Confirm? (Y/N): "

        elif x >= 0 and x != 3:
            while actionzero:
                action = input(f"Which Training Program Would You Like To Change? (Type 0 To Exit): ").title()
                checkint = True
                checkexist = False

                exist = 0
                actionzero = False
                if action == "0":
                    return list

                cnt = 0
                for program in totalprogram:
                    if action == program:
                        exist = 1
                        actionzero = False
                        checkint = False
                        checkexist = False
                        break

                while checkint:
                    if int(action)+1 >= 0 or int(action)+1 < 0:
                        print("\nPlease Enter The Name Of The Training Program.\n")
                        actionzero = True
                        checkexist = False
                        break
                
                while checkexist:
                    if exist == 0:
                        print(f"Training Program {action} Does Not Exist")

                if x >= 0 and exist == 1 and x != 4:
                    while True:
                        new = input("\nWhat Will The New Training Program Be? (Type 0 To Exit): ").strip().title()
                        confirmtxt = f"\n{user}'s Training Program Will Change From \033[1m{program}\033[0m --> \033[1m{new}\033[0m, Confirm? (Y/N): "
                        if new == "0":
                            actionzero = True
                            break

                elif x == 4 and exist == 1:
                    confirmtxt = f"\n{user}'s {action} Program Will Be \033[1mDELETED\033[0m, Confirm? (Y/N): "

        loop = True
        while loop:
            cnt = 0
            confirm = input(f"{confirmtxt}").capitalize()
            if confirm == "Y":
                if x == 0:
                    for line in list:
                        if line[0] == user and line[1] == program:
                            line[1] = new
                            print("\nUpdated Successfully!\n")
                            return list
                        
                elif x == 3:
                    for line in list: 
                        if line[0] == user:
                            list.pop(cnt)
                        cnt += 1
                    return list
                
                elif x == 4:
                    for line in list:
                        if line[0] == user and line[1] == program:
                            list.pop(cnt)
                        cnt += 1
                    print("\nUpdated Successfully!\n")
                    return list
            elif confirm == "N":
                loop = False
            else:
                print("Invalid Input, Please Try Again.")

    elif x == 1:
        program =""
        new = ""
        for line in list:
            if line[0] == user:
                program = line[1]
                new = line[2]
                break

        while True:
            confirm = input(f"\n{user}'s Training Program Will Change From \033[1m{program}\033[0m --> \033[1m{new}\033[0m, Confirm? (Y/N): ").capitalize()
            if confirm == "Y":
                list = readlist("trainprogram")
                for line in list:
                    if line[0] == user and line[1] == program:
                        line[1] = new
                        break
                return list
                
                    
            elif confirm == "N":
                return 0
            else:
                print("Invalid Input, Please Try Again.")
                break

def infochange(list, old, new, txt):
    for row in range(len(list)):
        for clm in range(len(list[row])):
            if old == list[row][clm]:
                list[row][clm] = new

    list = write(list, txt)
    return list

def admin():
    print("admin")

def receptionist():
    while True:
        print(f"Welcome, {gu.title()}.")
        print('''
    1. Register & Enroll A Trainee
    2. Enroll A Trainee
    3. View Pending Requests
    4. Update Trainee's Training Program
    5. Accept Payment
    6. Delete Trainee/Trainee's Training Program
    7. Change Account Information
    9. Logout
    0. Logout & Exit
    ''')
        
        try: #to check the class(integer, str, etc.) of action
            action = int(input("What would you like to do?: "))
        except ValueError: #execute when action is not an iteger
            print("Invalid Input, Please Try Again.")
            continue

        userlist = readlist("trainprogram")
        datalist = readlist("userdata")
        traineelist = readlist("traineedetails")
        pendinglist = readlist("pendingreq")

        if action == 1:
            regis = True
            while regis:
                username = input("Please Enter The Trainee's Username (Type 0 To Exit): ").strip() #get username
                if username == "0":
                    regis = False
                    break

                exist = alrdexist(username) #check if it already exists
                if exist== 1 or exist == 2: #already exists
                    print("\nUsername Already Exists, Please Try Another One.\n")
                
                elif exist == 0: #doesn't exist
                    password = input("Please Enter Their Password (Type 0 To Exit): ").strip()
                    if password == "0":
                        regis = False
                        break

                    program = input("What Program Would You Like To Enroll?: ").strip().title()
                    name = input("Please Enter Your Name: ")
                    ic = input("Please Enter Your IC/Passport Number: ")
                    email = input("Please Enter Your Email Address: ")
                    contact = input("Please Enter Your Contact Number: ")
                    amtpaid = "0"
                    amtdue = "100"
                    check = input(f"{username}, {password}, {name}, {program}, {ic}, {email}, {contact}, Are These Information Correct? (Y/N) (Type 0 To Cancel): ").title

                    if check == "0":
                        regis = False
                        break

                    elif check == "N":
                        print("Please Enter Again.")
                        regis = True

                    elif check == "Y":
                        newdata = [username, password, "te"]
                        datalist.append(newdata)
                        write(datalist, "userdata") #register new user to userdata.txt

                        userdata = [username, name, ic, email, contact]
                        traineelist.append(userdata)
                        write(traineelist, "traineedetails")
                        
                        newuser = [username, program, amtpaid, amtdue] #putting new user and program into a list
                        userlist.append(newuser) #adding it into the database as a whole
                        write(userlist, "trainprogram") #writing it into trainprogram.txt

                        print("Registered Successfully!")
                        regis = False
                        break
                
        elif action == 2:
            while True:
                username = input("Please Enter The Trainee's Username (Type 0 To Exit): ").strip()
                exist = alrdexist(username)
                if username == "0": #exit
                    break
                if exist == 0:
                    print("\nUsername Does Not Exist, Please Register First.\n")
                elif exist == 2: #username exists but it has another roll e.g: admin, coach
                    print("\nThis Username Is Not Enrolled As A Trainee, Please Register As A Trainee First.")
                elif exist == 1: #username exist
                    enroll = True
                    while enroll:
                        enroll = False
                        program = input("\nWhat Program Would You Like To Enroll? (Type 0 To Exit): ").strip().title()

                        exist = 0
                        if program == "0":
                            break

                        with open("trainprogram.txt") as f:
                            for line in f:
                                user, p, *_ = line.strip().split(":")
                                if username == user and p == program:
                                    print(f"{username} Has Already Enrolled In This Training Program.")
                                    enroll = True
                                    break
                                else:
                                    continue

                    amtpaid = "0"
                    amtdue = "100"
                    newuser = [username, program, amtpaid, amtdue]
                    userlist.append(newuser)
                    write(userlist, "trainprogram")
                    break

        elif action == 3:
            cnt = 0
            for pending in range(len(pendinglist)):
                cnt += 1
            print(f"You Have {cnt} Pending Request(s).")

            while True:
                action = input("Would You Like To Review Them? (Y/N): ").title()
                if action == "Y":
                    while True:
                        cnt = 1
                        for line in range(len(pendinglist)):
                            print(f"{cnt}. {pendinglist[line][0]}, {pendinglist[line][1]} --> {pendinglist[line][2]}")
                            cnt += 1

                        try:
                            choice = int(input("Which One Would You Like To Assess First?: "))
                        except ValueError:
                            print("Invalid Action, Please Try Again.")
                            continue

                        if choice in range(len(pendinglist) +1):
                            userlist = update(pendinglist, pendinglist[choice -1][0], 1)
                            if userlist == 0:
                                continue
                            else:
                                write(userlist, "trainprogram")
                                pendinglist.pop(choice -1)
                                write(pendinglist, "pendingreq")
                                print("Update Successfully!")
                            break

                        else:
                            print("Invalid Action, Please Try Again")

                elif action == "N":
                    break
                else:
                    print("Invalid Action, Please Try again")
                break

        elif action == 4:
            while True:
                username = input("\nPlease Enter The Trainee's Username (Type 0 To Exit): ").strip()
                exist = alrdexist(username)
                if username == "0":
                    break
                if exist == 0:
                    print("\nUsername Does Not Exist")
                elif exist == 2:
                    print("\nThis Username Is Not Enrolled As A Trainee, Please Enter A Trainee's Username.")
                elif exist == 1:
                    userlist = update(userlist, username, 2)
                    write(userlist, "trainprogram")
                    break

        elif action == 5:
            while True:
                choice = input("Please Enter The Username Whose Payment Record You Would Like to Access? (Type 0 To Exit): ")
                user = choice
                cnt = 1
                amounts = []
                amt = 0

                if choice == "0":
                    break

                for line in userlist:
                    if choice == userlist[amt][0]:
                        print(f"{cnt}. {userlist[amt][1]}: RM {userlist[amt][2]}/RM {userlist[amt][3]}")
                        tmp = [str(cnt), userlist[amt][0], userlist[amt][1], int(userlist[amt][2]), int(userlist[amt][3])]
                        amounts.append(tmp)
                        cnt += 1
                    amt += 1

                if cnt == 1:
                    print("\nUsername Not Found, Please Try Again\n")
                    continue
                
                elif cnt != 1:
                    loop = True
                    while loop:
                        choice = input("Which Training Program Would You Like To Access? (Type 0 To Exit): ").title()
                        exist = 0
                        tmp = 0

                        if choice == "0":
                            loop = False
                            break

                        for tmp in range(len(amounts)):
                            if choice == amounts[tmp][2] or choice == amounts[tmp][0]:
                                exist = 1
                                choice = amounts[tmp][2]
                                while True:
                                    try:
                                        pay = int(input("Please Enter The Desired Payment Amount (Type 0 To Exit): RM"))
                                    except ValueError:
                                        print("Please Enter Numbers Only.")
                                        continue
                                    break
                                
                                if pay == "0":
                                    loop = False
                                    break

                                cnt = 0
                                for cnt in range(len(amounts)):
                                    if choice == amounts[cnt][2]:
                                        amounts[cnt].pop(0)
                                        amounts[cnt][2] += pay
                                        amounts[cnt][2] = str(amounts[cnt][2])
                                    elif choice != amounts[cnt][2]:
                                        amounts[cnt].pop(0)
                                        amounts[cnt][2] = str(amounts[cnt][2])
                                        cnt += 1

                                cnt = 0
                                row = 0
                                for cnt in range(len(userlist)):
                                    if userlist[cnt][0] == user:
                                        userlist[cnt][2] = amounts[row][2]
                                        row += 1

                                write(userlist, "trainprogram")
                                print("Payment Successful.")
                                loop = False

                                while True:
                                    action = input("Would You Like A Receipt? (Y/N): ").title()
                                    if action == "Y":
                                        get = datetime.datetime.now()
                                        amt = 0
                                        for amt in range(len(userlist)):
                                            if user == userlist[amt][0] and choice == userlist[amt][1]:
                                                print(f'''
==================================================
    ------------------------------------------
            Your Beloved Compony
    DATE: {get.strftime('%x')}
    TIME: {get.strftime('%X')}
    ------------------------------------------
Username: {user}
Training Program: {choice}
Paid Amount: RM {pay}
Total Paid: RM {userlist[amt][2]}/RM {userlist[amt][3]}
==================================================
''')
                                        loop = False
                                        break

                                    elif action == "N":
                                        loop = False
                                        break

                        if exist == 0:
                            print("Invalid Action, Please Try Again.")

        elif action == 6:
            delete = True
            while delete:
                print("1. Delete Trainee")
                print("2. Delete Trainee's Training Program\n")
                choice = input("What Would You Like to do?: ").title()

                while True:
                    username = input("\nPlease Enter The Trainee's Username (Type 0 To Exit): ").strip()
                    exist = alrdexist(username)

                    if username == "0":
                        delete = False
                        break
                    if exist == 0:
                        print("\nUsername Does Not Exist")
                    elif exist == 2:
                        print("\nThis Username Is Not Enrolled As A Trainee, Please A Trainee's Username.")

                    elif exist == 1:
                        if choice == "1" or choice == "Delete Trainee":
                            userlist = update(userlist, username, 3)
                            write(userlist, "trainprogram")
                            datalist = update(datalist, username, 5)
                            write(userlist, "userdata")
                            print("Deleted Succesfully.")
                            delete = False
                            break
                        
                        elif choice == "2" or choice == "Delete Trainee's Training Program" or choice == "Delete Training Program":
                            userlist = update(userlist, username, 4)
                            write(userlist, "trainprogram")
                            delete = False
                            break

        elif action == 7:
            changeinfo = True
            print(f"Username: {gu}")
            print(f"Password: {gp}")

            while changeinfo:
                choice = input("Which One Would You Like To Change? (Type 0 To Exit): ").title()

                if choice == "0":
                    changeinfo = False
                    break

                elif choice == "Username":
                    newu = input("Please Enter Your New Username: ")
                    datalist = infochange(datalist, gu, newu, "userdata")
                    print("Updated Successfully!")
                    changeinfo = False
                
                elif choice == "Password":
                    newp = input("Please Enter Your New Password: ")
                    datalist = infochange(datalist, gp, newp, "userdata")
                    print("Updated Successfully!")
                    changeinfo = False

                else:
                    print("Invalid Input, Please Try Again.")

        elif action == 9:
            print("\nLogout Successfully!")
            login()
            break

        elif action == 0:
            break

        else:
            print("Invalid Action, Please Try Again.")

def coach():
    print("coach")

def trainee():
    print("trainee")

import datetime
login() #call def main()