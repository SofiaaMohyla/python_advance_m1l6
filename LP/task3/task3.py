"""
Проблема в поточній реалізації класу OrderProcessor полягає в тому, що він
 використовує безпосередньо конкретні сервіси (EmailService та SMSService)
 для відправки повідомлень. Це може призвести до проблем при зміні або розширенні типів повідомлень.

Чи розглядали ви можливість абстрагувати логіку відправки повідомлень в
окремий інтерфейс чи абстрактний клас, що дозволить легше заміняти та
 розширювати функціональність в майбутньому?
"""

class EmailService:
    def send_email(self, recipient, message):
        print(f"Sending email to {recipient}: {message}")


class SMSService:
    def send_sms(self, recipient, message):
        print(f"Sending SMS to {recipient}: {message}")


class OrderProcessor:
    def __init__(self):
        self.email_service = EmailService()
        self.sms_service = SMSService()

    def process_order(self, order_id, recipient, method):
        print(f"Processing order {order_id}")
        if method == "email":
            self.email_service.send_email(recipient, f"Your order {order_id} has been processed.")
        elif method == "sms":
            self.sms_service.send_sms(recipient, f"Your order {order_id} has been processed.")


processor = OrderProcessor()
processor.process_order(1, "customer@example.com", "email")
processor.process_order(2, "123-456-7890", "sms")
