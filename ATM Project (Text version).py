#atm replica project by YASHWANTH

balance=int(input("Welcome to Y.A.S.H Banking Services\nThanks for choosing our bank\nAdd some amount to confirm your bank account : "))

name=input("\nYour bank account has been created successfully\nEnter your name : ")

print(f"\nWelcome {name}, your account number is 24042008\n")

password=input("Create a strong password : ")

enter_pass=input("\nPut your password to get banking services : ")

if enter_pass==password:

    choice=int(input("\n1.Check account balance\n2.Add amount to account\n3.Borrow amount from account\nEnter the service you want to get : "))
    
    if choice==1:
        print(f"\nYour current balance is {balance} Rupees.\nThank you. Visit again.\n")

    elif choice==2:
        credit_amt=int(input("\nEnter the amount you want to add : "))
        new_balance=balance+credit_amt
        print(f"\n{credit_amt} was successfully credited into your account\nYour new balance is {new_balance}\nThank you. Visit again\n")

    elif choice==3:
        debit_amt=int(input("\nEnter the amount you want to borrow : "))
        
        if debit_amt>balance:
            print("\nUnsufficient amount in your account.\nThank you. Visit again.\n")
        else:
            rem_balance=balance-debit_amt
            print(f"\n{debit_amt} was successfully debited from your account\nYour remaining balance is {rem_balance}\nThank you. Visit again\n")

    else:
        print("\nInvalid choice. Try again after some time.\n")

else:
    print("\nYour entered password is wrong\nTry again after some time\n")
