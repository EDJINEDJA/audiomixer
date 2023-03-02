
import os 
import glob

class Utils():

    def __init__(self) -> None:
        self.audios = os.path.realpath("./data/raw/*.wav")

    def Load(self):
       
        files = []
        for file in glob.glob(self.audios):
            files.append(file)

        return files