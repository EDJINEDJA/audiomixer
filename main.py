from src.utils import utils

parser = utils.Utils(2)
print(parser.Load())

import tkinter as tk
import os


import tkinter as tk
import os
import pygame
import shutil

class AudioPlayer:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Lecteur audio")
        self.parent.geometry("500x300")

        # Création du frame principal
        self.main_frame = tk.Frame(self.parent)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Ajout du bouton de sélection du dossier
        self.select_button = tk.Button(self.main_frame, text="Sélectionner un dossier", command=self.select_folder)
        self.select_button.pack(pady=20)

        # Ajout du bouton pour jouer les fichiers audio
        self.play_button = tk.Button(self.main_frame, text="Lire les fichiers audio", command=self.play_audio_files, state=tk.DISABLED)
        self.play_button.pack(pady=20)

        # Ajout du frame pour les remarques
        self.notes_frame = tk.Frame(self.main_frame)
        self.notes_frame.pack(pady=20)

        # Ajout d'un titre pour le frame de remarques
        self.notes_title = tk.Label(self.notes_frame, text="Remarques pour chaque fichier audio")
        self.notes_title.pack()

        # Création de la variable pour les remarques
        self.notes = []

    def select_folder(self):
        # Ouvre la boîte de dialogue pour sélectionner un dossier
        folder_path = tk.filedialog.askdirectory()

        # Si un dossier est sélectionné, active le bouton de lecture
        if folder_path:
            self.selected_folder = folder_path
            self.play_button.config(state=tk.NORMAL)

    def play_audio_files(self):
        # Crée le nouveau dossier
        new_folder_path = "./data/processed"

        # Parcourt tous les fichiers audio dans le dossier sélectionné
        for file_name in os.listdir(self.selected_folder):
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
