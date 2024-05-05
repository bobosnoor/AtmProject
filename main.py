from account import Account
from bank import Bank
from customer import Customer
from card import Card
from atm_interrface import AtmInterface
from card_reader import CardReader
def main():
    bank1 = Bank('bca', "BRINIDJA")
    customer_1 = Customer('lina', '087782288608', 'lina@gmail.com', 'Dusun mekarjati')
    account_1 = Account("535278104")
    account_2 = Account("55555")
    card1 = Card("12879876610018", "248163")
    customer_1.add_account(account_1)
    customer_1.add_account(account_2)
    bank1.add_customer(customer_1)
    account_1.link_card(card1)
    atm = AtmInterface(bank1, "pamanukan")
    card_reader = CardReader(atm)
    card_reader.insert_card(card1)
if __name__ == "__main__":
    main()




    



