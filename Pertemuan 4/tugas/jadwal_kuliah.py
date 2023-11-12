import tkinter as tk
from tkinter import ttk

def tambah_jadwal():
    mata_kuliah = combo_mata_kuliah.get()
    ruang = entry_ruang.get()
    gedung = combo_gedung.get()
    hari = combo_hari.get()
    jam_mulai = entry_jam_mulai.get()
    jam_selesai = entry_jam_selesai.get()
    dosen = entry_dosen.get()

    # Menambahkan data ke dalam treeview
    tree.insert("", "end", values=(mata_kuliah, ruang, gedung, hari, jam_mulai, jam_selesai, dosen))

    # Mengosongkan input setelah menambahkan data
    entry_ruang.delete(0, "end")
    entry_jam_mulai.delete(0, "end")
    entry_jam_selesai.delete(0, "end")
    entry_dosen.delete(0, "end")

# Membuat window
window = tk.Tk()
window.title("Jadwal Kuliah")

# Menambahkan warna latar belakang pada jendela
window.configure(background="lightgrey")

# Label Nama
Nama = tk.Label(window, text="AHMAD MAULANA (220511138)", bg='lightgrey')

# Membuat label dan entry untuk setiap kolom
label_mata_kuliah = tk.Label(window, text="Mata Kuliah  :", bg='lightgrey')
mata_kuliah_options = ["Pemograman 2 (PBO)", "Arsitektur dan Organisasi Komputer", "AIK 2 (Ibadah, Akhlak dan Muamalah)", "Komunikasi Data", "Struktur Data dan Algoritma", "Statistik dan Probabilitas", "Kalkulus 2", "Sistem Informasi (APSI)"]
combo_mata_kuliah = ttk.Combobox(window, values=mata_kuliah_options)

label_ruang = tk.Label(window, text="Ruang  :", bg='lightgrey')
entry_ruang = tk.Entry(window)

label_gedung = tk.Label(window, text="Gedung    :", bg='lightgrey')
gedung_options = ["Ir.H.Djuanda", "Machdor"]
combo_gedung = ttk.Combobox(window, values=gedung_options)

label_hari = tk.Label(window, text="Hari    :", bg='lightgrey')
hari_options = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
combo_hari = ttk.Combobox(window, values=hari_options)

label_jam_mulai = tk.Label(window, text="Jam Mulai  :", bg='lightgrey')
entry_jam_mulai = tk.Entry(window)

label_jam_selesai = tk.Label(window, text="Jam Selesai  :", bg='lightgrey')
entry_jam_selesai = tk.Entry(window)

label_dosen = tk.Label(window, text="Dosen  :", bg='lightgrey')
entry_dosen = tk.Entry(window)

# Membuat tombol untuk menambahkan jadwal
tombol_tambah = tk.Button(window, text="Tambah Jadwal", command=tambah_jadwal, bg='light green')

# Membuat Treeview untuk menampilkan jadwal
columns = ("Mata Kuliah", "Ruang", "Gedung", "Hari", "Jam Mulai", "Jam Selesai", "Dosen")
tree = ttk.Treeview(window, columns=columns, show="headings")

# Menambahkan heading untuk setiap kolom
for col in columns:
    tree.heading(col, text=col)
    if col == "Mata Kuliah":
        tree.column(col, width=230, stretch=tk.NO)
    else:
        tree.column(col, width=150)

# Menempatkan elemen-elemen pada grid
Nama.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
label_mata_kuliah.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
combo_mata_kuliah.grid(row=1, column=2, padx=10, pady=5, sticky="ew")
label_ruang.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
entry_ruang.grid(row=2, column=2, padx=10, pady=5, sticky="ew")
label_gedung.grid(row=3, column=0, padx=10, pady=5, sticky="ew")
combo_gedung.grid(row=3, column=2, padx=10, pady=5, sticky="ew")
label_hari.grid(row=4, column=0, padx=10, pady=5, sticky="ew")
combo_hari.grid(row=4, column=2, padx=10, pady=5, sticky="ew")
label_jam_mulai.grid(row=5, column=0, padx=10, pady=5, sticky="ew")
entry_jam_mulai.grid(row=5, column=2, padx=10, pady=5, sticky="ew")
label_jam_selesai.grid(row=6, column=0, padx=10, pady=5, sticky="ew")
entry_jam_selesai.grid(row=6, column=2, padx=10, pady=5, sticky="ew")
label_dosen.grid(row=7, column=0, padx=10, pady=5, sticky="ew")
entry_dosen.grid(row=7, column=2, padx=10, pady=5, sticky="ew")
tombol_tambah.grid(row=8, column=1, columnspan=1, pady=10)
tree.grid(row=9, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")

# Mengatur proporsi kolom dan baris agar dapat melebar dan mengisi window
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.rowconfigure(9, weight=1)

# Menjalankan main loop
window.mainloop()
