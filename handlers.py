from transactions import*
class WithdrawHandler:
    def __init__(self, keypad, screen):
        self.keypad = keypad
        self.screen = screen
    def handle(self, account):
        while True:
            amount = self.keypad.get_input("Enter The amount to withdraw: ")
            try:
                amount = float(amount)
                if amount <= 0:
                    self.screen.show_message("Invalid amount, Please enter positive amount")
                    continue
                transaction = WithdrawTransaction(amount)
                transaction.execute(account)
                break
            except ValueError:
                self.screen.show_message("Invalid input, Please enter valid amount: ")
class DepositHandler:
    def __init__(self, keypad, screen):
        self.kaypad = keypad 
        self.screen = screen
    def handle(self,account):
        while True:
            amount = self.kaypad.get_input("Enter the amount to deposite: ")
            try:
                amount = float(amount)
                if amount <= 0:
                    self.screen.show_message("Invalid amount , Please enter positive amount: ")
                    continue
                transaction = DepositTransaction(amount)
                transaction.execute(account)
                break
            except ValueError:
                self.screen.show_message("Invalid input, Please enter valid amount: ")
class BalanceInquiryHnandler:
    def handle(self, account):
        transaction = BalanceInqueryTransaction()
        transaction.execute(account)
class TransactionHistoryHandler:
    def handle(self, account):
        account.display_transaction_history()
class PinChangerHandler:
    def __init__(self, keypad, screen):
        self.keypad = keypad
        self.screen = screen
    def handle(self, account):
        old_pin = self.keypad.get_input("Enter your current PIN: ", secure = True)
        new_pin = self.keypad.get_input("Enter you new PIN: ", secure = True)
        confirm_new_pin = self.keypad.get_input("Confirm your new PIN: ", secure = True)
        if new_pin != confirm_new_pin:
            self.screen.show_message("PINs don't matches, Please try again: ")
            return
        if account.linked_card.set_pin(old_pin, new_pin):
            self.screen.show_message("PIN changed successfully")
        else:
            self.screen.show_message("Incorrect Pin, Please enter right PIN: ")
class TransferHandler:
    def __init__(self, keypad, screen, bank):
        self.keypad = keypad
        self.screen = screen
        self.bank = bank
    def handle(self, account):
        while True:
            amount = self.keypad.get_input("Please enter amount to transfer: ")
            destination_account_number = self.keypad.get_input("Enter the destination account number: ")
            try:
                amount = float(amount)
                if amount <= 0:
                    self.screen.get_input("Invalid amount , Please enter possitive value: ")
                    continue
                transaction = TransferTransaction(amount, destination_account_number)
                transaction.execute(account, self.bank)
            except ValueError:
                self.screen.show_message("Invalid input , Please enter valid input: ")