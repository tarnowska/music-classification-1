from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import ShortTermFeatures
from pathlib import Path
import csv

import matplotlib.pyplot as plt
from numpy import asarray
from numpy import savetxt
import numpy as np
import pandas as pd


# Reads wav file
def read_audio_file(wav_file):
    [Fs, x] = audioBasicIO.read_audio_file(wav_file)
    return Fs, x


# Extracts all the features of the wav song
def feature_extraction(signal, sampling_rate, window, step, deltas=True):
    F, f_names = ShortTermFeatures.feature_extraction(signal, sampling_rate, window, step, deltas)
    return F, f_names


# Extracts short term features, and their names, from all features
def extract_short_term_features(features, features_names):
    short_features = []
    short_features_names = []
    for x in range(0, 34):
        # Creates new array of only short term features and respective names
        short_features.append(features[x][0])
        short_features_names.append(features_names[x])
    return short_features, short_features_names


# Creates csv file for short term features
def create_csv(csv_file_name, file_audio_name, short_features_names, short_features, first_time):
    short_features_names.insert(0, "Short Term Feature Names: ")
    short_features.insert(0, Path(file_audio_name).stem)
    if first_time:
        with open(csv_file_name, 'w') as myFile:
            file_writer = csv.writer(myFile)
            file_writer.writerow(short_features_names)
            file_writer.writerow(short_features)
    else:
        with open(csv_file_name, 'a') as myFile:
            file_writer = csv.writer(myFile)
            file_writer.writerow(short_features)

