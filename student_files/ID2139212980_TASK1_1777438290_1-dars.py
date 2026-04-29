#  Yomon ob-havo uchun funksiya
def ehtiyot_boling():
    print(" Ehtiyot bo‘ling! Ob-havo yomon.")

# Ob-havoga qarab boshlang‘ich tezlik
ob_havo = input("Ob-havo (yaxshi/yomon/bulutli/quyoshli): ").lower()

if ob_havo == "yaxshi":
    tezlik = 80
elif ob_havo == "yomon":
    tezlik = 50
    ehtiyot_boling()
elif ob_havo == "bulutli":
    tezlik = 70
    print(" Bulutli ob-havo, tezlik 70 km/soat")
elif ob_havo == "quyoshli":
    tezlik = 110
    print(" Quyoshli ob-havo, tezlik 110 km/soat")
else:
    tezlik = 60
    print(" Noma'lum ob-havo, standart tezlik 60 km/soat")

#  Yoqilg‘i tekshirish
yoqilgi = float(input("Yoqilg‘i miqdori (litr): "))
if yoqilgi < 10:
    tezlik = min(tezlik, 50)
    print(" Yoqilg‘i kam, tezlik 50 km/soatgacha tushirildi")

#  Yuk tekshirish
yuk = float(input("Yuk miqdori (kg): "))
if yuk > 1000:
    tezlik = min(tezlik, 30)
    print(" Yuk ko‘p, tezlik 30 km/soatga tushirildi")

#  Mashina turi
mashina = input("Mashina turi (yuk/yengil): ").lower()
if mashina == "yuk":
    tezlik -= 20
    print(" Yuk mashinasi, tezlik 20 ga kamaytirildi")

# 5. Ko‘prikdan o‘tish
koprik = input("Ko‘prikdan o‘tish (ha/yo‘q): ").lower()
if koprik == "ha":
    tezlik = min(tezlik, 40)
    print(" Ko‘prik, tezlik 40 km/soat bilan cheklangan")

#  Harorat
harorat = input("Harorat (issiq/sovuq): ").lower()
if harorat == "sovuq":
    tezlik -= 10
    print(" Sovuq ob-havo, tezlik 10 ga kamaytirildi")


if tezlik < 0:
    tezlik = 0

print(f" Yakuniy tezlik: {tezlik} km/soat")