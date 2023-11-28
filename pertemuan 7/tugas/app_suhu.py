from tkinter import Tk, StringVar, ttk

def konversi_suhu():
    try:
        suhu_celsius = float(entry_celsius.get())
        suhu_fahrenheit = (suhu_celsius * 9/5) + 32
        suhu_kelvin = suhu_celsius + 273.15

        hasil_text = (
            f"Hasil konversi:\n"
            f"{suhu_fahrenheit:.2f} Fahrenheit\n"
            f"{suhu_kelvin:.2f} Kelvin"
        )
        var_hasil.set(hasil_text)
        
        # Perubahan untuk menengahkan teks di label_hasil
        label_hasil.config(justify='center', anchor='center', foreground='#333', background='#F0FFFF', font=('Helvetica', 12))

    except ValueError:
        var_hasil.set("Masukkan suhu dalam bentuk angka")
        
        # Perubahan untuk menengahkan teks di label_hasil pada kondisi kesalahan
        label_hasil.config(justify='center', anchor='center', foreground='red', background='#F0FFFF', font=('Helvetica', 12))

root = Tk()
root.title("Aplikasi Konversi Suhu")

# Latar belakang gradasi warna Azure
root.configure(background='#E6E6FA')

# Gaya untuk widget ttk
style = ttk.Style()
style.theme_use('clam')  # Pilih tema yang lebih modern
style.configure('TLabel', font=('Helvetica', 12), foreground='#333', background='#F0FFFF')
style.configure('TButton', font=('Helvetica', 12), foreground='#fff', background='#4CAF50')
style.configure('TEntry', font=('Helvetica', 12), fieldbackground='#fff')

label_celsius = ttk.Label(root, text="Suhu Celsius:", style='TLabel')
label_celsius.grid(row=0, column=0, padx=10, pady=10, sticky='w')

entry_celsius = ttk.Entry(root)
entry_celsius.grid(row=0, column=1, padx=10, pady=10)

button_konversi = ttk.Button(root, text="Konversi", command=konversi_suhu, style='TButton')
button_konversi.grid(row=1, column=0, columnspan=2, pady=10)

var_hasil = StringVar()
label_hasil = ttk.Label(root, textvariable=var_hasil, style='TLabel')
label_hasil.grid(row=2, column=0, columnspan=2, pady=10, sticky='nsew')

# Mengatur lebar kolom agar sesuai dengan teks
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()
