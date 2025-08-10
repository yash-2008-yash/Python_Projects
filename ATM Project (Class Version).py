#program to credit or debit money and check the balance

class Account:

    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no

    #debit method
    def debit(self,balance,deb_amt):
        rem=balance-deb_amt
        print(deb_amt,"Rupees debited from your account")
        print("Remaining balance :",rem,"Rupees")

    #credit method
    def credit(self,balance,cre_amt):
        new_balance=balance+cre_amt
        print(cre_amt,"Rupees credited into your account")
        print("New balance :",new_balance,"Rupees")
 
cstmr=Account(10000,2008)
