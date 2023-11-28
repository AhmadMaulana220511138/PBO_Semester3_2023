import os
import threading
from tkinter import Tk, Button, Label, PhotoImage
import pygame

class MusicPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        self.label = Label(root, text="AHMAD MAULANA 220511138")
        self.label.pack(pady=20, padx=5)

        self.label = Label(root, text="Nadin : Dirayakan")
        self.label.pack(pady=10, padx=5)

        self.button_play = Button(root, text="Putar Musik", command=self.play_music)
        self.button_play.pack(pady=10, padx=5)

        # Menambahkan gambar untuk tombol jeda dan lanjut
        self.photo_pause = PhotoImage(file="pause.png").subsample(16)
        self.photo_resume = PhotoImage(file="play.png").subsample(16)

        self.button_pause = Button(root, image=self.photo_pause, command=self.pause_resume_music, state="disabled")
        self.button_pause.pack(pady=10)

        # Menambahkan callback untuk menutup mixer saat aplikasi ditutup
        self.root.protocol("WM_DELETE_WINDOW", self.close_app)

        # Menambahkan atribut untuk melacak status musik
        self.music_paused = False

    def play_music(self):
        # Ganti 'tugas/dirayakan.mp3' dengan nama file MP3 yang ingin Anda putar
        file_path = os.path.join(os.getcwd(), "tugas", "dirayakan .mp3")

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
        self.label.config(text=f"Durasi Musik: {duration:.2f} detik")

        # Mengaktifkan tombol putar kembali
        self.button_play.config(state="normal")
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



    def close_app(self):
        # Membersihkan mixer sebelum menutup aplikasi
        pygame.mixer.quit()
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = MusicPlayerApp(root)
    root.mainloop()
