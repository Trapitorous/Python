class Mpesa:
    def __init__(self,account_balance,phone_number):
        self.phone_number=phone_number
        self.account_balance=account_balance
    def send_money(self,amount,recipient):
        if self.account_balance >=amount:
            self.account_balance -= amount
            print(f"{amount} KES sent to {recipient} was successfully sent")
        else:
            print("insufficient funds")
class personal_mpesa(Mpesa):
    def __init__(self,account_balance,phone_number,id_number):
        super().__init__(account_balance,phone_number)
        self.id_number = id_number
    def buyairtime(self,amount):
        if self.account_balance >=amount:
            print(f'{amount} KES airtime bought successfully')
        else:
            print("insufficient funds")

class business:
    def __init__(self,business_name,account_balance,phone_number,):
        super().__init__(account_balance,phone_number)
    def receive_money(self,amount):
        self.account_balance += amount
        print(f'{amount} Kes received successfully')
personal=personal_mpesa(500,88888888,22222)
personal.send_money(400,222222)



