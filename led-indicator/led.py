from os.path import exists

# Thanks to REYRE for founding the led GPIO.


class Led:
    def __init__(self, pin: int, gpio: str = '/sys/class/gpio') -> None:
        if not exists(gpio):
            raise Exception('GPIO path invalid')
        if not pin:
            raise Exception('Pin parameter required')
        self.__gpio_path = gpio
        self.__pin = pin
        self._initialize_pin()

    def _initialize_pin(self) -> None:
        if exists(f'{self.__gpio_path}/gpio{self.__pin}'):
            return
        with open(f'{self.__gpio_path}/export', 'w') as f:
            f.write(str(self.__pin))
        with open(f'{self.__gpio_path}/gpio{self.__pin}/direction',  'w') as f:
            f.write('out')
        return

    def on(self) -> None:
        with open(f'{self.__gpio_path}/gpio{self.__pin}/value', 'w') as f:
            f.write('1')

    def off(self) -> None:
        with open(f'{self.__gpio_path}/gpio{self.__pin}/value', 'w') as f:
            f.write('0')
