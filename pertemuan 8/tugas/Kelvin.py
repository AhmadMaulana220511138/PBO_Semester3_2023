class Kelvin:
    def __init__(self, suhu):
        self.suhu = suhu

    def get_kelvin(self):
        return self.suhu

    def get_celcius(self):
        val = self.suhu - 273.15  # Konversi dari Kelvin ke Celcius
        return val
    
    def get_fahrenheit(self):
        val = 9/5 * (self.suhu - 273.15) + 32  # Konversi dari Kelvin ke Fahrenheit
        return val

    def get_reamur(self):
        val = 4/5 *(self.suhu - 273.15)   # Konversi dari Kelvin ke Reamur
        return val
    

K = Kelvin(60)
val_k = K.get_kelvin()
C = K.get_celcius()
F = K.get_fahrenheit()
R = K.get_reamur()

print(str(val_k) + " Kelvin, sama dengan:")
print(str(C) + " Celcius")
print(str(F) + " Fahrenheit")
print(str(R) + " Reamur")