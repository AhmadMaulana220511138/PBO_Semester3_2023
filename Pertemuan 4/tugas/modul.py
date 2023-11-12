def hitung_luas_balok(p, l, t):
    Luas = round (2*(p*l) + 2*(p*t) + 2*(l*t))
    return Luas

def hitung_volume_balok(p, l, t):
    Volume = p * l * t 
    return Volume

def hitung_luas_bola(jarijari):
    luas = 4*3.14*jarijari**2
    return luas

def hitung_volume_bola(jarijari):
    Volume = 4/3*3.14*jarijari**3
    return Volume

def hitung_luasselimut_kerucut(jarijari, sisi):
    luasselimut = 3.14*jarijari*sisi
    return luasselimut

def hitung_luaspermukaan_kerucut(jarijari, sisi):
    luaspermukaan = 3.14*jarijari*sisi
    return luaspermukaan

def hitung_luasvolume_kerucut(jarijari, tinggi):
    luasvolume = 1/3*3.14*jarijari**2*tinggi
    return luasvolume

def hitung_luas_kubus(R):
    Luas = 6 * (R * R)
    return Luas

def hitung_volume_kubus(R):
    Volume = R * R * R
    return Volume

def hitung_luas_limassegiempat(sisi, tinggisegitiga):
    Luas = (sisi*sisi)+(4*sisi*tinggisegitiga/2)
    return Luas

def hitung_volume_limassegiempat(sisi, tinggilimas):
    Volume = 1/3*(sisi*sisi)*tinggilimas
    return Volume

def hitung_luaspermukaan_limassegitiga(alassegitiga, tinggisegitiga, tinggilimas):
    luas = 4*(1/2*alassegitiga*tinggisegitiga)*tinggilimas
    return luas

def hitung_volume_limassegitiga(alassegitiga, tinggisegitiga, tinggilimas):
    Volume =  1/3*(1/2*alassegitiga*tinggisegitiga)*tinggilimas
    return Volume

def hitung_luasalas_prismasegitiga(sisi1, sisi2, sisi3, tinggiprisma):
    luasalas = ( sisi1 + sisi2 + sisi3 ) * tinggiprisma
    return luasalas

def hitung_luassisi_prismasegitiga(sisi1, sisi2, sisi3, tinggiprisma, alas, tinggi):
    luassisi = ( sisi1 + sisi2 + sisi3 ) * tinggiprisma + alas * tinggi
    return luassisi

def hitung_volume_prismasegitiga(alas, tinggi, tinggiprisma):
    volume = ( alas * tinggi ) / 2 * tinggiprisma
    return volume

def hitung_luasselimut_tabung(jarijari, tinggi):
    luasselimut = 2*3.14*jarijari*tinggi
    return luasselimut

def hitung_luaspermukaan_tabung(jarijari, tinggi):
    luaspermukaan = 2*3.14*jarijari*tinggi+2*3.14*jarijari**2
    return luaspermukaan

def hitung_volume_tabung(jarijari, tinggi):
    Volume = 3.14*jarijari**2*tinggi
    return Volume