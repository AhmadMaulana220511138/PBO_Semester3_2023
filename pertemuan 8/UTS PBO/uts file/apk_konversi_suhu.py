from tkinter import Tk, StringVar, ttk

def konversi_suhu():
    try:
        suhu_celsius = float(entry_celsius.get())
        satuan_pilihan = satuan_var.get()

        if satuan_pilihan == "Fahrenheit":
            suhu_hasil = (suhu_celsius * 9/5) + 32
        elif satuan_pilihan == "Kelvin":
            suhu_hasil = suhu_celsius + 273.15
        elif satuan_pilihan == "Reamur":
            suhu_hasil = (4/5) * suhu_celsius
        else:  # Default is Celsius
            suhu_hasil = suhu_celsius

        hasil_text = f"Hasil konversi: {suhu_hasil:.2f} {satuan_pilihan}"
        var_hasil.set(hasil_text)

        # Perubahan untuk menengahkan teks di label_hasil
        label_hasil.config(justify='center', anchor='center', foreground='#333', background='#E6E6FA', font=('Helvetica', 12))

    except ValueError:
        var_hasil.set("Masukkan suhu dalam bentuk angka")
        
        # Perubahan untuk menengahkan teks di label_hasil pada kondisi kesalahan
        label_hasil.config(justify='center', anchor='center', foreground='red', background='#E6E6FA', font=('Helvetica', 12))

root = Tk()
root.title("Aplikasi Konversi Suhu")
root.geometry("400x300")
root.configure(background='#E6E6FA')  # Latar belakang warna Azure

# Gaya untuk widget ttk
style = ttk.Style()
style.theme_use('clam')  # Pilih tema yang lebih modern
style.configure('TLabel', font=('Helvetica', 12), foreground='#333', background='#E6E6FA')
style.configure('TButton', font=('Helvetica', 12), foreground='#fff', background='#4CAF50')
style.configure('TEntry', font=('Helvetica', 12), fieldbackground='#fff')
style.configure('TCombobox', font=('Helvetica', 12))

# Label untuk nama dan NIM di bagian atas window
label_wm = ttk.Label(root, text="AHMAD MAULANA 220511138", style='TLabel')
label_wm.pack(pady=10)

# Kolom 1
label_celsius = ttk.Label(root, text="Suhu Celsius:", style='TLabel')
label_celsius.pack(padx=10, pady=5)

entry_celsius = ttk.Entry(root)
entry_celsius.pack(padx=10, pady=5)

# Kolom 2
label_satuan = ttk.Label(root, text="Konversi ke:", style='TLabel')
label_satuan.pack(padx=10, pady=5)

satuan_var = StringVar()
combobox_satuan = ttk.Combobox(root, textvariable=satuan_var, values=["Celsius", "Fahrenheit", "Kelvin", "Reamur"])
combobox_satuan.pack(padx=10, pady=5)

# Kolom 3
button_konversi = ttk.Button(root, text="Konversi", command=konversi_suhu, style='TButton')
button_konversi.pack(pady=10)

# Kolom 4
var_hasil = StringVar()
label_hasil = ttk.Label(root, textvariable=var_hasil, style='TLabel')
label_hasil.pack(padx=10, pady=10, anchor='center')

# Mengatur lebar kolom agar sesuai dengan teks
root.grid_columnconfigure(0, weight=1)

root.mainloop()
