from abc import *
#from abc import ABC, abstractmethod

class MoneyChanger(ABC):
    @abstractmethod
    def convert(self, dollars):
        pass

class USDToRupee(MoneyChanger):
    def convert(self, dollars):
        exchange_rate = 75.0  # 1 USD to INR
        return dollars * exchange_rate

class USDToBaht(MoneyChanger):
    def convert(self, dollars):
        exchange_rate = 32.0  # 1 USD to THB
        return dollars * exchange_rate

class USDToKyat(MoneyChanger):
    def convert(self, dollars):
        exchange_rate = 1500.0  # 1 USD to MMK
        return dollars * exchange_rate


dollars = float(input("Enter the amount in dollars: "))

rupee_converter = USDToRupee()
baht_converter = USDToBaht()
kyat_converter = USDToKyat()

rupees = rupee_converter.convert(dollars)
baht = baht_converter.convert(dollars)
kyats = kyat_converter.convert(dollars)

print('Equavalent Dollar to ruppes',rupees)
print('Equavalent Dollar to baht',baht)
print('Equavalent Dollar to kyats',kyats)
    
