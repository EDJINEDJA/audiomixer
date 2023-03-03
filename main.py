from src.utils import utils

parser = utils.Utils(2)
print(parser.Load())

import tkinter as tk
import os


import tkinter as tk
import os
import pygame
import shutil
import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb
from tkinter import filedialog
import wave
import pygame
import os
import shutil

class AudioPlayer:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("emotion")
        self.parent.geometry("1280x720")

        # Création des frames
        self.main_frame = tk.Frame(self.parent)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.frame1 = tk.Frame(self.main_frame, background= "blue")
        self.frame2 = tk.Frame(self.main_frame, background="white" )
        
        self.frame1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.frame2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.frame3 = tk.Frame(self.frame2, background= "white")
        self.frame4 = tk.Frame(self.frame2, background="white" )

        self.frame4.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.frame3.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        

      

       
        #  # Création des widgets pour la frame 1 (Ajout du bouton de sélection du dossier)
        self.select_button = tk.Button(self.frame1, text="Sélectionner un dossier", command=self.select_folder)
        self.select_button.pack(pady=20)

        # Variable pour stocker le chemin du dossier sélectionné
        self.selected_folder = tk.StringVar()

        # Création des widgets pour la frame 2
        self.L = tk.Label(self.frame3, text="Outil pour jouer les audio et récupérer les noms cibles")
        self.L.pack(padx=40,pady=100)

        self.play_button = tk.Button(self.frame3, text="Lire", command=self.play_audio)
        self.play_button.pack(side=tk.LEFT, padx=40)

        self.pause_button = tk.Button(self.frame3, text="Pause", command=self.pause_audio)
        self.pause_button.pack(side=tk.LEFT, padx=40)

        self.stop_button = tk.Button(self.frame3, text="Stop", command=self.stop_audio)
        self.stop_button.pack(side=tk.LEFT, padx=40)

        self.volume_label = tk.Label(self.frame3, text="Volume :")
        self.volume_label.pack(side=tk.LEFT, padx=40)

        self.volume_scale = tk.Scale(self.frame3, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_scale.pack(side=tk.LEFT, padx=10)
        # Ajout du frame pour les remarques
        #self.notes_frame = tk.Frame(self.frame2)
        #self.notes_frame.pack(side=tk.BOTTOM,pady=100)

        # Ajout d'un titre pour le frame de remarques
        self.notes_title = tk.Label(self.frame4, text="Remarques pour chaque fichier audio")
        self.notes_title.pack(side=tk.BOTTOM,padx=10,pady=200)

        # Création de la variable pour les remarques
        self.notes = []
        
        # Initialisation des variables
        self.audio_file = None
        self.audio_stream = None
        self.volume = 50
        self.paused = False

    def play_audio(self):
        # Crée le nouveau dossier
        new_folder_path = "./data/processed"

        # Parcourt tous les fichiers audio dans le dossier sélectionné
    
        for file_name in os.listdir(os.path.realpath(self.selected_folder)):
            if file_name.endswith(".wav"):
                # Lit le fichier audio
                # initialize pygame
                pygame.init()

                # load the audio file
                pygame.mixer.music.load(file_name)

                # play the audio file
                pygame.mixer.music.play()

                # wait for the audio to finish playing
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)

                # quit pygame
                pygame.quit()

                # Demande à l'utilisateur de donner des remarques pour le fichier audio
                note = self.get_audio_note()

                # Ajoute les remarques à la liste
                self.notes.append((file_name, note))

                # Copie le fichier audio dans le nouveau dossier avec le nom donné par l'utilisateur
                new_file_path = os.path.join(new_folder_path, f"{note}.wav")
                shutil.copyfile(new_folder_path, new_file_path)

    def get_audio_note(self):
        # Création de la fenêtre de dialogue pour les remarques
        note_window = tk.Toplevel()
        note_window.title("Remarques pour le fichier audio")
        note_window.geometry("400x200")

        # Ajout du champ de texte pour les remarques
        note_label = tk.Label(note_window, text="Remarques :")
        note_label.pack(pady=10)

        note_text = tk.Text(note_window, height=5)
        return note_text


    def pause_audio(self):
        if self.audio_file and not self.paused:
            pygame.mixer.music.pause()
            self.paused = True
        elif self.audio_file and self.paused:
            pygame.mixer.music.unpause()
            self.paused = False

    def stop_audio(self):
        if self.audio_file:
            pygame.mixer.music.stop()

    def set_volume(self, volume):
        self.volume = int(volume)
        if self.audio_file:
            pygame.mixer.music.set_volume(self.volume / 100)

    def select_folder(self):
        # Ouvre la boîte de dialogue pour sélectionner un dossier
        folder_path = filedialog.askdirectory()

        # Met à jour la variable selected_folder avec le chemin du dossier sélectionné
        if folder_path:
            self.selected_folder.set(folder_path)

        # Affiche le chemin du dossier sélectionné
        self.label = tk.Label(self.main_frame, textvariable=self.selected_folder)
        self.label.pack(pady=10)