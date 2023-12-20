class Reamur:
    def __init__(self, suhu):
        self.suhu = suhu

    def get_reamur(self):
        return self.suhu

    def get_celcius(self):
        val = (5/4) * self.suhu  # Mengubah rumus ke (5/4) * self.suhu
        return val
    
    def get_fahrenheit(self):
        val = ((9/4) * self.suhu) + 32  # Mengubah rumus ke ((9/4) * self.suhu) + 32
        return val

    def get_kelvin(self):
        val = ((5/4) * self.suhu) + 273.15  # Mengubah rumus ke ((5/4) * self.suhu) + 273.15
        return val


"""R = Reamur(60)
val = R.get_reamur()
C = R.get_celcius()
F = R.get_fahrenheit()
K = R.get_kelvin()

print(str(val) + " Reamur, sama dengan:")
print(str(C) + " Celcius")
print(str(F) + " Fahrenheit")
print(str(K) + " Kelvin")"""
