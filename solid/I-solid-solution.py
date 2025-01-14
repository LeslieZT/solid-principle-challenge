from abc import ABC, abstractmethod

class PaymentInterface(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

class RefundInterface(ABC):
    @abstractmethod
    def refund(self, amount: float) -> None:
        pass

class DisputeInterface(ABC):
    @abstractmethod
    def handle_dispute(self, dispute_id: str) -> None:
        pass

class BasicGiftCard(PaymentInterface):
    def pay(self, amount: float) -> None:
        print(f"Gift card used to pay {amount}.")

class GoldenGiftCard(PaymentInterface, RefundInterface, DisputeInterface):
    def pay(self, amount: float) -> None:
        print(f"Refundable gift card used to pay {amount}.")

    def refund(self, amount: float) -> None:
        print(f"Refund of {amount} requested for the Refundable gift card.")

    def handle_dispute(self, dispute_id: str) -> None:
        print(f"Dispute {dispute_id} handled by the Refundable gift card.")

if __name__ == "__main__":
    gift_card = GoldenGiftCard()
    gift_card.pay(100)
    gift_card.refund(50)
    gift_card.handle_dispute("123456789")