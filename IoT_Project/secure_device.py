import time

class SecureIoTSensor:
    def __init__(self):
        self.__secret_pin = "5821"

    def verify_pin_secure(self, input_pin):
        if len(input_pin) != len(self.__secret_pin):
            return False
        
        result = 0
        for i in range(len(self.__secret_pin)):
            result |= (ord(input_pin[i]) ^ ord(self.__secret_pin[i]))
            time.sleep(0.05)
            
        return result == 0