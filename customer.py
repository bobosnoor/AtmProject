class Customer:
    def __init__(self,name, phone, email, address):
        self.name= name
        self.phone = phone
        self.email = email
        self.address = address
        self.accounts = {}
    def add_account(self, account):
        self.accounts[account.account_number] = account