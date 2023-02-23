class BankCard:
    __serial_number = "1111 2222 3333 4444"  # private-переменная
    __pin = 955  # private-переменная

    def __get_pin(self):  # private-метод
        print("My pin is : ", self.__pin)


bank_card = BankCard()
bank_card._BankCard__get_pin()
bank_card._BankCard__serial_number = "2222 3333 4444 66666"
print("New serial number is ", bank_card._BankCard__serial_number)
