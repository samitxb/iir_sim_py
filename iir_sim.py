import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import iirfilter, freqz

b, a = iirfilter(4, 0.2, btype='low', ftype='butter', output='ba')
w, h = freqz(b, a)
plt.plot(w, 20 * np.log10(abs(h)))
plt.title('IIR Filter Frequency Response')
plt.xlabel('Frequency (radians/sample)')
plt.ylabel('Amplitude (dB)')
plt.grid()
plt.show()
