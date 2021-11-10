import waveFunctions as wave
import numpy as np
import matplotlib.pyplot as plt

path = '! wave-starter-kit/data example/'

data20, duration, count = wave.readWaveData(path + '20 mm.txt')
data40, duration, count = wave.readWaveData(path + '40 mm.txt')
data60, duration, count = wave.readWaveData(path + '60 mm.txt')
data80, duration, count = wave.readWaveData(path + '80 mm.txt')
data100, duration, count = wave.readWaveData(path + '100 mm.txt')
data120, duration, count = wave.readWaveData(path + '120 mm.txt')

heights = [40, 60, 80, 100, 120]
adc = [np.mean(data20), np.mean(data40), np.mean(data60), np.mean(data80), np.mean(data100), np.mean(data120)]

plt.plot(adc, heights)
plt.title('Калибровочный график')
plt.ylabel(u'h, mm')
plt.xlabel(u'adc')
plt.minorticks_on()
plt.grid(which = "major", linewidth = 1)
plt.grid(which = "minor", linestyle = '--', linewidth = 0.5)

plt.show()

p = np.polyfit(adc, heights, 3)


waveData, duration, count = wave.readWaveData(path + 'wave.txt')

t = np.linspace(0, duration, count)

plt.plot(t, np.polyval(p, waveData))
plt.title('Зависимость уровня воды от времени')
plt.ylabel(u'h, mm')
plt.xlabel(u't, с')
plt.minorticks_on()
plt.grid(which = "major", linewidth = 1)
plt.grid(which = "minor", linestyle = '--', linewidth = 0.5)
plt.show()










# np.mean(data) 

# heights = [40, 60, 80, 100, 120]
# adc = [mean(40 mm.txt)]
# adc = [mean(60 mm.txt)]
# adc = [mean(80 mm.txt)]
# adc = [mean(100 mm.txt)]
# adc = [mean(120 mm.txt)]

# L_A = len(data)
# fig_data = plt.figure()

# x_A = list(range(0, L_A))
# x_A = [i/100 for i in x_A]

# plot(h, adc) 

# subplot_data_A = fig_data.add_subplot(111)

# subplot_data_A.set_ylabel(u'ADC')
# subplot_data_A.set_xlabel(u'h, mm')

# subplot_data_A.set_title('Калибровочный график')

# plt.show()

# fig_data.savefig('/home/gr105/Desktop/Nikolskaya Margarita/processing', format = 'png')

