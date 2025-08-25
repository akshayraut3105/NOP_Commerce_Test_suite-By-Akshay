import configparser

config = configparser.RawConfigParser()

config.read(r"C:\Users\AKSHAY\PycharmProjects\NOP_Commerce_Test_suite\Configurations\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURl():
        url = config.get('common info', 'baseurl')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
