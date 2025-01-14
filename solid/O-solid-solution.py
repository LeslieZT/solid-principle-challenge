from abc import ABC, abstractmethod
class PaymentMethodInterface(ABC):
    def __init__(self, amount):
        self.amount = amount
            
    @abstractmethod
    def calculate_fee(self) -> float:
        pass
    
class CreditCard(PaymentMethodInterface):
    def calculate_fee(self) -> float:
        return self.amount * 0.03

class PayPal(PaymentMethodInterface):
    def calculate_fee(self) -> float:
        return self.amount * 0.05
    
class BankTransfer(PaymentMethodInterface):
    def calculate_fee(self) -> float:
        return 2.50

class UnknownPaymentMethod(PaymentMethodInterface):
    def calculate_fee(self) -> float:
        return 0.0

class FeeCalculator:
    @staticmethod
    def calculate_fee(payment_method: PaymentMethodInterface):
        return payment_method.calculate_fee()

if __name__ == "__main__":
    credit_card = CreditCard(100)
    paypal = PayPal(100)
    bank_transfer = BankTransfer(100)
    unknown_payment_method = UnknownPaymentMethod(100)
    print(f"Credit Card Fee: {FeeCalculator.calculate_fee(credit_card)}")
    print(f"PayPal Fee: {FeeCalculator.calculate_fee(paypal)}")
    print(f"Bank Transfer Fee: {FeeCalculator.calculate_fee(bank_transfer)}")
    print(f"Unknown Payment Method Fee: {FeeCalculator.calculate_fee( unknown_payment_method)}")