import os
import tkinter as tk
import tkinter.filedialog as filedialog
import pygame
import shutil

class AudioPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("emotion")
        self.root.geometry("1280x720")
        self.audio_files = []
        self.current_audio_index = 0
        self.current_audio = None
        self.new_audio_name = tk.StringVar()

        # Création des widgets
        self.audio_label = tk.Label(root, text="")
        self.new_name_entry = tk.Entry(root, textvariable=self.new_audio_name)

        self.save_button = tk.Button(root, text="Enregistrer sous", command=self.save_audio)
        self.next_button = tk.Button(root, text="Suivant", command=self.play_next)
        self.play_button = tk.Button(root, text="Lire", command=self.play_audio)
        self.choose_folder_button = tk.Button(root, text="Choisir un dossier", command=self.choose_folder)

        # Placement des widnouveaux_fichiers_audiogets
        self.choose_folder_button.pack(side=tk.TOP)
        self.audio_label.pack(side=tk.TOP)
        self.new_name_entry.pack(side=tk.TOP)
        self.save_button.pack(side=tk.TOP)
        self.next_button.pack(side=tk.TOP)
        self.play_button.pack(side=tk.TOP)

    def choose_folder(self):
        # Ouvre une boîte de dialogue pour choisir un dossier contenant les fichiers audio
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.audio_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(".wav")]
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
          
                new_path = os.path.join("./data/processed/",os.path.basename(self.current_audio ) + "_" + new_name + ".wav")
                #os.makedirs(os.path.dirname(new_path), exist_ok=True)
                shutil.copy2(self.current_audio, new_path)
                #os.rename(self.current_audio, new_path)
                self.play_next()

    def play_next(self):
        # Joue le fichier audio suivant dans la liste
        if self.audio_files:
            self.current_audio_index = (self.current_audio_index + 1) % len(self.audio_files)
            self.current_audio = self.audio_files[self.current_audio_index]
            self.update_audio_label()
            #self.new_audio_name.set(os.path.splitext(os.path.basename(self.current_audio))[0])


if __name__ == "__main__":
    root = tk.Tk()
    app = AudioPlayer(root)
    root.mainloop()
