# Leddar Vu8 Object Detection Report

**An evaluation of the Leddar Vu8 LiDAR sensor for UAV applications**

By Josué Dazogbo, Computer Engineering Student at the University of Ottawa

Date: 27 July 2023

## Overview

This repository contains a [technical report](LeddarVu8VisualizationReport.pdf) detailing the evaluation of the Leddar Vu8 LiDAR sensor's performance for UAV applications and the associated code used to interface the Leddar Sensor.

## Code Structure

The code used to record and visualize data is split into 2 files: [DataRecorder.py](DataRecorder.py) and [DataVisualizer.py](DataVisualizer.py). The 'DataRecorder.py' file uses the publically available [LeddarSDK](https://sdk.leddartech.com/v4.2/#/) to record the output position fed from the Leddar Vu8 LiDAR sensor and write it to a Comma-Seperated-Value (csv) file. The 'DataVisualizer.py' file is used to quickly visualize the data caputred by the previous file.

## Understanding the Repository

This is general explanation of the [DataRecorder.py](DataRecorder.py) script:

1. The script prompts the user to enter the recording time in minutes. It ensures that the input is a positive floating-point number greater than zero. If the input is invalid, it prompts the user to enter the time again until a valid input is provided.

2. After obtaining the recording time, the script prompts the user to enter the recording rate in Hertz. It also validates the input to ensure it's a positive floating-point number greater than zero and less than or equal to a maximum rate defined by DataRecorder.maximumRate.

3. Once both the recording time and rate are validated, the script calls the recordData method of the DataRecorder class to record the data. It then saves the recorded data to a CSV file with a filename based on the recording time and rate.

## Conclusion

The Leddar Vu8 demonstrates accurate distance measurement capabilities and effective obstacle detection. Implementation of an infinite distance system enhances its utility. Further enhancements such as altitude detection could improve data validity. The sensor also depicts simple object geometries effectively. For further information on the findings, a  has also been uploaded to the repository.

