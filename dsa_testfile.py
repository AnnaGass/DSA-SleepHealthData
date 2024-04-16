import pyedflib
import csv

rec_filename = r'C:\Users\Anna\Documents\Master\Semester 3\ucddb002.rec'

edf_file = pyedflib.EdfReader(rec_filename)

# Get the indices of Pulse and SpO2 signals
pulse_index = edf_file.getSignalLabels().index('Pulse')
spo2_index = edf_file.getSignalLabels().index('SpO2')

# Read Pulse and SpO2 from the .rec file
pulse_data = edf_file.readSignal(pulse_index)
spo2_data = edf_file.readSignal(spo2_index)

csv_filename = r'C:\Users\Anna\Documents\Master\Semester 3\Testdatei_dsa.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write column namens into header rows
    writer.writerow(['Pulse', 'SpO2'])
    
    # Write Pulse and SpO2 data to the CSV file
    for pulse, spo2 in zip(pulse_data, spo2_data):
        writer.writerow([pulse, spo2])
   
edf_file.close()

print("The data has been successfully saved to the CSV file.")
