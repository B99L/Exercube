import numpy as np
from ezc3d import c3d

def getFileName(proband, minute):
    return r'C:\Users\badrl\OneDrive - ZHAW\Desktop\Studium\5.Semerster\PA\Data\pat'+ str(proband).zfill(2)+ '/pat'+ str(proband).zfill(2)+ '_dynamic_'+ str(minute).zfill(2)+ '.c3d'

def getExperimentMarker(filename):
    return np.array(c3d(filename)['parameters']['POINT']['LABELS']['value'])

def getSingleFileData(filename):
    return np.array(c3d(filename)['data']['points'])[:-1,:]

