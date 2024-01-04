import os
import threading
from tkinter import Tk, Button, Label, PhotoImage, Canvas
import pygame

class MusicPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Memainkan File mp.3")

        # Tambahkan elemen Canvas untuk latar belakang
        self.canvas = Canvas(root, bg="#FFEFD5", height=800, width=500)
        self.canvas.pack(expand=True, fill="both")

        self.label1 = Label(self.canvas, text="AHMAD MAULANA 220511138", bg="#FFEFD5")
        self.label1.pack(pady=20, padx=5)

        self.label2 = Label(self.canvas, text="Nadin : Rayuan Perempuan Gila", bg="#FFEFD5")
        self.label2.pack(pady=10, padx=5)

        self.button_play = Button(self.canvas, text="Putar Musik", command=self.play_music, bg="#00FF00")
        self.button_play.pack(pady=10, padx=5)

        # Menambahkan gambar untuk tombol jeda dan lanjut
        self.photo_pause = PhotoImage(file="pause 4.png").subsample(16)
        self.photo_resume = PhotoImage(file="play 3.png").subsample(16)

        self.button_pause = Button(self.canvas, image=self.photo_pause, command=self.pause_resume_music, state="disabled")
        self.button_pause.pack(pady=10)

        # Menambahkan atribut untuk melacak status musik
        self.music_paused = False

    def play_music(self):
        # Ganti 'tugas/dirayakan.mp3' dengan nama file MP3 yang ingin Anda putar
        file_path = os.path.join(os.getcwd(), "uts file", "rayuan.mp3")

        # Membuat thread terpisah untuk memutar musik
        self.music_thread = threading.Thread(target=self._play_music_thread, args=(file_path,))
        self.music_thread.start()

        # Mengaktifkan tombol jeda
        self.button_pause.config(state="normal", image=self.photo_pause)

    def _play_music_thread(self, file_path):
        # Inisialisasi Pygame
        pygame.init()
        pygame.mixer.init()

        # Memutar file MP3
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        # Menunggu hingga lagu selesai atau dijeda
        while pygame.mixer.music.get_busy() or self.music_paused:
            pygame.time.Clock().tick(10)

        # Menampilkan durasi musik saat selesai
        duration = pygame.mixer.Sound(file_path).get_length()
        self.label2.config(text=f"Durasi Musik: {duration:.2f} detik")

        # Menonaktifkan tombol jeda
        self.button_pause.config(state="disabled")

    def pause_resume_music(self):
        # Mengonfirmasi apakah musik sedang dijeda atau tidak
        if not self.music_paused:
            # Jika tidak dijeda, jeda musik
            pygame.mixer.music.pause()
            self.music_paused = True
            # Mengganti gambar tombol menjadi "Lanjut"
            self.button_pause.config(image=self.photo_resume)
        else:
            # Jika dijeda, lanjutkan musik
            pygame.mixer.music.unpause()
            self.music_paused = False
            # Mengganti gambar tombol menjadi "Jeda"
            self.button_pause.config(image=self.photo_pause)

if __name__ == "__main__":
    root = Tk()
    app = MusicPlayerApp(root)
    root.mainloop()
