import RPi.GPIO as GPiO
import time
import matplotlib.pyplot as plt

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2 ** bits
experement_time = 10
troykaModule = 17
comparator = 4
list_value = []
count_value = 0
GPiO.setmode(GPiO.BCM)
GPiO.setup(dac, GPiO.OUT, initial=GPiO.LOW)
GPiO.setup(troykaModule, GPiO.OUT, initial=GPiO.HIGH)
GPiO.setup(comparator, GPiO.IN)

def dec2bin(dec):
    return [int(bit) for bit in bin(dec)[2:].zfill(bits)]

def bin2dac(value):
    signal = dec2bin(value)
    GPiO.output(dac, signal)
    return signal

try:
    with open("data.txt", "w") as data_file:
        data_file.write("")
    start_time = time.time()

    while True:
        some_time = time.time()
        if some_time - start_time < experement_time:
            a = 0
            b = 256
            value = int((a + b) / 2)
            while True:
                signal = bin2dac(value)
                time.sleep(0.01)
                if b - a == 1:
                    break
                elif GPiO.input(comparator) == 1:
                    a = value
                    value = int((a + b) / 2)
                elif GPiO.input(comparator) == 0:
                    b = value
                    value = int((a + b) / 2)
            list_value.append(value)
            count_value = count_value + 1
            value_str = [str(value)]
            with open("data.txt", "a") as data_file:
                data_file.write("\n".join(value_str))
                data_file.write("\n")

    with open("settings.txt", "w") as settings_file:
        settings_file.write("{:.4f}\n".format(stop_time - start_time))
        settings_file.write("{:.4f}\n".format((stop_time - start_time) / count_value))
        settings_file.write("{:.4f}\n".format(count_value / (stop_time - start_time)))
        settings_file.write("{:.4f}\n".format(3.3 / 256))

    plt.plot(list_value)
    plt.show()

except KeyboardInterrupt:
    print("The program was stoped by the keyboard.")
else:
    print("No excrptions.")
finally:
    GPiO.output(dac, GPiO.LOW)
    GPiO.cleanup(dac)
    print("GPiO cleanup complited.")