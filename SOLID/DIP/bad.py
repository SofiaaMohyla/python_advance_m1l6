class MonobankPaymentProcessor:
    def process_payment(self, amount):
        print(f"Processing payment of {amount} through Monobank.")


class PrivatBankPaymentProcessor:
    def process_payment(self, amount):
        print(f"Processing payment of {amount} through PrivatBank.")


class PaymentService:
    def __init__(self, bank_name):
        self.bank_name = bank_name

    def process_payment(self, amount):
        if self.bank_name == "Monobank":
            processor = MonobankPaymentProcessor()
        elif self.bank_name == "PrivatBank":
            processor = PrivatBankPaymentProcessor()
        else:
            raise ValueError("Unknown bank name")

        processor.process_payment(amount)


# Використання
payment_service = PaymentService("Monobank")
payment_service.process_payment(100)

payment_service = PaymentService("PrivatBank")
payment_service.process_payment(200)
