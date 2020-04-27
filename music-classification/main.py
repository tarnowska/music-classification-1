# TO DO
"""
THE SECOND VARIANT IS COMPLETELY DONE (HOPEFULLY)
THE FIRST VARIANT NEEDS TO SHOW THE WINDOWS AS ROWS AND THE FEATURES AS COLUMNS -- LOOK AT THE EXAMPLE WHEN IT IS
GRAPHED
"""


# Imports
import pathlib
from pathlib import Path
import os
import short_term_feature_extractor as stfe
import convert_mp3_to_wav as convert

# Declare variables
first_time = True
## If you want first_variant keep True, if you want second variant, make False
first_variant = True

# Converts all mp3 files to wav files
convert.convert_dir_mp3_to_wav("test_audio", 16000, 1)


# Loops through file with audio
for file in pathlib.Path("test_audio").iterdir():
    file_type = os.path.splitext(str(file))[-1].lower()
    if file_type == ".wav":
        # Reads audio file
        [Fs, x] = stfe.read_audio_file(file)

        # Default csv file name for second variant
        csv_name = "audio_st_features.csv"

        # Extracts features
        if first_variant:
                F, f_names = stfe.feature_extraction(x, Fs, 0.500 * Fs, 0.025 * Fs)
                csv_name = (Path(file).stem + "_st_features.csv")
        else:
            F, f_names = stfe.feature_extraction(x, Fs, 0.500 * Fs, 32.0 * Fs)

        # Extracts short term features
        short_term_features, short_term_features_names = stfe.extract_short_term_features(F, f_names)

        # Creates csv file
        stfe.create_csv(csv_name, file, short_term_features_names, short_term_features, first_time)

        # Signals that next loop is not the first one - helps with editing csv file
        if first_variant is False:
            first_time = False

    else:
        # Get rid of this if you want to keep the original mp3 files
        os.remove(str(file))
