from abc import ABC, abstractmethod

class CommunicationDevice(ABC):
    @abstractmethod
    def make_calls(self):
        pass

    @abstractmethod
    def send_sms(self):
        pass

    @abstractmethod
    def browse_internet(self):
        pass

class SmartPhone(CommunicationDevice):
    def make_calls(self):
        print("Здійснення дзвінків зі смартфону")

    def send_sms(self):
        print("Відправлення SMS зі смартфону")

    def browse_internet(self):
        print("Перегляд інтернету зі смартфону")

class LandlinePhone(CommunicationDevice):
    def make_calls(self):
        print("Здійснення дзвінків з стаціонарного телефону")

    def send_sms(self):
        print("Стаціонарний телефон не підтримує SMS")

    def browse_internet(self):
        print("Стаціонарний телефон не підтримує інтернет")
