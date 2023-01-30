# Capstone Project III : Submitted by Bhavya Patteeswaran

# =====importing libraries===========
import datetime


# ====== Create functions===========
# Function 1 reg_user() - Register the new user and password in the user.txt file, no duplicate users are allowed.
def reg_user():
    new_user = (input("Please enter a new username: \n"))
    while new_user in usernames_lst:
        print("The username you entered is already listed.")
        new_user = input("Please enter a new username: \n")

    if new_user not in usernames_lst:
        usernames_lst.append(new_user)

    new_user_password = (input("Please enter a new password: \n"))
    confirm_new_password = input("Please retype your password to confirm: \n")

    while new_user_password != confirm_new_password:
        print("Your passwords do not match!")
        new_user_password = (input("Please enter a new password: \n"))
        confirm_new_password = input("Please retype your password to confirm: \n")

    if new_user_password == confirm_new_password:
        print("Your passwords are match.")
        passwords_lst.append(new_user_password)

    with open('user.txt', 'r+') as user_file:
        for i in range(len(usernames_lst)):
            user_file.write(user_dict["Usernames"][i] + ", " + user_dict["Passwords"][i] + '\n')

    print("Your new username and password have been successfully added.")


# Function 2 add_task() - Add new task into tasks.txt file
def add_task():
    task_file = open("tasks.txt", "a+")
    today = datetime.datetime.today()
    new_task_username = input("Enter the 'username' of the person whom the task is assigned to: ")
    new_title = input("Enter the 'title' of the new task: ")
    new_description = input("Enter the 'description' of the new task: ")
    new_assigned_date = today.strftime("%d %b %Y")
    new_due_date = input("Enter the due date of the new task in the format: dd mmm yyyy: ")
    task_completed = "No"

    task_file.write(
        f"\n{new_task_username}, {new_title}, {new_description}, {new_assigned_date}, {new_due_date}, {task_completed}")
    task_file.close()
    print("The new task is added to the tasks.txt file")


# Function 3 view_all() - View all task in requested output format from tasks.txt file
def view_all():
    with open("tasks.txt", "r") as tasks_read:
        data = tasks_read.readlines()
        for pos, task in enumerate(data, start=1):
            split_data = task.split(", ")
            output = f'--------------------[{pos}]-------------------------------\n'
            output += '\n'
            output += f'Task: \t\t\t{split_data[1]}\n'
            output += f'Assigned to: \t{split_data[0]}\n'
            output += f'Assigned Date:\t{split_data[3]}\n'
            output += f'Due Date:\t\t{split_data[4]}\n'
            output += f'Is completed?:  {split_data[5]}\n'
            output += f'Description: \t{split_data[2]}\n'
            output += '\n'
            output += '------------------------------------------------------\n'
            print(output)


# Function 4: view_mine() - View only login user's task and select specific task number to edit task or -1 to return
def view_mine():
    tasks_read = open("tasks.txt", "r")
    data = tasks_read.readlines()

    for pos, task in enumerate(data):
        split_data = task.split(", ")
        if username_in == split_data[0]:
            output = f'--------------------[{pos+1}]-------------------------------\n'
            output += '\n'
            output += f'Task: \t\t\t{split_data[1]}\n'
            output += f'Assigned to: \t{split_data[0]}\n'
            output += f'Assigned Date:\t{split_data[3]}\n'
            output += f'Due Date:\t\t{split_data[4]}\n'
            output += f'Is completed?:  {split_data[5]}\n'
            output += f'Description: \t{split_data[2]}\n'
            output += '\n'
            output += '------------------------------------------------------\n'
            print(output)

    while True:
        task_choice = int(input('Please select a task number to edit from the above output or type -1 to return to main menu: '))
        edit_task_choice = task_choice - 1

        if task_choice == -1:
            print("Return to main menu")
            break

        elif 0 <= edit_task_choice < len(data):
            edit_data = data[edit_task_choice]

            output = f'-----------[SELECT AN OPTION]-----------\n'
            output += "1- Edit task by changing username and due date only for not completed task: \n"
            output += "2- Mark task as completed: 'Yes' \n"
            output += '----------------------------------------\n:'

            choice = int(input(output))
            if choice == 1:
                split_data = edit_data.split(", ")
                if split_data[-1] in ['No', 'No\n']:
                    # Change the username of that particular task
                    update_username = input("Enter reassigned username to that particular task: ")
                    split_data[0] = update_username

                    # Update the due date of that particular task
                    update_due_date = input("Enter the due date of that particular task in the format: dd mmm yyyy: ")
                    split_data[4] = update_due_date
                    new_data = ", ".join(split_data)

                    data[edit_task_choice] = new_data

                    tasks_write = open('tasks.txt', 'w')
                    for task in data:
                        tasks_write.write(task)

                    tasks_write.close()
                    break

                else:
                    print("You can't edit on the completed task!")

            elif choice == 2:
                split_data = edit_data.split(", ")
                split_data[-1] = 'Yes\n'
                new_data = ", ".join(split_data)
                data[edit_task_choice] = new_data

                tasks_write = open('tasks.txt', 'w')
                for task in data:
                    tasks_write.write(task)

                tasks_write.close()
                break

            elif choice <= 0 or choice >= 3:
                print('You have selected an invalid option, try again.')
                continue

        else:
            print('You have selected an invalid option, try again.')
            continue

    tasks_read.close()
    print("You've finished the task in viewing your own task!")


# Function 5: overdue_check() - compare the due date with current date and find the overdue date of the task
def overdue_check(due_date):
    list_dates = due_date.split()  # 05 Jan 2023 -> ['05', 'Jan', '2023']
    day = int(list_dates[0])
    year = int(list_dates[2])

    # A month dictionary with number values is set to enable calculation of string month into an integer.
    months_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10,
                   'Nov': 11, 'Dec': 12}
    month = months_dict[list_dates[1]]

    date_now = datetime.date.today().strftime('%d %b %Y')
    date_now_list = date_now.split()
    day_now = int(date_now_list[0])
    year_now = int(date_now_list[2])
    month_now = months_dict[date_now_list[1]]

    # Convert date in same format to compare. date_1 is the due date and date_2 is the current date.
    date_1 = datetime.date(year, month, day)
    date_2 = datetime.date(year_now, month_now, day_now)

    over_due = False
    if date_2 > date_1:
        over_due = True

    elif date_1 > date_2 or date_1 == date_2:
        over_due = False

    return over_due


# Function 6: generate_reports() - create 2 files - task_overview.txt and user_overview.txt
def generate_reports():
    # Generate task_overview file
    task_overview = ""
    c = 0
    i = 0
    o = 0
    total_tasks = len(tasks_dict)
    for key in tasks_dict:
        if tasks_dict[key][5] == "Yes":
            c += 1

        elif tasks_dict[key][5] == "No":
            i += 1

            if overdue_check(tasks_dict[key][4]):  # If function returns 'True', a task is overdue and incomplete.
                o += 1

    # Concatenate above outputs in task_overview string
    task_overview += f"The total number of tasks that have been generated and tracked using the task_manager.py are {total_tasks}."
    task_overview += f"\nThe total number of completed tasks are {c}."
    task_overview += f"\nThe total number of uncompleted tasks are {i}."
    task_overview += f"\nThe total number of tasks that haven't been completed and overdue are {o}."
    task_overview += f"\nThe percentage of incomplete tasks are {round((i / total_tasks) * 100, 2)}%."
    task_overview += f"\nThe percentage of tasks that overdue are {round((o / total_tasks) * 100, 2)}%."

    # Write the task_overview string in the task_overview.txt file
    with open('task_overview.txt', 'w') as fw_tov:
        fw_tov.write(task_overview)

    # generate the user_overview file
    total_users = len(usernames_lst)
    fw_uov = open('user_overview.txt', 'w')

    # Setting blank strings to store info in to be written to the generated text files.
    user_overview = ""
    user_overview += f"The total number of users registered with task_manager.py are {total_users}."
    user_overview += f"\nThe total number of tasks generated and tracked by task_manager.py are {total_tasks}."

    for user in usernames_lst:
        # Set variables for total users, for each user's complete, incomplete & over-due tasks.
        total_task_user = 0
        uc = 0
        ui = 0
        uo = 0
        for key in tasks_dict:
            if tasks_dict[key][0] == user:
                total_task_user += 1

            if tasks_dict[key][0] == user and tasks_dict[key][5] == 'Yes':
                uc += 1

            if tasks_dict[key][0] == user and tasks_dict[key][5] == 'No':
                ui += 1

                if overdue_check(tasks_dict[key][4]):  # call the function overdue to check due_date.
                    uo += 1

        # Concatenate above outputs in user_overview string.
        user_overview += f"\nUsername: {user}"
        user_overview += f"\nThe total number of tasks assigned to {user} are {total_task_user}."
        user_overview += f"\nThe percentage of the total number of tasks assigned to {user} are {round((total_task_user / total_tasks) * 100, 2)}%."
        user_overview += f"\nThe percentage of tasks assigned to {user} that have been completed are {round((uc / total_task_user) * 100, 2)}%."
        user_overview += f"\nThe percentage of tasks still to be completed by {user} are {round((ui / total_task_user) * 100, 2)}%."
        user_overview += f"\nThe percentage of incomplete and overdue tasks assigned to {user} are {round((uo / total_task_user) * 100, 2)}%."
        user_overview += "\n"

    # Write the user_overview string into the user_overview.txt file.
    fw_uov.write(user_overview)
    fw_uov.close()
    print("user_overview and task_overview text file reports are generated successfully.")


# Function 7: display_statistics() - To display task_overview.txt and user_overview.txt reports in console output.
def display_statistics():
    with open('task_overview.txt', 'r') as f_read:
        task_read = f_read.readlines()
        print("""\n____________________________________________________

The task overview report is as follows:
____________________________________________________\n""")
        for line in task_read:
            print(line)

    print("""\n_____________________________________________________

The user overview report is as follows:
_____________________________________________________\n""")

    with open('user_overview.txt', 'r') as f_read1:
        user_read = f_read1.readlines()
        for line in user_read:
            print(line)

    print("""\n______________________________________________________

End of Statistics Reports
______________________________________________________\n""")


# ====Login Section====
with open("user.txt", "r") as file:
    login = file.readlines()

    user_dict = {}
    usernames_lst = []
    passwords_lst = []
    for line in login:
        login_details = line.split(', ')
        usernames_lst.append(login_details[0])
        passwords_lst.append(login_details[1].strip("\n"))
        user_dict["Usernames"] = usernames_lst
        user_dict["Passwords"] = passwords_lst  # {'Usernames': ['admin', 'bhavya'], 'Passwords': ['adm1n', 'bhavya1']}

    print("'Login to the task manager website'")

    username_in = input("Enter your username: ")
    Login_invalid = True
    while Login_invalid:
        if username_in not in usernames_lst:
            print("The username is incorrect.")
            username_in = input("Enter your username: ")
        else:
            print("The username is correct.")
            password_in = input("Enter your password: ")
            password_invalid = True
            while password_invalid:
                if password_in not in passwords_lst:
                    print("Your username is correct but your password is incorrect.")
                    password_in = input("Enter your password: ")
                else:
                    print("Your password is correct. Login is successful")
                    password_invalid = False
            Login_invalid = False


# Creating the dict for tasks.txt file which will be useful for generate report.
tasks_dict = {}
count = 1
with open('tasks.txt', 'r') as f_read:
    for line in f_read:
        newline = line.rstrip('\n')
        split_line = newline.split(", ")
        tasks_dict[f"Task {count} details:"] = split_line
        # eg {'Task 7 details:': ['bhavya', 'Capstone Project III', 'Capstone Project III test continue', '05 Jan 2023', '10 Jan 2023', 'Yes']}
        count += 1

# main menu is differentiated for admin and other users by only admin can register new user, generate report and display statistics.
while True:
    if username_in == "admin":
        menu = input('''\nSelect one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()
    else:
        menu = input('''\nSelect one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == 'gr':
        generate_reports()

    elif menu == 'ds':
        while True:
            try:
                check_file = open('user_overview.txt', 'r')
                display_statistics()
                check_file.close()
                break
            except FileNotFoundError as error:
                print("\nThe file that you are trying to open does not exist")
                generate_reports()

    elif menu == 'e':
        print('Goodbye!!! You are successfully logout.')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
