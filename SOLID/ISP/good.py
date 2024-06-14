from abc import ABC, abstractmethod


class CallingDevice(ABC):
    @abstractmethod
    def make_calls(self):
        pass


class MessagingDevice(ABC):
    @abstractmethod
    def send_sms(self):
        pass


class InternetBrowsingDevice(ABC):
    @abstractmethod
    def browse_internet(self):
        pass


class SmartPhone(CallingDevice, MessagingDevice, InternetBrowsingDevice):
    def make_calls(self):
        print("Здійснення дзвінків зі смартфону")

    def send_sms(self):
        print("Відправлення SMS зі смартфону")

    def browse_internet(self):
        print("Перегляд інтернету зі смартфону")


class LandlinePhone(CallingDevice):
    def make_calls(self):
        print("Здійснення дзвінків з стаціонарного телефону")
