from curses import baudrate
import matplotlib.pyplot as plt
import serial

serialPort = serial.Serial()
serialPort.port = 'COM6'
serialPort.baudrate = 115200
serialPort.timeout = None
serialPort.open()

fftLen = 128

plt.ion()
fftPlot, ax = plt.subplots(figsize=(8,8))
f = list(range(1,fftLen+1))
line = [0] * fftLen
line1, = ax.plot(f, line)
ax.set_ylim([0, 33])

while True:
    if(serialPort.read(1) == bytes("F", 'ascii')):
        line=serialPort.readline()
        line = line.split(b',')
        line.pop()
        line = [int(i) for i in line]
        line1.set_xdata(f)
        line1.set_ydata(line)
        
        fftPlot.canvas.draw()
        fftPlot.canvas.flush_events()
