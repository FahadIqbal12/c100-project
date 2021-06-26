import random
class Atm:
    def __init__(self,CardNo,Pin):
        self.CardNo = CardNo
        self.Pin = Pin

    def CashWithdraw(self):
        amount = int(input('Please Enter Amount : '))
       
        if (amount > 0) :
            print('Cash Withdrawn')    


    def Balance (self):
        balance = random.randint(10000,30000)
        print(balance)

atm = Atm(input('Please Enter Card No. : '),input('Please enter PIN Code : '))       
selection = int(input('If you want to check your balance enter 1 and if you want to withdraw cash enter 2 : '))

if (selection == 1):
    Atm.Balance(atm)

elif( selection == 2):
    Atm.CashWithdraw(atm)
else:
    print('Wrong Input')


