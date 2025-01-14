from abc import ABC, abstractmethod

class PaymentInterface(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

class PaymentAndRefundInterface(PaymentInterface):
    @abstractmethod
    def refund(self, amount: float) -> None:
        pass

class PaymentMethod(PaymentAndRefundInterface):
    def __init__(self, balance: float):
        self.balance = balance

    def pay(self, amount: float):
        if amount > self.balance:
            raise ValueError("Not enough balance.")
        self.balance -= amount
        print(f"[PaymentMethod] Paid {amount}. New balance: {self.balance}")

    def refund(self, amount: float):
        self.balance += amount
        print(f"[PaymentMethod] Refunded {amount}. New balance: {self.balance}")
        
class NonRefundableGiftCard(PaymentInterface):
    def pay(self, amount: float) -> None:
        print(f"Gift card used to pay {amount}.")
        

if __name__ == "__main__":
    gift_card = NonRefundableGiftCard()
    gift_card.pay(100)
    payment_method = PaymentMethod(100)
    payment_method.pay(50)
    payment_method.refund(25)