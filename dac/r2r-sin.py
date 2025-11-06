
import r2r_dac as r2r
import RPi.GPIO as GPIO
import signal_generator as sg
import time

leds = [16, 20, 21, 25, 26, 17, 27, 22]
amplitude = 3.2
signal_frequency = 10
samplind_frequency = 20
dynamic_range = 3.29

if __name__ == "__main__":
    try:
        dac = r2r.R2R_DAC(leds, dynamic_range, True)
        while True:
            sg.wait_for_sampling_period(sampling_frequency)
            voltage = sg.get_sin_wave_amplitude(signal_frequency, time.time())
            GPIO.output(leds, dac.dec2bin(abs(int(voltage*255)))