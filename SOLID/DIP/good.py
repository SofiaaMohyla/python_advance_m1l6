from abc import ABC, abstractmethod

class IPaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class MonobankPaymentProcessor(IPaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of {amount} through Monobank.")

class PrivatBankPaymentProcessor(IPaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of {amount} through PrivatBank.")

class PaymentService:
    def __init__(self, processor: IPaymentProcessor):
        self.processor = processor

    def process_payment(self, amount):
        self.processor.process_payment(amount)

# Використання
monobank_processor = MonobankPaymentProcessor()
privatbank_processor = PrivatBankPaymentProcessor()

payment_service = PaymentService(monobank_processor)
payment_service.process_payment(100)

payment_service = PaymentService(privatbank_processor)
payment_service.process_payment(200)
