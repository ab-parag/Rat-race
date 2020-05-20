import time

class ratRace:
    '''
    Rat race 1.1.2
    This game is a simulation of player's monthly income and expence chart. Player has to provide his salary, monthly expenses & liabilities (if any) along with its tenure during registration.
    Player will have option to spend the remaining balance of creating assets and/or other stuff
    Target of the player is to 
    '''
    user=''
    salary=0
    balance=0
    month=1

    expenses=[['Education Loan',10000,60],
          ['Monthly Expence',5000,600],
          ['Room rent',5600,240]
         ]

    spendingChoices=[['Fixed Deposit - Monthly payout interest 0.5%'],
                     ['Recurring Deposit - cumulative monthly interest of 0.3%'],
                     ['Liquor - standard rate 700 Rs per bottle'],
                     ['Purchase a 2 wheeler vehicle - 5k down payment and 3000 EMI for next 36 months'],
                     ['Don\'t want to spend yet']
        ]

    Assets=[]
    Collections=[]
    
    def __init__(self,u,s):
        self.user=u
        self.salary=s
        self.Collections.append(['Salary', s])
        print('Welcome to rate race, '+str(self.user))

    def passMonth(self):
        print('-----------------------\n'+str(self.month)+'th Month\n-----------------------')
        self.showCollections()
        #print('You salary has been creadited rs '+ str(self.salary)+' INR')
        #self.balance=self.balance+self.salary
        print('Updated balance:' + str(self.balance))
        paymentStatus=0

        print('Your expences are:')
        for idx, exp in enumerate(self.expenses):
            print(str(idx+1) + ' ' + str(exp[0])+ ' = Rs ' + str(exp[1]) + ' INR')

        print('Enter expence number you want to pay - ')
        
        dummyExpenses = self.expenses
        expStatus=['Unpaid' for i in range(len(dummyExpenses))]
        while(paymentStatus < len(dummyExpenses)+1):
            i=int(input())
            if i==1 and expStatus[0] == 'Unpaid':
                self.balance=self.balance-dummyExpenses[0][1]
                print('Paid Rs '+str(dummyExpenses[0][1])+'/- for '+str(dummyExpenses[0][0])+'. Updated Balance = '+str(self.balance))
                paymentStatus=paymentStatus+1
                expStatus[0]='Paid'
            elif i==2 and expStatus[1] == 'Unpaid':
                self.balance=self.balance-dummyExpenses[1][1]
                print('Paid Rs '+str(dummyExpenses[1][1])+'/- for '+str(dummyExpenses[1][0])+'. Updated Balance = '+str(self.balance))
                paymentStatus=paymentStatus+1
                expStatus[1]='Paid'
            elif i==3 and expStatus[2] == 'Unpaid':
                self.balance=self.balance-dummyExpenses[2][1]
                print('Paid Rs '+str(dummyExpenses[2][1])+'/- for '+str(dummyExpenses[2][0])+'. Updated Balance = '+str(self.balance))
                paymentStatus=paymentStatus+1
                expStatus[2]='Paid'
            elif i==4:
                if paymentStatus==len(dummyExpenses):
                    print('Done all the payments for '+str(self.month)+'th Month.\nRemaining balance = '+str(self.balance)+'\n\n')
                    self.month=self.month+1
                    break
                else:
                    print('You have not paid all the bills for this month. Try again...')
            else:
                print('Either you provided Invalid input, or you selected an expense which was already paid. Please try again')
                
    def spendMoney(self):
        while(True):
            print('You can choose to spend your remaining balance (Rs '+str(self.balance)+' INR) on below items:\n')
            for idx, spd in enumerate(self.spendingChoices):
                print( str(idx+1) + ' ' + str(spd[0]))
            print('\nEnter option# you want to spend on - ')
            i=int(input())
            if i==1:
                print('Enter the amount you want to put in Fixed deposite:')
                amt=int(input())
                if amt<self.balance:
                    self.Assets.append(['Fixed Deposit',amt])

                    self.balance = self.balance - amt

                    self.Collections.append(['Fixed Deposit',amt])
                    
                    print('\nCongratulations!! You\'ve created an assest:')
                    print(str(self.Assets[-1][0]) + ' '+ str(self.Assets[-1][1]))
                    print('\nYour updated balance is '+str(self.balance)+'\n')
                    time.sleep(1)
                else:
                    print('Insufficient fund, Please try again\n')
                    time.sleep(1)
            elif i==5:
                print('You chose to hold the cash with you. Good Luck')
                break
            else:
                print('Invalid input. please try again')

    def startRace(self, m):
        print('Starting the race for '+str(m)+' months time')
        for m in range(m):
            self.passMonth()
            time.sleep(1)
            if self.balance>0:
                self.spendMoney()
            else:
                print('Sorry, you ran out of balance!')
                break
            print()
            self.showAssets()
            time.sleep(3)
        print('You are leaving with total balance: '+str(self.balance))

    def showAssets(self):
        print('Hello '+str(self.user)+' you own below Assets:')
        for asset in self.Assets:
            print(str(asset[0]) + ' ' + str(asset[1]))

    def showCollections(self):
        print('Hello '+str(self.user)+' your onthly collections are:')
        for coll in self.Collections:
            if 'Fixed' in coll[0]:
                print('FD interest: ' + str((coll[1]*0.5)/100) + ' INR')
                self.balance=self.balance + float(((coll[1]*0.5)/100))
            if 'Salary' in coll[0]:
                print('Salary: '+ str(self.salary))
                self.balance=self.balance + self.salary

#----------------------
ob=ratRace('Mr A',21410.5)
ob.showAssets()
ob.startRace(2)
