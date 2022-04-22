from curses import baudrate
import matplotlib.pyplot as plt
import numpy as np
import serial

serialPort = serial.Serial()
serialPort.port = 'COM6'
serialPort.baudrate = 115200
serialPort.timeout = None
serialPort.open()

fftLen = 256
halfLen = int(fftLen/2)
startComChar = "F"
fs = 44200

plt.ion()
fftPlot, ax = plt.subplots(figsize=(8,8))
f = np.linspace(0,  fs/2, halfLen)#list(range(1,fftLen+1))
line = [0] * fftLen
line1, = ax.plot(f, line[0:halfLen])
ax.set_ylim([0, 50000])
plt.xlabel("Frequency [Hz]")
plt.ylabel("Normalized amplitude")
plt.title("FFT")

while True:
    if(serialPort.read(1) == bytes(startComChar, 'ascii')):
        line=serialPort.readline()
        line = line.split(b',')
        #print(len(line))
        line.pop()
        line = [int(i) for i in line]
        line = np.fft.fft(line)
        line = line[0:halfLen]
        line1.set_xdata(f)
        line1.set_ydata(np.abs(line))
        print(len(line))
        fftPlot.canvas.draw()
        fftPlot.canvas.flush_events()
