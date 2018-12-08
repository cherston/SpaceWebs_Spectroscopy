import serial
import re
import csv
import numpy as np

portPath = '/dev/cu.usbmodem1421'
baudRate = 115200
filename = "../ML_Test_Data/OOHalogenSource_LowResSpect_INT=200Gain=3p7dist=0p5cm.csv"

ser = serial.Serial(portPath, baudRate)

def save_to_csv(data, filename):
	with open(filename, 'a') as csvfile:
		csvwrite = csv.writer(csvfile)
		csvwrite.writerow(data)

def find_matches(sensorData):
	R = re.findall('\[([^]]*)',sensorData)
	return R

def startup():
	print "flushing input"
	ser.flushInput()


startup()

while True:
	sensorData = ser.readline()
	#print sensorData
        #if("next pixel" in sensorData):
        #print "prep next pixel"
        #if("done with row" in sensorData):
        #print "done with row"

	values = find_matches(sensorData)

	#eliminate some garbage at the beginning of each read
	if(len(values) == 6):
		values = map(float, values)
		print str(values) + str(',')
		save_to_csv(values, filename)