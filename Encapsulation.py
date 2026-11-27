#Mobile Phone Balance System Using Encapsulation
class Mobile:
    def __init__(self):
        self.name = 'Honey Keerthana'
        self.balance = 100

    def recharge(self,amount):
        if amount > 0:
            self.balance += amount
            print('Recharge successful')
        else:
            print('Enter a valid amount')

    def make_call(self,charge):
        if charge > 0 and self.balance >= charge:
            self.balance -= charge
            print('Made call successfully')
        else:
            print('Insufficient Balance or Invalide charge')

    def check_balance(self):
        return self.balance

    def display_details(self):
        print('\n Mobile owner :',self.name)
        print('\n Current Balance :',self.check_balance())

user = Mobile()

while True:
    print('\n ------- MOBILE PHONE BALANCE SYSTEM -------')
    print('\n1. Recharge')
    print('\n2. Make Call')
    print('\n3. Check Balance')
    print('\n4. Display Details')
    print('\n5. Exit')
          
    choice = int(input('\n Enter a choice'))
                 
    if choice == 1:
        amount = int(input('Enter amount to recharge'))
        user.recharge(amount)

    elif choice == 2:
        charge = int(input("Enter Call Charge: "))
        user.make_call(charge)

    elif choice == 3:
        print("Current Balance:", user.check_balance())

    elif choice == 4:
        user.display_details()

    elif choice == 5:
        print("Thank you for using our service!")
        break

    else:
        print("Invalid Choice! Try Again.")                     
        
    
        
        
        
        
