import sys

class Bank:

    global username
    global password
    global account_balance

    def __init__(myObject):
        myObject.username = 'linkesh'
        myObject.password = '1234'
        myObject.account_balance = 5000

    def cash_withdraw(myObject, amount):
        if(int(amount) <= myObject.account_balance):
            myObject.account_balance = myObject.account_balance - int(amount)
            print("You Withdraw : " + str(amount))
            print("Your Account Balance : " + str(myObject.account_balance))
        else:
            print("Insufficient Balance")

    def cash_credit(myObject, amount):
        myObject.account_balance = myObject.account_balance + int(amount)
        print("Your account has been Credited : " + str(amount))
        print("Your Account Balance : " + str(myObject.account_balance))

    def change_password(myObject):
        newpwd = input("Please Enter Your New Password : ")
        cnfpwd = input("Please Enter Your Confirm Password : ")
        if(newpwd == cnfpwd):
            myObject.password = newpwd
            print("Password Updated Successfully!!")
        else:
            print("New Password and Confirm Password Should Match")

if __name__ == "__main__":
    myObject = Bank()    
    print("Welcome to Bank of Edureka!")
    un = input("Please Enter Your UserName : ")
    pwd = input("Please Enter Your Password : ")
    if(un == myObject.username and pwd == myObject.password):
        print("Welcome Mr.Linkesh! Please Select the Option from below!!")
        print("Press 1 for Cash Withdrawal")
        print("Press 2 for Cash Deposit")
        print("Press 3 for Change Password")
        choice = input("Please Enter Your Choice : ")
        if ( choice == '1'):
            amt = input("Please Enter the amount you wish to withdraw : ")
            myObject.cash_withdraw(amt)
        elif( choice == '2'):
            amt = input("Please Enter the amount you wish to deposit : ")
            myObject.cash_credit(amt)
        elif( choice == '3'):
            myObject.change_password()
        else:
            print("Invalid Option! Thank You for Banking with Us!!")
    else:
        print("Invalid Username/Password. Please try again Later!!")
    print("Thank You for Banking with Us!!")
