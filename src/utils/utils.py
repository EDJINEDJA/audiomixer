
import os 
import re
import glob
from pathlib import Path
import random


class Utils():

    def __init__(self,n) -> None:
        self.audios = os.path.realpath("./data/raw/*.wav")
        self.n = n

    def Load(self):
        file_memory={}
        cluster = []
        files = []
        for file in glob.glob(self.audios):
            files.append(file)

        aud_idx = []

        for item in files:
            base = re.findall("\d+.wav", item)
            parser = Path(" ".join(base))
            aud_idx.append(int(parser.stem))
            file_memory[int(parser.stem)]= item
        max_aud_idx = max(aud_idx)
        
        k_cluster = int(max_aud_idx/self.n)
      
        for idx in range(0,k_cluster):
            t=range(self.n*(idx) + 1 ,(idx+1)*self.n+1)
            cluster.append([])
            for i in t:
                cluster[idx].append(i)

        for item in range(0,k_cluster):
           cluster[item]=random.sample(cluster[item],len(cluster[item]))
        
        for idx , item in enumerate(cluster):
            
            for idx_ in item:
                
                yield(file_memory[idx_])
        
