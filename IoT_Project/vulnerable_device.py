import time

class IoTSensor:
    def __init__(self):
        self.__secret_pin = "5821"  # Секретный PIN

    def verify_pin(self, input_pin):
        if len(input_pin) != len(self.__secret_pin):
            return False
        
        # Посимвольная проверка с "ранним выходом"
        for i in range(len(self.__secret_pin)):
            if input_pin[i] == self.__secret_pin[i]:
                # Имитируем небольшую задержку обработки процессором
                time.sleep(0.05) 
            else:
                # УЯЗВИМОСТЬ: функция возвращает результат мгновенно,
                # если символ не совпал.
                return False
        return True