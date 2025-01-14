from abc import ABC, abstractmethod

class PaymentInterface(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass    

class PayPalService(PaymentInterface):
    def pay(self, amount: float):
        print(f"Paying {amount} using PayPal...")

class PaymentProcessor:
    def __init__(self, payment_service: PaymentInterface):
        self.payment_service = payment_service

    def process_payment(self, amount: float):
        self.payment_service.pay(amount)


if __name__ == "__main__":
    payment_service = PayPalService()
    payment_processor = PaymentProcessor(payment_service)
    payment_processor.process_payment(100)