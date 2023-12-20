print("Konversi Suhu Kelvin")

# Entry
suhu = input("Masukkan suhu dalam Kelvin:")

# rumus
C = (float (suhu)) - 32
F = (9/5 * float(suhu) + 32) - 273
R = (4/5 * float (suhu)) - 273


#output
print(suhu + " Kelvin, sama dengan ")
print(str(C) + " Celcius ")
print(str(F) + " Fahrenheit ")
print(str(R) + " Reamur ")