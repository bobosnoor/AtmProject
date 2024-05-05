from keypad import Keypad
from screen import Screen
from handlers import *

class AtmInterface:
    def __init__(self, bank, atm_location):
        self.keypad = Keypad()
        self.screen = Screen()
        self.bank = bank
        self.atm_location = atm_location
        self.withdraw_handler = WithdrawHandler(self.keypad, self.screen)
        self.deposit_handler = DepositHandler(self.keypad, self.screen)
        self.balance_inquiry_handler = BalanceInquiryHnandler()
        self.transaction_history_handler = TransactionHistoryHandler()
        self.pin_changer_handler = PinChangerHandler(self.keypad, self.screen)
        self.transfer_handler = TransferHandler(self.keypad, self.screen, bank)
    def display_main_menu(self,account):
        message = """
        1. Withdraw
        2. Deposite
        3. Balance Inquiry
        4. View Transactions
        5. Change Pin
        6. Transfer funds
        7. Exit
        Choose an option: """
        while True:
            choice = self.keypad.get_input(message)
            match choice:
                case "1":
                    self.withdraw_handler.handle(account)
                case "2":
                    self.deposit_handler.handle(account)
                case "3":
                    self.balance_inquiry_handler.handle(account)
                case "4":
                    self.transaction_history_handler.handle(account)
                case "5":
                    self.pin_changer_handler.handle(account)
                case "6":
                    self.transfer_handler.handle(account)
                case "7":
                    self.screen.show_message("Enjecting card....\nGood bye.")
                case _:
                    self.screen.show_message("Invalid Choice, Please try again.")
            self.keypad.get_input("Press Enter to continue: ")
            self.screen.clear_screen()