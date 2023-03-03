import os
import tkinter as tk
import tkinter.filedialog as filedialog
from tkinter import messagebox
import pygame
import shutil
import sys



class AudioPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Emotion app")
        self.root.geometry("1280x720")
        self.audio_files = []
        self.current_audio_index = 0
        self.current_audio = None
        self.new_audio_name = tk.StringVar()
        self.name=""
        self.essai=0
        self.new_path =""
        # Initialisation des variables
        self.audio_file = None
        self.audio_stream = None
        self.volume = 50
        self.paused = False

        # Création des frames
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.frame1 = tk.Frame(self.main_frame, background= "#787878")
        self.frame2 = tk.Frame(self.main_frame)
        
        self.frame1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.frame2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


        # Création des widgets
        self.upload_label = tk.Label(self.frame1, text="Charger le dossier contenant les audio ici !",background="#787878",font=('Helvetica', 15),foreground="white")
        self.choose_folder_button = tk.Button(self.frame1, text="Choisir un dossier", command=self.choose_folder)

        # Label pour le champ "Nom"
        self.name_label = tk.Label(self.frame1, text="Nom : ",background="#787878",font=('Helvetica', 15),foreground="white")

        # Champ de saisie pour le nom
        self.name_entry = tk.Entry(self.frame1)

        # Label pour le champ "Nombre d'éssai"
        self.essai_label = tk.Label(self.frame1, text="Nombre d'éssai : ", background="#787878",font=('Helvetica', 15),foreground="white")

        # Champ de saisie pour le Nombre d'éssai
        self.essai_entry = tk.Entry(self.frame1)

        # Bouton pour soumettre le formulaire
        self.submit_button = tk.Button(self.frame1, text="Soumettre", command=self.submit_form)

        self.audio_monitoring = tk.Label(self.frame2, text="Donner le label pour cet audio et enrégistrer!",font=('Helvetica', 15),foreground="black")
        self.audio_label = tk.Label(self.frame2, text="")
        self.new_name_entry = tk.Entry(self.frame2, textvariable=self.new_audio_name)

        self.save_button = tk.Button(self.frame2, text="Enregistrer sous", command=self.save_audio)
        self.next_button = tk.Button(self.frame2, text="Suivant", command=self.play_next)
        self.play_button = tk.Button(self.frame2, text="Lire", command=self.play_audio)

        self.volume_label = tk.Label(self.frame2, text="Volume :")

        self.volume_scale = tk.Scale(self.frame2, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume)
      
        self.pause_button = tk.Button(self.frame2, text="Pause", command=self.pause_audio)
        

        self.stop_button = tk.Button(self.frame2, text="Stop", command=self.stop_audio)
        
        # Placement des widnouveaux_fichiers_audiogets
        self.upload_label.pack(side=tk.TOP,pady=30)
        self.choose_folder_button.pack(side=tk.TOP,pady=50)
        self.name_label.pack(padx=5, pady=5)
        self.name_entry.pack( padx=5, pady=5)
        self.essai_label.pack( padx=5, pady=5)
        self.essai_entry.pack( padx=5, pady=5)
        self.submit_button.pack( padx=5, pady=5)
        self.audio_monitoring.pack(side=tk.TOP,pady=30)
        self.audio_label.pack(side=tk.TOP,padx=10, pady=10)
        self.new_name_entry.pack(side=tk.TOP ,padx=10, pady=10)
        self.save_button.pack(side=tk.TOP,padx=10, pady=10)
        self.next_button.pack(side=tk.TOP,padx=10, pady=10)
        self.play_button.pack(side=tk.TOP,padx=10, pady=10)
        self.volume_label.pack(side=tk.TOP, padx=10, pady=10)
        self.volume_scale.pack(side=tk.TOP)
        self.pause_button.pack(side=tk.TOP, pady=40)
        self.stop_button.pack(side=tk.TOP)

    @staticmethod
    def resource_path(relative_path):
        #https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS2
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def submit_form(self):
        self.name = self.name_entry.get()
        self.essai = self.essai_entry.get()
        self.new_path = self.resource_path(os.path.join("data\\processed\\", f"{self.name }_{self.essai}"))
        os.makedirs(self.new_path,exist_ok=True)
    

    def choose_folder(self):
        # Ouvre une boîte de dialogue pour choisir un dossier contenant les fichiers audio
        folder_path  = filedialog.askdirectory()
        if not os.listdir(folder_path):
            messagebox.showwarning("Dossier vide", "Le dossier sélectionné est vide.")
        else:
            # Continuer avec le traitement du dossier
            self.audio_files = [os.path.join(folder_path, f) for f in os.listdir(self.resource_path(folder_path)) if f.endswith(".wav")]
            self.current_audio_index = 0
            self.current_audio = None
            self.update_audio_label()

    def update_audio_label(self):
        # Affiche le nom du fichier audio en cours
        if self.current_audio:
            self.audio_label.config(text="Listning ...")

    def play_audio(self):
        # Joue le fichier audio en cours
        if self.current_audio:
            pygame.mixer.init()
            pygame.mixer.music.load(self.current_audio)
            pygame.mixer.music.play()

    def save_audio(self):
        # Enregistre le fichier audio en cours avec un nouveau nom
        if self.current_audio:
            new_name = self.new_audio_name.get()
            if new_name:
          
                new_path = os.path.join(self.new_path,os.path.basename(self.current_audio ) + "_" + new_name + ".wav")
                shutil.copy2(self.current_audio, new_path)
                #os.rename(self.current_audio, new_path)
                self.play_next()

    def play_next(self):
        # Joue le fichier audio suivant dans la liste
        
        if self.audio_files:
            self.current_audio_index = (self.current_audio_index + 1) % len(self.audio_files)
            self.current_audio = self.audio_files[self.current_audio_index]
            self.update_audio_label()
            self.new_audio_name.set(f"audio_{self.current_audio_index }")
            if self.current_audio_index == 0:
                messagebox.showwarning("Dernier audio", "La lecture aléatoire des audio vont recommencés après cet audio")
            
    def set_volume(self, volume):
        self.volume = int(volume)
        if self.current_audio:
            pygame.mixer.music.set_volume(self.volume / 100)

    def pause_audio(self):
        if self.current_audio and not self.paused:
            pygame.mixer.music.pause()
            self.paused = True
        elif self.current_audio and self.paused:
            pygame.mixer.music.unpause()
            self.paused = False

    def stop_audio(self):
        if self.current_audio:
            pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioPlayer(root)
    root.mainloop()
