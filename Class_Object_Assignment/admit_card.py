class AdmitCard:
    total_cards_issued = 0

    def __init__(self, app_number=1001, app_name=None):
        self.app_number = app_number
        self.app_name = app_name
        AdmitCard.total_cards_issued += 1

    def set_info(self, app_number, app_name):
        self.app_number = app_number
        self.app_name = app_name

    def set_app_number(self, app_number):
        self.app_number = app_number

    def set_app_name(self, app_name):
        self.app_name = app_name

    def get_info(self):
        return f"Application number is {self.app_number} and the name of the applicant is {self.app_name}"

    def get_app_number(self):
        return f"Application number is {self.app_number}"

    def get_app_name(self):
        return f"Application name is {self.app_name}"

    @classmethod
    def display_total_cards(cls):
        print(f"Total number of cards is {cls.total_cards_issued}")

    def display_address(self, address):
        print(f"Applicant address is {address}")


if __name__ == "__main__":
    print("Default value of Admit Card")
    card1 = AdmitCard()
    print(card1.get_app_number())
    print(card1.get_app_name())

    card2 = AdmitCard()
    card2.set_info(1002, "Khit Khit")
    print(card2.get_info())

    card3 = AdmitCard()
    card3.set_info(1004, "Thit Thit")
    print(card3.get_info())

    print("After changing name and number for this card")
    card4 = AdmitCard()
    card4.set_info(1020, "Yu Yu")
    print(card4.get_info())

    card5 = AdmitCard()
    card5.set_info(1025, "Po Po")
    print(card5.get_info())

    card6 = AdmitCard()
    card6.set_info(3000, "Tu Tu")
    print(card6.get_info())

    AdmitCard.display_total_cards()
