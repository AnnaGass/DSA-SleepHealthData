from pyedflib import highlevel

import pyedflib
import numpy as np
import matplotlib.pyplot as plt

# Index 6 = SpO2
# Index 13 = Pulse
variable_index = [13]
path = "Data/subject7.rec"

f = pyedflib.EdfReader(path)

signal_labels = f.getSignalLabels()
spo2_signals = f.readSignal(6)
pulse_signals = f.readSignal(13)

print(signal_labels)

# Plot the list
plt.plot(spo2_signals)

# Add labels and title
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Plot of a List')

# Show the plot
plt.show()

# # Writing the ndarray to a CSV file
# np.savetxt('data.csv', signals_data, delimiter=',')