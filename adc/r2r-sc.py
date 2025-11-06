import r2r_adc2 as r2r
from matplotlib import pyplot as plt
import adc_plot
import RPi.GPIO as GPIO
import time
adc = r2r.R2R_ADC(bits_gpio=[26, 20, 19, 16, 13, 12, 25, 11],compare_time=0.01,verbose=True)
voltage_arr = []
time_arr = []
sp = []
duration = 3.0
if __name__ == "__main__":
    try:
        start_time = time.time()
        sampling = time.time()
        while (time.time() - start_time) < duration:
            #voltage_arr.append(int(adc.sequential_counting_adc())/256*3.19)
            voltage_arr.append(int(adc.sar_voltage())
            sp.append(time.time() - sampling)
            time_arr.append(time.time()-start_time)
            sampling = time.time()
        #adc_plot.plt_voltage_vs_time(time_arr, voltage_arr)  
        plt.figure(figsize = (10, 6))
        #plt.hist(sp)
        plt.plot(time_arr, voltage_arr)
        plt.title('Распределение периодов дискретизации тзмерений по времени на 1 знаение') 
        plt.grid(True, alpha=0.3)
        plt.xlabel('Период, с')
        plt.ylabel('Кол-во измерений')
        plt.show()
    finally:
        adc.deinit()