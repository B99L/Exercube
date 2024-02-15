import numpy as np
from os.path import exists
from ezc3d import c3d

import matplotlib.pyplot as plt
from matplotlib import cm
from constants import *
from modules.filehandling import getFileName, getExperimentMarker, getSingleFileData
from modules.markerorder import getMarkerOrder

order = getMarkerOrder()

probands = np.arange(1, 8)
probands = np.delete(probands, [3-1])

data = np.empty((PROBANDS, AXES, MAX_MARKERS, MAX_VALUES))

print("Evaluate Datapoints of users...")
maxDataPoints = 0
dataPoints = np.array(())
for proband in probands:
    dataPoint = 0
    for minute in range(1, MAX_MINUTES+1):
        filename = getFileName(proband, minute)
        if(exists(filename)):
            singleFileData = getSingleFileData(filename)
            dataPoint += singleFileData.shape[2]
    if(maxDataPoints < dataPoint):
        maxDataPoints = dataPoint
    dataPoints = np.append(dataPoints, dataPoint)

print("Get Data of each users...")
def createArrayForSingleAthlete(filename, probandData, probandEntries):
    markerControlArray = np.array(())
    if(exists(filename)):
        experimentMarker = getExperimentMarker(filename)
        singleFileData = getSingleFileData(filename)
        entries = singleFileData.shape[2]
        #Insert every Marker into probandData
        for markerIndex in range(order.shape[0]):
            if(np.any(experimentMarker  == order[markerIndex])):
                fileIndex = np.where(experimentMarker == order[markerIndex])[0][0]
                probandData[:, markerIndex, probandEntries: probandEntries + entries] = singleFileData[:, fileIndex, :]
                markerControlArray = np.append(markerControlArray, experimentMarker[fileIndex])
            else:
                #if(not(proband == 5 or proband == 20)):
                    #raise Exception("No NaN value necessary")
                #Set the values of the missing marker as nan
                probandData[:, markerIndex, probandEntries: probandEntries + entries] = np.nan
                markerControlArray = np.append(markerControlArray, order[markerIndex])
        probandEntries += entries

        if(not(np.array_equal(markerControlArray, order))):
            raise Exception("Order of marker wrong")
    return probandData, probandEntries


probandIndex = 0 
print("Create dataframe...")
for proband in probands:
    probandData = np.zeros((AXES, MAX_MARKERS, int(dataPoints[probandIndex])))
    probandEntries = 0
    for minute in range(1, MAX_MINUTES+1):
        filename = getFileName(proband, minute)
        probandData, probandEntries = createArrayForSingleAthlete(filename, probandData, probandEntries)

    data[probandIndex, :, :, 0:int(dataPoints[probandIndex])] = probandData
    probandIndex += 1

np.save(r'C:\Users\badrl\Downloads\dataframe\Pats' , data)












