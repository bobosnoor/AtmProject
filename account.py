class Account:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0
        self.linked_card = None
        self.transaction_history = []
    def add_transaction(self,transaction):
        self.transaction_history.append(transaction)
    def link_card(self, card):
        self.linked_card = card
    def display_transaction_history(self):
        if not self.transaction_history:
            print("No transactions available")
            return
        print("Transaction history\n")
        for transaction in self.transaction_history:
            print(f"ID: {transaction.transaction_id}\nType: {transaction.transaction_type.value}\nAmount: {transaction.amount}\nTime: {transaction.time_stamp}\n")