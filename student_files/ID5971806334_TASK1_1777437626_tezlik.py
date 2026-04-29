# ============================================================
# TEZLIK BOSHQARUV DASTURI
# ============================================================

# 7 & 9: Ob-havoga qarab boshlang'ich tezlik
def boshlangich_tezlik(ob_havo):
    if ob_havo == "quyoshli":
        return 110
    elif ob_havo == "yaxshi":
        return 80
    elif ob_havo == "bulutli":   # 1-topshiriq
        return 70
    else:                        # yomgir, qor, tuman = yomon
        return 50

# 8: Yomon ob-havo uchun ogohlantirish funksiyasi
def ob_havo_tekshir(ob_havo):
    yomon_havolar = ["yomgir", "qor", "tuman"]
    if ob_havo in yomon_havolar:
        print("  ⚠  Ehtiyot bo'ling! Yomon ob-havo!")

# ============================================================
# Ma'lumotlarni so'rash
# ============================================================
print("=== TEZLIK HISOBLASH DASTURI ===\n")

ob_havo = input("Ob-havo holati (quyoshli/yaxshi/bulutli/yomgir/qor/tuman): ").strip().lower()
yoqilgi = float(input("Yoqilg'i miqdori (litr): "))            # 2-topshiriq
yuk = float(input("Yuk og'irligi (kg): "))                      # 3-topshiriq
mashina_turi = input("Mashina turi (yuk/yengil): ").strip().lower()  # 4-topshiriq
koprik = input("Ko'prikdan o'tasizmi? (ha/yo'q): ").strip().lower()  # 5-topshiriq
harorat = input("Harorat holati (issiq/sovuq): ").strip().lower()    # 6-topshiriq

# ============================================================
# Tezlikni hisoblash
# ============================================================
tezlik = boshlangich_tezlik(ob_havo)
print(f"\n--- Natijalar ---")
print(f"Boshlang'ich tezlik ({ob_havo}): {tezlik} km/soat")

ob_havo_tekshir(ob_havo)  # 8-topshiriq

# 2: Yoqilg'i kam bo'lsa
if yoqilgi < 10:
    tezlik = min(tezlik, 50)
    print(f"  Yoqilg'i kam ({yoqilgi} l), tezlik pasaydi: {tezlik} km/soat")  # 10

# 3: Yuk chegarasi 1000 kg
if yuk > 1000:
    tezlik = min(tezlik, 30)
    print(f"  Yuk ko'p ({yuk} kg), tezlik pasaydi: {tezlik} km/soat")  # 10

# 4: Mashina turi
if mashina_turi == "yuk":
    tezlik = tezlik - 20
    print(f"  Yuk mashinasi, tezlik 20 km/soatga kamaydi: {tezlik} km/soat")  # 10

# 5: Ko'prikdan o'tish
if koprik == "ha":
    tezlik = min(tezlik, 40)
    print(f"  Ko'prik bor, tezlik cheklandi: {tezlik} km/soat")  # 10

# 6: Harorat
if harorat == "sovuq":
    tezlik = tezlik - 10
    print(f"  Sovuq havo, tezlik 10 km/soatga pasaydi: {tezlik} km/soat")  # 10

tezlik = max(tezlik, 0)

print(f"\n>>> YAKUNIY TEZLIK: {tezlik} km/soat <<<")
