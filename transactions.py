from enum import Enum
from abc import ABC, abstractmethod
import uuid
import datetime

class TransactionType(Enum):
    WITHDRAW = "withdraw"
    DEPOSIT = "deposit"
    BALANCE_INQUIRY = "balance_inquiry"
    TRANSFER = "transfer"
class Transaction(ABC):
    def __init__(self, transaction_type, amount = None):
        self.transaction_type = transaction_type
        self.amount = amount
        self.transaction_id = uuid.uuid4()
        self.time_stamp = datetime.datetime.now()
    @abstractmethod
    def execute(self):
        pass
class WithdrawTransaction(Transaction):
    def __init__(self, amount=None):
        super().__init__(TransactionType.WITHDRAW, amount)
        self.amount = amount
    def execute(self, account):
        if account.balance >= self.amount:
            account.balance -= self.amount
            print(f"Withdraw succsessful your balance is {account.balance}")
            account.add_transaction(self)
        else:
            print("insufficient funds")
class DepositTransaction(Transaction):
    def __init__(self, amount):
        super().__init__(TransactionType.DEPOSIT, amount)
        self.amount = amount
    def execute(self, account):
        account.balance +=  self.amount
        print(f"Deposit success you balance is {account.balance}")
        account.add_transaction(self)
class BalanceInqueryTransaction(Transaction):
    def __init__(self):
        super().__init__(TransactionType.BALANCE_INQUIRY, amount=0)       
    def execute(self, account):
        self.amount = account.balance
        print(f"you balance is {account.balance}")
        account.add_transaction(self)
class TransferTransaction(Transaction):
    def __init__(self, amount, destination_account_number):
        super().__init__(TransactionType.TRANSFER, amount)
        self.destination_account_number = destination_account_number
    def execute(self, account, bank):
        if account.balance >= self.amount:
            destination_account = bank.accounts.get(self.destination_account_number)
            if destination_account:
                account.balance -= self.amount
                destination_account.balance += self.amount
                print(f"Transfer successful, New balance {account.balance} ")
            else:
                print("Destination account isn't found.")
        else:
            print("insufficient funds")