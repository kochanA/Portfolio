class User:
    def __init__(self, name, pin, is_logged_in=False):
        self.name = name
        self.pin = pin
        self.is_logged_in = is_logged_in
        self.bank_account = self
        self.bank_account.user = self

    def log_in(self, name, pin):
        if name == self.name and pin == self.pin:
            if not self.is_logged_in:
                self.is_logged_in = True
                print(f"Welcom {self.name}, login was successful.")
            else:
                print(f"You are already logged in.")
        else:
            print('Incorect data')

    def log_out(self):
        if self.is_logged_in:
            self.is_logged_in = False
            print(f"Goodbye {self.name}, you have been logged out successfully.")
        else:
            print(f"You can not be logged out, because you are not log in")

    @property
    def logged_status(self):
        return True if self.is_logged_in else False


def logged_status(func):
    def check_login(self, *args):
        if self.bank_account.user.logged_status:
            return func(self, *args)
        print("Not logged in")

    return check_login


class BankAccount:
    def __init__(self, user):
        self._amount = 0
        self.user = user

    def _add_money(self, amount):
        self._amount += amount

    def _withdraw_money(self, amount):
        self._amount -= amount

    @property
    def balance(self):
        return self._amount


class CreditCard:

    def __init__(self, bank_account):
        self.bank_account = bank_account

    def add_money(self, amount, pin):
        if pin == self.bank_account.user.pin:
            self.bank_account._add_money(amount)
            print(f"Account balance: {self.balance}")
        else:
            print("Wrong password.")

    def pay(self, amount, pin):
        if pin == self.bank_account.user.pin:
            if amount <= self.balance:
                self.bank_account._withdraw_money(amount)
                print(f"Account balance: {self.balance}")
            else:
                print("Insufficient balance !!!")
        else:
            print("Wrong password.")

    @property
    def balance(self):
        return self.bank_account._amount


class PhoneApp:
    def __init__(self, bank_account):
        self.bank_account = bank_account

    @logged_status
    def account_balance(self):
        print(f"Account balance: {self.balance}")

    @logged_status
    def pay_with_blik(self, amount, phone_number):
        if amount <= self.balance:
            self.bank_account._withdraw_money(amount)
            lenght_phone_number = len(phone_number.replace(" ", ""))
            if lenght_phone_number == 9:
                print(f"Money sent to {phone_number}")
                print(f"Account balance: {self.balance}")
            else:
                print("Wrong phone number.")
        else:
            print("Insufficient balance !!!")

    @logged_status
    def wire_tranfer(self, amount, account_number):
        if amount <= self.balance:
            self.bank_account._withdraw_money(amount)
            # czy wystarczy takie sprawdzenie nr konta ?
            lenght_account_number = len(account_number.replace(" ", ""))
            if lenght_account_number == 26:
                print(f"Money sent to {account_number}")
                print(f"Account balance: {self.balance}")
            else:
                print("Wrong account number.")
        else:
            print("Insufficient balance !!!")

    @property
    def balance(self):
        return self.bank_account._amount


user_1 = User("Alicja", "4651")
user_2 = User("Michal", "0010")

if __name__ == '__main__':
    user = user_1
    bank_account = BankAccount(user)
    credit_card = CreditCard(bank_account)
    phone_app = PhoneApp(bank_account)

    user.log_in("Alicja", "4651")
    credit_card.add_money(500, '4651')
    credit_card.pay(200, '4651')
    phone_app.account_balance()
    phone_app.pay_with_blik(100, "500 620 010")
    phone_app.wire_tranfer(20, "78 8491 8481 4712 6485 9312 0547")
    user.log_out()