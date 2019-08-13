from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

path = "data/dataset_files"
extension = 'wav'
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if extension in file:
            files.append(os.path.join(r, file))
print(files)

for e in files:
    if '_background_noise_' in e:
        pass
    else:
        print("Slicing %s" % e)
        sound_file = AudioSegment.from_wav(e)
        print("Max amp: %f" % sound_file.max_possible_amplitude)
        sound_file.normalize()
        print("Max amp: %f" % sound_file.max_possible_amplitude)
        print("Min silence: %f" % sound_file.dBFS)
        dbfs = sound_file.dBFS
        audio_chunks = split_on_silence(sound_file, 
        # must be silent for at least half a second
        min_silence_len=200,

        # consider it silent if quieter than -16 dBFS
        silence_thresh=dbfs-(0.01*dbfs)
        )

        for i, chunk in enumerate(audio_chunks):

            out_file = e + "_{0}.wav".format(i)
            print ("exporting " + out_file)
            chunk.export(out_file, format="wav")
    #PROGRAMA
