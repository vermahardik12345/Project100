class atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin
    def balanceinquiry(self):
        print('Your balance is Rs.200:')
    def cashwithdrawl(self,amount):
        new_amount=200-amount
        print('Your withdrawl'+str(amount)+"Your remaining balance is Rs."+str(new_amount))    
def main():
    name=input("What is your name:")    
    print('Hello'+name)
    cardnumber=input("Insert your cardnumber:")
    pin=input('Enter your pin:')
    new_user=atm(cardnumber,pin)

    print('Choose your activity') 
    print('1 for enquiry')
    print('2 for withdrawl')
    activity=int(input('Choose activity:'))

    if(activity==1):
        new_user.balanceinquiry() 
    elif(activity==2):
        amount=int(input('Enter the amount:')) 
        new_user.cashwithdrawl(amount)
    else:
        print('Enter a valid no.')    
 
if __name__ =='__main__':
    main()