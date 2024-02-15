import numpy as np

from constants import *
from model_configuration import *


def reshape_for_time_series(train_data):
    train_data_reshaped = np.zeros((train_data.shape[0], train_data.shape[3], train_data.shape[1] * train_data.shape[2]))

    for timestep in range(train_data.shape[3]):
        for axis in range(train_data.shape[1]):
            for marker in range(train_data.shape[2]):
                train_data_reshaped[:, timestep, (axis*train_data.shape[2])+marker] = train_data[:, axis, marker, timestep]
    return train_data_reshaped

def moving_window_single_athlete(data, min, max, timeseries_datapoints):
    gain = WINDOW_LENGTH - OVERLAP
    if(gain <= 0):
        raise Exception("Windowlength must be greater than Overlap")
    
    number_of_windows = int((max-min)/gain)
    windows = np.zeros((number_of_windows, WINDOW_LENGTH, timeseries_datapoints))

    for i in range(number_of_windows):
        windows[i] = data[min+i*gain:min+i*gain+WINDOW_LENGTH]
    return windows

def downsampling(train_data):
    return train_data[:,::round(DOWNSAMPLING_RATE)]
