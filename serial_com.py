from curses import baudrate
import matplotlib.pyplot as plt
import numpy as np
import serial

serialPort = serial.Serial()
serialPort.port = 'COM6'
serialPort.baudrate = 115200
serialPort.timeout = None
serialPort.open()

fftLen = 128
startComChar = "F"
fs = 44200

plt.ion()
fftPlot, ax = plt.subplots(figsize=(8,8))
f = np.linspace(0,  fs/2, fftLen)#list(range(1,fftLen+1))
line = [0] * fftLen
line1, = ax.plot(f, line)
ax.set_ylim([0, 33])
plt.xlabel("Frequency [Hz]")
plt.ylabel("Normalized amplitude")
plt.title("FFT")

while True:
    if(serialPort.read(1) == bytes(startComChar, 'ascii')):
        line=serialPort.readline()
        line = line.split(b',')
        line.pop()
        line = [int(i) for i in line]
        line1.set_xdata(f)
        line1.set_ydata(line)
        
        fftPlot.canvas.draw()
        fftPlot.canvas.flush_events()
