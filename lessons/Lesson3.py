class BankAccount:

    def __init__(self, login, password, balance):
        self.login = login
        self._balance = balance
        self.__password = password


    def get_balance(self, password):
        if password == self.__password:
            return self._balance
        else:
            return "Не верный пароль!!"

    def get_pass(self, password):
        if password == self.__password:
            return self.__password
        else:
            return "Не верный пароль!!"

    def _prot_method(self):
        return "prot"

    def __priv_method(self):
        return "priv"

    def get_priv_method(self):
        return self.__priv_method()


ardager = BankAccount("ardager", "123321", 1000)

# print(ardager.get_balance("123321"))
# print(ardager.login)
# print(ardager.get_pass("123321"))
# print(ardager._prot_method())
# print(ardager.get_priv_method())



from abc import ABC, abstractmethod



# Абстрактный класс
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def voice(self):
        pass

class Dog(Animal):

    def move(self):
        return "Step Step"

    def voice(self):
        return "Gaf Gaf"


class Donald(Dog):
    pass


gufi = Donald()

# print(gufi.move())
# print(gufi.voice())



class SmsOtp(ABC):
    @abstractmethod
    def send_sms_to_phone(self):
        pass



class SmsKr(SmsOtp):

    def send_sms_to_phone(self):

        data = '''
            <Phone>+996779280699</Phone>
            <text>Ваш код: 1234</Text>
        '''

        # response_data = self.send_(data)
        return "OK sms sended!!"


class SmsRu(SmsOtp):

    def send_sms_to_phone(self):

        data = {
            "phone": "+79102331793",
            "text": "Ваш код: 1234"
        }
        # response_data = self.send_(data)
        return "OK sms sended!!"