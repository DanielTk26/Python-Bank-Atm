class Atm:
   
  def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

  def check_balance(self):
        print("Your balance is 5,60,000")
  
  def withdrawl(self,amount):
        new_amount = 50000 - amount
        print("You have withdrawn an amount of "+str(amount) +". Your remaining balance is "+ str(new_amount))


def main():
    Card_number = input("Insert your valid card number:- ")
    pin_number  = input("Enter your pin :- ")

    new_user =  Atm(Card_number ,pin_number)

    print("Choose your action ")
    print("1.Balance Enquriy   2.Withdrawl")
    activity = int(input("Enter Action number :- "))

    if (activity == 1):
        new_user.check_balance()
    
    elif (activity == 2):
        amount = int(input("Enter the amount to be withdrawed:- "))
        new_user.withdrawl(amount)
    
    else:
        print("Kindly Enter a valid number")


if __name__ == "__main__":
    main()


