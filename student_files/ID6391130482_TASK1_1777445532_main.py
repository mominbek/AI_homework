ob_havo = input("Ob-havo qanday? (yaxshi/yomon/bulutli/quyoshli): ").lower()
yuk_holati = int(input("Mashinadagi yuk og‘irligi (kg): "))
yoqilgi = int(input("Yoqilg‘i miqdori (litr): "))
mashina_turi = input("Mashina turi (yuk/yengil): ").lower()
koprik = input("Ko‘prikdan o‘tish (ha/yo‘q): ").lower()
harorat = input("Harorat (issiq/sovuq): ").lower()

# 1 va 9-topshiriq: ob-havo holatlari
if ob_havo == "yaxshi":
    tezlik = 100
    print("Yaxshi ob-havo")
elif ob_havo == "yomon":
    tezlik = 60
    print("Yomon ob-havo")
elif ob_havo == "bulutli":
    tezlik = 70
    print("Bulutli ob-havo")
elif ob_havo == "quyoshli":
    tezlik = 110
    print("Quyoshli ob-havo")
else:
    tezlik = 60
    print("Noma'lum ob-havo")

# 2-topshiriq: yoqilg‘i
if yoqilgi < 10:
    tezlik = 50
    print("Yoqilg‘i kam, tezlik 50 ga tushirildi")

# 3-topshiriq: yuk > 1000
if yuk_holati > 1000:
    tezlik = 30
    print("Yuk 1000 kg dan oshdi, tezlik 30 ga tushirildi")

# 4-topshiriq: mashina turi
if mashina_turi == "yuk":
    tezlik -= 20
    print("Yuk mashinasi, tezlik 20 ga kamaydi")

# 5-topshiriq: ko‘prik
if koprik == "ha":
    if tezlik > 40:
        tezlik = 40
    print("Ko‘prikdan o‘tish, tezlik 40 dan oshmaydi")

# 6-topshiriq: harorat
if harorat == "sovuq":
    tezlik -= 10
    print("Sovuq havo, tezlik kamaydi")

# 7-topshiriq (alohida soddalashtirilgan variant)
print("\nSoddalashtirilgan variant:")
if ob_havo == "yaxshi":
    print("Tezlik: 80 km/soat")
else:
    print("Tezlik: 50 km/soat")

# 8-topshiriq: funksiya
def ehtiyot():
    print("Ehtiyot bo‘ling!")

if ob_havo == "yomon":
    ehtiyot()

# manfiy bo‘lib ketmasin
if tezlik < 0:
    tezlik = 0

# 10-topshiriq: yakuniy natija
print(f"\nTavsiya qilingan tezlik: {tezlik} km/soat")