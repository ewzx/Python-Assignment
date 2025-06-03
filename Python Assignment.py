from datetime import datetime
import os

#-----------------------Ng Ginny-------------------------
# Log access for successful login
def log_access(username, role):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("access_log.txt", "a") as f:
        f.write(f"{timestamp} - {username} - {role}\n")

def view_access_log():
    print("\n--- Login Access Log ---")
    try:
        with open("access_log.txt", "r") as f:
            logs = f.readlines()
            if not logs:
                print("No login records found.")
            else:
                for line in logs:
                    print(line.strip())
    except FileNotFoundError:
        print("Access log file not found.")

# User Registration
def register_user(clearance_code):
    username = input("Enter username: ")
    password = input("Enter password: ")
    name = input("Enter name: ")
    with open("userdata.txt", "a") as f:
        f.write(f"{username}:{password}:{name}:{clearance_code}\n")
    print("Registered Successfully.")

# Delete User
def delete_user(role_code):
    username = input("Enter the username to delete: ")
    found = False
    lines = []
    with open("userdata.txt", "r") as f:
        for line in f:
            u, p, name, c = line.rstrip().split(":")
            if u == username and c == role_code:
                found = True
                continue
            lines.append(line)
    if found:
        with open("pyp", "w") as f:
            for l in lines:
                f.write(l)
        print(f"{username} deleted successfully.")
    else:
        print("User not found or role mismatch.")

# Coach-Sport Assignment
def assign_coach_sport():
    coach = input("Enter coach username: ")
    sport = input("Enter sport to assign: ")
    with open("coach_sport.txt", "a") as f:
        f.write(f"{coach}:{sport}\n")
    print(f"{coach} assigned to {sport}.")

# Income Report
def view_income_report():
    total_income = 0
    incomes = []

    with open("income_report.txt", "r") as f:
        print(f"{'Sport':<15} {'Income':>15}")
        print("-" * 30)
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split(":")
            if len(parts) == 2:
                sport, amount = parts
                try:
                    amount_float = float(amount.replace(",", ""))
                    incomes.append((sport, amount_float))
                    total_income += amount_float
                    formatted_amount = f"RM{amount_float:,.2f}"
                    print(f"{sport:<15} {formatted_amount:>15}")
                except ValueError:
                    print(f"Invalid amount for sport: {sport}")
        print("-" * 30)
        formatted_total = f"RM{total_income:,.2f}"
        print(f"{'Total Income:':<15} {formatted_total:>15}")

# User Records
def ReadFileData(AllRec):
    AllRec.clear()
    try:
        with open('userdata.txt', 'r') as fh:
            for line in fh:
                listRec = line.strip().split(':')
                if len(listRec) == 4:
                    AllRec.append(listRec)
    except FileNotFoundError:
        pass

def SaveData(AllUsers):
    with open('userdata.txt', 'w') as fh:
        for record in AllUsers:
            recstr = ':'.join(record) + '\n'
            fh.write(recstr)

def SearchModify(AllRec, username):
    found = False
    for cnt in range(len(AllRec)):
        if AllRec[cnt][0] == username:
            found = True
            print('UserID:', AllRec[cnt][0])
            print('User Name:', AllRec[cnt][2])
            print('User Password:', AllRec[cnt][1])
            newPassword = input('Enter a New Password: ')
            AllRec[cnt][1] = newPassword
            SaveData(AllRec)
            print('\nProfile Updated.\n')
            break
    if not found:
        print("User not found in records.")

# Update own profile
def update_own_profile(username):
    AllUsers = []
    ReadFileData(AllUsers)
    SearchModify(AllUsers, username)
#--------------------------------------------------------


#----------------------Huang Yixuan----------------------
#load coaches' information from coaches.txt
def load_coaches():
    try:
        with open("coaches.txt","r") as fh :
            return[line.strip().split(",") for line in fh if line.strip()]
    except FileNotFoundError:
        return[]

#save information to coaches.txt
def save_coaches(coaches):
    print("Saving coach information to file...")
    with open("coaches.txt","w") as fh:
        for coach in coaches:
            fh.write(",".join(coach)+"\n")

#load training information
def load_trainings():
    print("Loading training information...")
    try:
        with open("trainings.txt","r") as fh :
            return[line.strip().split(",") for line in fh if line.strip()]
    except FileNotFoundError:
        return[]

#save to trainings.txt
def save_trainings(trainings):
    print("Saving training information to file...")
    with open("trainings.txt","w") as fh:
        for training in trainings:
            fh.write(",".join(training)+"\n")

#save but contain original data
def add_training_to_file(new_training):
    trainings = load_trainings()
    trainings.append(new_training)
    save_trainings(trainings)

#log in
def coach_login():
    print("Please log in.")
    coaches = load_coaches()
    attempts = 3
    while attempts > 0 :
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        for coach in coaches:
            if coach[0] == username and coach[1] == password:
                print(f"Login successfully! Welcome back, {coach[2]}! ")
                return coach
        attempts -= 1
        print(f"Login failure. The remaining attempt is : {attempts} ")
    print("You have no attempt to login! ")
    return None

#add training courses
def add_training(coach_username):
    print("Adding training course...")
    trainings = load_trainings()
    training_name = input("Please enter the course name: ")
    charges = input("Please enter the course charges: ")
    schedule = input("Please enter the course schedule: ")
    #identification: course name + coach name
    training_id = f"{coach_username}_{training_name}"
    new_training = [training_id, coach_username, training_name, charges, schedule]
    add_training_to_file(new_training)
    print("Add the course successfully! ")

#update the course
def update_training():
    print("Ready to update the course...")
    trainings = load_trainings()
    course_name = input("Please enter the course name which you want to update: ")
    found = False
    for i, training in enumerate(trainings):   #enumerate(sequence, [start=0])
        if training[2] == course_name:
            print(f"Now the course information is: {training}")
            training[2] = input("New course name: ") or training[2]
            training[3] = input("New charge: ") or training[3]
            training[4] = input("New schedule: ") or training[4]
            trainings[i] = training
            save_trainings(trainings)
            print("Successfully update!")
            found = True
            break
    if not found:
            print("Course not found.")

#delete course
def delete_training():
    print("Ready to delete the course...")
    trainings = load_trainings()
    training_id = input("Please enter the course id which you want to delete: ")
    for i, training in enumerate(trainings):
        if training[0] == training_id:
            del trainings[i]      #delete [i] in traings
            save_trainings(trainings)
            print("Successfully delete! ")
            return
    print("Course not found.")

#to see the trainee's information
def view_enrolled_trainees():
    try:
        with open("traineedetails.txt", "r") as fh:
            trainees = [line.strip().split(",") for line in fh if line.strip()]
        with open("trainprogram.txt","r") as fh:
            programs = [line.strip().split(",") for line in fh if line.strip()]
    except FileNotFoundError:
        print("Trainee file not found.")
        return
    trainee_courses_list = []
    for program in programs:
        trainee_name = program[0].lower()
        course_name = program[1]
        trainee_courses_list.append((trainee_name, course_name))
    if not trainees:
        print("Trainee data not found.")
        return
    print("\n=== INFORMATION OF ALL TRAINEES ===")
    print("Trainee name\tContact number\t\tIC\t\tCourse")
    print("-"*100)
    for trainee in trainees:
        trainee_name = trainee[1].lower()
        trainee_ic = trainee[2]
        trainee_contact = trainee[4]
        courses = []
        for t in trainee_courses_list:
            if t[0] == trainee_name and t[1] not in courses:
                courses.append(t[1])
        unique_courses = []
        for course in courses:
            if course not in unique_courses:
                unique_courses.append(course)
        unique_courses.sort()
        course_str = ", ".join(unique_courses) if unique_courses else "none"
        print(trainee_name,"\t",trainee_contact,"\t",trainee_ic,"\t",course_str)

#update own information
def update_profile(coach):
    print("Updating your information...")
    coaches = load_coaches()
    index = coaches.index(coach)
    print("Current information: ",coach)
    coach[0] = input("New username: ") or coach[0]
    coach[1] = input("New password: ") or coach[1]
    coach[2] = input("New name: " ) or coach[2]
    coach[3] = input("New contact email: ") or coach[3]
    coach[index] = coach
    save_coaches(coaches)
    print("Update successfully.")

#view all course data
def view_all_trainings():
    trainings = load_trainings()
    if not trainings:
        print("There is no training course now.")
    print("\n=== COURSE INFORMATION ===")
    print("Training id\t\t\tCoach\t\tCourse name\t\tCharge\tSchedule")
    print("-"*100)
    for training in trainings:
        print(training[0], "\t", training[1], "\t", training[2], "\t", training[3], "\t", training[4])

#coach menu
def coach_main_menu(coach):
    while True:
        print("\n=== COACH MENU ===")
        print("1. Add training course")
        print("2. Update training course")
        print("3. Delete training course")
        print("4. View trainees list")
        print("5. Update own profile")
        print("6. View all the course")
        print("7, Log out")
        choice = input("Select the action: ")
        if choice == "1":
            add_training(coach[0])
        elif choice == "2":
            update_training()
        elif choice == "3":
            delete_training()
        elif choice == "4":
            view_enrolled_trainees()
        elif choice == "5":
            update_profile(coach)
        elif choice == "6":
            view_all_trainings()
        elif choice == "7":
            print("Logging out...")
            return
        else:
            print("Action can not work. Please choose again.")
    while True:
        print("\n=== COACH MENU ===")
        print("1. Add training course")
        print("2. Update training course")
        print("3. Delete training course")
        print("4. View trainees list")
        print("5. Update own profile")
        print("6. View all the course")
        print("7, Log out")
        choice = input("Select the action: ")
        if choice == "1":
            add_training(coach[0])
        elif choice == "2":
            update_training()
        elif choice == "3":
            delete_training()
        elif choice == "4":
            view_enrolled_trainees()
        elif choice == "5":
            update_profile(coach)
        elif choice == "6":
            view_all_trainings()
        elif choice == "7":
            print("Logging out...")
            return
        else:
            print("Action can not work. Please choose again.")
#--------------------------------------------------------


#-------------------Wong Zhen Xuan-----------------------
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
                global gname
                gu, gp, gname, c = line.strip().split(":") #u, p, c = username, password, clearance; .rstrip is to remove \n on line 87; .split is to split the three data in txt file
                if username == gu and password == gp: #check if the user's input is the same in the csv file
                    print("Login Successfully!\n")
                    log_access(username, c)
                    return c, username
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
            u, p, n, c = line.strip().split(":")
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
            confirmtxt = f"\nAll of {user}'s Training Programs Will Be \033[1mDELETED\033[0m, Confirm? (Y/N): "

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

def infochange(list, old, new, txt):
    for row in range(len(list)):
        for clm in range(len(list[row])):
            if old == list[row][clm]:
                list[row][clm] = new

    list = write(list, txt)
    return list
#--------------------------------------------------------

#-----------------------Ng Ginny-------------------------
def admin():
    AllUsers = []
    ReadFileData(AllUsers)
    while True:
        print('''
Admin Menu:
1. Register Coach
2. Delete Coach
3. Assign Coach to Sport
4. Register Receptionist
5. Delete Receptionist
6. View Income Report
7. Save Data
8. Update Own Profile
9. View Login Access Log
10. Exit to Main Menu
''')
        choice = input('Select Your Choice: ')
        if choice == '1':
            register_user('c')
            ReadFileData(AllUsers)
        elif choice == '2':
            delete_user('c')
            ReadFileData(AllUsers)
        elif choice == '3':
            assign_coach_sport()
        elif choice == '4':
            register_user('r')
            ReadFileData(AllUsers)
        elif choice == '5':
            delete_user('r')
            ReadFileData(AllUsers)
        elif choice == '6':
            view_income_report()
        elif choice == '7':
            SaveData(AllUsers)
            print("Data Saved.")
        elif choice == '8':
            username = input("Enter your admin username: ")
            update_own_profile(username)
            ReadFileData(AllUsers)
        elif choice == '9':
            view_access_log()
        elif choice == '10':
            break
        else:
            print("Invalid choice.")
#--------------------------------------------------------


#-------------------Wong Zhen Xuan-----------------------
def receptionist():
    while True:
        print(f"Welcome, {gname.title()}.")
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
                    name = input("Please Enter Your Name: ").title()
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
                        newdata = [username, password, name, "te"]
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
                    print("\nEnrolled Successfully!\n")
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
                                    if userlist[cnt][0] == user and userlist[cnt][1] == amounts[cnt][1]:
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
                        print("\nThis Username Is Not Enrolled As A Trainee, Please Enter A Trainee's Username.")

                    elif exist == 1:
                        if choice == "1" or choice == "Delete Trainee":
                            userlist = update(userlist, username, 3)
                            write(userlist, "trainprogram")
                            datalist = update(datalist, username, 5)
                            write(userlist, "userdata")
                            print("Deleted Successfully.")
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
            print(f"Name:     {gname}")
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

                elif choice == "Name":
                    newname = input("Please Enter Your New Name: ")
                    datalist = infochange(datalist, gname, newname, "userdata")
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
            print("\nLogout Successfully!")
            print("Exiting Program.")
            break

        else:
            print("Invalid Action, Please Try Again.")
#--------------------------------------------------------


#----------------------Huang Yixuan----------------------
def coach():
    coach = coach_login()
    if coach:
        coach_main_menu(coach)
    else:
        print("Log in failure.")
        exit()
#--------------------------------------------------------


#----------------------Soon Yu Hang----------------------
def trainee(username):
    while True:
        with open("userdata.txt", "r") as f:
            u = p = name = c = ""
            for line in f:
                u, p, name, c = line.rstrip().split(":")
                if u == username: #Matching Data to Username
                    break
            print(f"Welcome Trainee {name}.")
            print('''
            1. Training Schedule
            2. Payment
            3. Help Desk
            4. Update Own Profile
            5. Logout
            ''')
            choice = input('What would you like to do?:').title()

            with open("trainprogram.txt", "r") as x: #TrainProgram
                u = program = amtpaid = amtdue = ""
                for line in x:
                    u, program, amtpaid, amtdue = line.rstrip().split(":")
                    if u == username:  # Matching Data to Username
                        break
                if choice == '1': #View Program
                    print(f"{program}")

                elif choice == '2': #Payment
                    if amtdue==0:
                        print(f"Nothing Due")
                    elif amtdue<0: #Error Testing
                        print(f"ERROR")
                    else:
                        print(f"Payments Due {amtdue}")
                        print(f"Paid Amount {amtpaid}")

                elif choice == '3': #Request
                    cnt = 0
                    print (f"What is your issue?")
                    print('''
                    1. Change Training Program
                    2. View Request
                    3. Back to Main Menu
                    ''')
                    choice_exit = input().title()
                    with open("pendingreq.txt", "a") as p:  # New Request
                        u = program = new_program = ""
                        for line in p:
                            u, program, new_program = line.rstrip().split(":")
                            if u == username:  # Matching Data to Username
                                break
                        if choice_exit == '1':
                            p.write(f"{u}:{program}:{new_program}\n")
                            print(f"Request Sent Successfully")
                            cnt += 1
                        elif choice_exit == '2': #View Request
                            if cnt > 0:
                                print(f"You Have {cnt} Pending Request(s).")
                                with open("pendingreq.txt", "w") as p: #Overwrite/Delete Request
                                    for line in f:
                                        if username not in line.strip("\n"):  # Checks if the user is in the string
                                            f.write(line)
                                            print(f"Request Successfully Deleted")
                            elif cnt < 0: #Error Testing
                                print(f"ERROR")
                            else:
                                print(f"No Pending Request(s)")

                        elif choice_exit == '3':
                            break
                        else:
                            print (f"Invalid Input, Please Try Again.")

                elif choice == '4': #Profile Update
                        update_own_profile(u)

                elif choice == '5': #Back to login
                    print (f"Are you sure?") #DoubleChecking
                    print('''
                    1. Yes
                    2. No
                    ''')
                    choice_exit = input().title()
                    if choice_exit == '1':
                        print("\nLogout Successfully!")
                        login()
                    elif choice_exit == '2':
                        break
                    else:
                        print("Invalid Input, Please Try Again.")
                else:
                    print("Invalid choice.")
#--------------------------------------------------------


# Main Program Loop
def main():
    while True:
        print('''
1. Login
0. Exit
''')
        action = input("Select Your Action: ")
        if not action.isdigit():
            print("Invalid input. Try again.")
            continue
        action = int(action)

        if action == 1:
            clearance, username = login()
            if clearance == "a":
                admin()
                exit()
            elif clearance == "r":
                receptionist()
                exit()
            elif clearance == "c":
                coach()
                exit()
            elif clearance == "te":
                trainee(username)
                exit()

        elif action == 0:
            print("Exiting program.")
            exit()
        else:
            print("Invalid choice.")

main() #call def main()