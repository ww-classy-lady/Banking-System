'''Wendy Wu'''
'''06/12/2023'''
def log_in(accounts):
    success = False
    name = input("Enter the name: ")
    password = input("Enter the password: ")
    for key in accounts.keys():
        if name == key:
            if accounts[key] == password:
                success = True
                break
    return success
    
def create_account(accounts,amounts):
    name = input("Please enter your name: ")
    password = input("Please enter the password for your account: ")
    money = int(input("Enter your starting value: "))
    accounts[name] = password
    amounts[name] = money
    print("Account successfully created")
def delete_account(accounts,amounts):
    name = "Enter the user's name to delete the account: "
    accounts.pop(name) 
    amounts.pop(name)
    print("Account deleted successfully")
def retrieve_money(accounts,amounts):
    value = 0
    if log_in(accounts):
        name = input("Enter your name again please: ")
        value = int(input("Enter the value to retrieve: "))
        if amounts[name] > value:
            amounts[name] = amounts[name] - value
            print("Your balance is now: " , str(amounts[name]))
        else:
            print("You have a deficit!")
    else:
        print("login failed, redirecting you to the main menu page...")
        
def input_money(accounts,amounts):    
    value = 0
    if log_in(accounts):
        name = input("Enter your name again please: ")
        value = int(input("Enter the value to retrieve: "))
        amounts[name] += value
        print("Your balance is now: " , str(amounts[name]))

    else:
        print("login failed, redirecting you to the main menu page...")
def update_account(accounts,amounts):
    password_temp = ""
    amount_temp = 0
    if log_in(accounts):
        print("1. Change name 2. Change password")
        choice = int(input("Please Enter your Choice: "))
        name = input("Enter your name: ")
        if choice == 1:
            new_name = input("Enter your new name please: ")
            password_temp = accounts[name]
            amount_temp = amounts[name]
            accounts.pop(name)
            amounts.pop(name)
            accounts[new_name] = password_temp
            amounts[new_name] = amount_temp
        elif choice == 2: 
            password = input("Enter your password")
            new_pass = input("Enter your new password please: ")
            accounts[name] = new_pass
        else:
            print("Not valid choice, redirecting you to the main menu page...")
    else:
        print("Not valid log in, redirecting you to the main menu page...")

def main():
    decision = 9
    accounts = {}
    amounts = {}
    '''name, password, and money amount '''
    ''' name and password -> key, value in dictionaries, then amount is the list'''
    while decision != 0:
        print("Welcome to the Best Online Banking Service in the World! (jk)")
        print("Menu of Operations:")
        print("1. Create a new account")
        print("2. Delete your account")
        print("3. Retrieve Money from your account")
        print("4. Input Money in your account")
        print("5. Update account information")
        print("6. See the Accounts and Amounts Dictionaries")
        print("0. Quit")
        decision = int(input("Please enter the number of choice: "))
        if decision == 1:
            create_account(accounts,amounts)
        elif decision == 2:
            delete_account(accounts,amounts)
        elif decision == 3:
            retrieve_money(accounts,amounts)
        elif decision == 4:
            input_money(accounts,amounts)
        elif decision == 5:
            update_account(accounts,amounts)
        elif decision == 6:
            print("Accounts: " , accounts, "Amounts: ", amounts)
        elif decision == 0:
            print("Thank you for banking with our Bank! Have a great day!")
        else:
            print("Please enter a valid option...")

if __name__ == "__main__":
    main()
