import leddar
import pandas as pd
import time
import numpy as np

class DataRecorder:

    dev = None
    recordingRate = None
    maximumRate = 5 #This value was found experimentally

    def getDevice()->leddar.Device:
        return DataRecorder.dev
    def setDevice(device):
        DataRecorder.dev = device  
    def getSamplingTime()->float:
        return 1/float((DataRecorder.recordingRate))
    def setRecordingRate(rate):
        '''Sets the rates (in Hz) at which echoes are read'''
        DataRecorder.recordingRate = rate
    def initializeDevice():
        DataRecorder.setDevice(leddar.Device())
        sensor_list = leddar.get_devices("Serial")
        DataRecorder.getDevice().connect(sensor_list[1]['name'], leddar.device_types["Serial"])
        DataRecorder.getDevice().set_data_mask(leddar.data_masks["DM_ECHOES"])
    def readData()->pd.DataFrame:
        '''Reads echo data from sensor and stores it in a nice dataframe format.'''
        echoes = DataRecorder.getDevice().get_echoes()
        data = {
        "X Coord 7":[echoes["data"][0][1]], "X Coord 6":[echoes["data"][1][1]], "X Coord 5":[echoes["data"][2][1]],
        "X Coord 4":[echoes["data"][3][1]], "X Coord 3":[echoes["data"][4][1]], "X Coord 2":[echoes["data"][5][1]],
        "X Coord 1":[echoes["data"][6][1]], "X Coord 0":[echoes["data"][7][1]],

        "Y Coord 7":[echoes["data"][0][2]], "Y Coord 6":[echoes["data"][1][2]], "Y Coord 5":[echoes["data"][2][2]], 
        "Y Coord 4":[echoes["data"][3][2]], "Y Coord 3":[echoes["data"][4][2]], "Y Coord 2":[echoes["data"][5][2]], 
        "Y Coord 1":[echoes["data"][6][2]], "Y Coord 0":[echoes["data"][7][2]]
        }
        return pd.DataFrame(data, index=pd.Index([echoes["timestamp"]], name='Timestamp'))
    def recordData(readTime, rate)->pd.DataFrame:
        echoes = []
        DataRecorder.initializeDevice()
        DataRecorder.setRecordingRate(rate)
        ticks = int((60*readTime)/DataRecorder.getSamplingTime())
        for i in range(ticks):
            data = DataRecorder.readData()
            time.sleep(DataRecorder.getSamplingTime())
            echoes.append(data)
        datas = pd.concat(echoes)
        DataRecorder.getDevice().disconnect()
        del DataRecorder.dev
        return datas

if __name__ == "__main__":
    
    print("Enter recording time (in minutes):", end=" ")

    while True:
        recordingTime = input()
        try:
            recordingTime = int(recordingTime)
        except:
            print("Invalid time. Please enter a time (in minutes):", end=" ")
        else:
            break

    print("Enter Recording rate (in Hertz WARNING: Rate must be smaller than 5 Hz):", end=" ")

    while True:
        recordingRate = input()
        try:
            recordingRate = int(recordingRate)
        except ValueError:
            print("Invalid rate. Please enter a rate (in Hertz):", end=" ")
        else:
            if recordingRate > DataRecorder.maximumRate:
                print("Recording Rate can't be higher than " + str(DataRecorder.maximumRate) + "Hz. Please re-enter a rate (in Hertz):", end=" ")
            else:
                break

    data = DataRecorder.recordData(recordingTime, recordingRate)
    data.to_csv("LeddarVu8-Data-" + str(recordingTime) + "mins-" + str(recordingRate) + "Hz.csv")
    print("File has been saved as '" + "LeddarVu8-Data-" + str(recordingTime) + "mins-" + str(recordingRate) + "Hz.csv" + "'")

    
