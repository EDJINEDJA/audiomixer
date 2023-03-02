
import os 
import re
import glob
from pathlib import Path

class Utils():

    def __init__(self) -> None:
        self.audios = os.path.realpath("./data/raw/*.wav")

    def Load(self):
       
        files = []
        for file in glob.glob(self.audios):
            files.append(file)

        aud_idx = []

        for item in files:
            base = re.findall("\d+.wav", item)
            parser = Path(base)
            aud_idx.append(parser.stem())

        return aud_idx