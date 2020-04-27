from __future__ import print_function
import os
import glob
import eyed3
import ntpath


# Used mp3 to wav converter in pyAudioAnalyis package
# Had to fix the encoding and decoding order (line 48-49) because it was done incorrectly in package
def convert_dir_mp3_to_wav(audio_folder, sampling_rate, num_channels,
                           use_tags=False):
    """
    This function converts the MP3 files stored in a folder to WAV. If required,
    the output names of the WAV files are based on MP3 tags, otherwise the same
    names are used.
    ARGUMENTS:
     - audio_folder:    the path of the folder where the MP3s are stored
     - sampling_rate:   the sampling rate of the generated WAV files
     - num_channels:    the number of channels of the generated WAV files
     - use_tags:        True if the WAV filename is generated on MP3 tags
    """

    types = (audio_folder + os.sep + '*.mp3',)  # the tuple of file types
    files_list = []

    for files in types:
        files_list.extend(glob.glob(files))

    for f in files_list:
        audio_file = eyed3.load(f)
        if use_tags and audio_file.tag != None:
            artist = audio_file.tag.artist
            title = audio_file.tag.title
            if artist != None and title != None:
                if len(title) > 0 and len(artist) > 0:
                    filename = ntpath.split(f)[0] + os.sep + \
                                  artist.replace(","," ") + " --- " + \
                                  title.replace(","," ") + ".wav"
                else:
                    filename = f.replace(".mp3", ".wav")
            else:
                filename = f.replace(".mp3", ".wav")
        else:
            filename = f.replace(".mp3", ".wav")
        command = "avconv -i \"" + f + "\" -ar " + str(sampling_rate) + \
                  " -ac " + str(num_channels) + " " + "\"" + filename + "\""
        print(command)
        os.system(command.encode('ascii', 'ignore').decode('unicode-escape')
                  .replace("\0", ""))
