import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import pygame
import os
from googletrans import Translator

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Teks ke Suara")

        self.label_author = tk.Label(root, text="AHMAD MAULANA 220511138")
        self.label_author.pack(pady=10)

        self.label_text = tk.Label(root, text="Masukkan teks:")
        self.label_text.pack(pady=10)

        self.text_entry = tk.Entry(root, width=70)
        self.text_entry.pack(pady=10)

        self.language_label = tk.Label(root, text="Pilih bahasa:")
        self.language_label.pack()

        self.language_var = tk.StringVar()
        self.language_var.set("Indonesia")  # Bahasa default: Indonesia
        languages = ["Indonesia", "Inggris", "Cina Sederhana", "Jepang", "Arab", "Sunda"]  # Nama bahasa untuk Cina Sederhana, Inggris, Jepang, Arab, dan Sunda
        self.language_menu = tk.OptionMenu(root, self.language_var, *languages)
        self.language_menu.pack(pady=10)

        self.translate_button = tk.Button(root, text="Terjemahkan", command=self.translate_text)
        self.translate_button.pack(pady=10)

        self.create_button = tk.Button(root, text="Buat dan Putar", command=self.create_and_play)
        self.create_button.pack(pady=20)

    def translate_text(self):
        text = self.text_entry.get()
        target_language = self.language_var.get()

        if not text:
            messagebox.showwarning("Peringatan", "Mohon masukkan teks terlebih dahulu.")
            return

        try:
            translator = Translator()
            translated_text = translator.translate(text, dest=self.get_language_code(target_language)).text
            self.text_entry.delete(0, tk.END)
            self.text_entry.insert(0, translated_text)
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan terjemahan: {str(e)}")

    def create_and_play(self):
        text = self.text_entry.get()
        language = self.language_var.get()

        if not text:
            messagebox.showwarning("Peringatan", "Mohon masukkan teks terlebih dahulu.")
            return

        try:
            myobj = gTTS(text=text, lang=self.get_language_code(language), slow=False)
            file_name = "output.mp3"
            myobj.save(file_name)

            pygame.mixer.init()
            pygame.mixer.music.load(file_name)
            pygame.mixer.music.play()

            # Tunggu audio selesai diputar
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            # Bersihkan
            pygame.mixer.quit()

            # Hapus file sementara
            os.remove(file_name)
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

    def get_language_code(self, language):
        language_mapping = {
            "Indonesia": "id",
            "Inggris": "en",
            "Cina Sederhana": "zh-cn",
            "Jepang": "ja",
            "Arab": "ar",
            "Sunda": "su"
        }
        return language_mapping.get(language, "id")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()
