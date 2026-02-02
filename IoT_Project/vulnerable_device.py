import time

class IoTSensor:
    def __init__(self):
        self.__secret_pin = "5821" 

    def verify_pin(self, input_pin):
        if len(input_pin) != len(self.__secret_pin):
            return False
        
        for i in range(len(self.__secret_pin)):
            if input_pin[i] == self.__secret_pin[i]:
                time.sleep(0.05) 
            else:
                return False
        return True