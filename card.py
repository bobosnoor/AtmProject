class Card:
    def __init__(self, number, pin):
        self.__pin = pin
        self.number = number
    def get_pin(self):
        return self.__pin
    def set_pin(self, old_pin, new_pin):
        if self.__pin == old_pin:
            self.__pin = new_pin
            return True
        else:
            return False