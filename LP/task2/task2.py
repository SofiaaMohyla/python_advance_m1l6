"""
Чи бачите ви можливість відокремити обробку різних типів повідомлень
у класі MessageSender, щоб полегшити додавання нових типів без змінення поточного коду?
"""

class MessageSender:
    def send_message(self, message_type, recipient, message):
        if message_type == "email":
            self.send_email(recipient, message)
        elif message_type == "sms":
            self.send_sms(recipient, message)

    def send_email(self, recipient, message):
        print(f"Sending email to {recipient}: {message}")

    def send_sms(self, recipient, message):
        print(f"Sending SMS to {recipient}: {message}")


sender = MessageSender()
sender.send_message("email", "john@example.com", "Hello John!")
sender.send_message("sms", "123-456-7890", "Hello!")
