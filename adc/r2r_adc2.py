import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, bits_gpio, compare_time=0.01, verbose=False):
        self.bits_gpio = bits_gpio
        self.verbose = verbose
        self.compare_time = compare_time
        self.num_bits = len(bits_gpio)
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def decimal2binary(self, decimal):
        binary_str = bin(int(decimal))[2:].zfill(8)
        signal = [int(bit) for bit in binary_str]
        return signal

    def number2dac(self, number):
        signal = self.decimal2binary(number)
        GPIO.output(self.bits_gpio, signal)
        return signal

    def sequential_counting_adc(self):
        max_value = 2**self.num_bits
       
        for value in range(max_value):
            time.sleep(self.compare_time)
            signal = self.number2dac(value)
            comparator_value = GPIO.input(self.comp_gpio)
           
            if comparator_value == 1:
                voltage = value / max_value * 3.19
                #print(f"Voltage = {voltage:.2f}V")
                return value

    def sar_voltage(self):
        result = 0
        max_value = 2**self.num_bits
        for i in range(7, -1, -1):
            test_value = result + (1 << i)
            self.number2dac(test_value)
            comparator_value = GPIO.input(self.comp_gpio)
       
            if comparator_value == 1:
                pass
            else:
                result = test_value
        voltage = (result / max_value) * 3.19
        print(f"Напряжение: {voltage:.3f}В")
        return voltage
        
if __name__ == "__main__":
    adc = R2R_ADC(bits_gpio=[26, 20, 19, 16, 13, 12, 25, 11],
                   compare_time=0.01,
                   verbose=True)
    try:
        while True:
            try:
                #adc.sequential_counting_adc()
                adc.sar_voltage()
                time.sleep(1)
            except ValueError as e:
                print(f"Ошибка: {e}")
            except KeyboardInterrupt:
                break
    finally:
        adc.deinit()