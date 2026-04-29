import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# ============================================================
# TOPSHIRIQ 1: X_train, Y_train uchun boshqa og'uvchi qiymatlar
# ============================================================
print("=" * 50)
print("TOPSHIRIQ 1: Uy narxi bashorati (yangi ma'lumotlar)")
print("=" * 50)

X_train = np.array([[20], [45], [60], [90], [130], [160], [200]])
Y_train = np.array([22000, 45000, 58000, 88000, 125000, 155000, 198000])

model1 = LinearRegression()
model1.fit(X_train, Y_train)
y_pred1 = model1.predict(X_train)

print(f"Formula: y = {model1.coef_[0]:.2f} * x + {model1.intercept_:.2f}")
print(f"R2 score: {r2_score(Y_train, y_pred1):.4f}")
print("Izoh: R2 = 1 ga yaqin bo'lsa, model juda aniq bashorat qilmoqda.")

plt.figure(figsize=(6, 4))
plt.scatter(X_train, Y_train, color='blue', label="Haqiqiy")
plt.plot(X_train, y_pred1, color='red', linewidth=2, label='Bashorat')
plt.xlabel('Uy maydoni (m2)')
plt.ylabel('Narxi ($)')
plt.title('Topshiriq 1: Uy narxi regressiyasi')
plt.legend()
plt.tight_layout()
plt.show()

# ============================================================
# TOPSHIRIQ 2: Ball ga nisbatan baho aniqlash
# ============================================================
print("\n" + "=" * 50)
print("TOPSHIRIQ 2: Talaba bahosi bashorati")
print("=" * 50)

# Ball (0-100) va baho (2-5) orasidagi bog'liqlik
X_ball = np.array([[20], [35], [50], [60], [70], [80], [90], [100]])
Y_baho = np.array([2, 2, 3, 3, 4, 4, 5, 5])

model2 = LinearRegression()
model2.fit(X_ball, Y_baho)

def baho_aniqla(ball):
    bashorat = model2.predict([[ball]])[0]
    baho = round(bashorat)
    baho = max(2, min(5, baho))
    return baho

print(f"Formula: baho = {model2.coef_[0]:.4f} * ball + {model2.intercept_:.4f}")
print()
for ball in [25, 45, 55, 65, 75, 85, 95]:
    print(f"Ball: {ball:3d} → Baho: {baho_aniqla(ball)}")

y_pred2 = model2.predict(X_ball)
plt.figure(figsize=(6, 4))
plt.scatter(X_ball, Y_baho, color='blue', label="Haqiqiy baho")
plt.plot(X_ball, y_pred2, color='red', linewidth=2, label='Bashorat')
plt.xlabel('Ball (0-100)')
plt.ylabel('Baho (2-5)')
plt.title('Topshiriq 2: Ball → Baho regressiyasi')
plt.legend()
plt.tight_layout()
plt.show()

# ============================================================
# TOPSHIRIQ 3: Yandex Go - masofa va to'lov
# ============================================================
print("\n" + "=" * 50)
print("TOPSHIRIQ 3: Yandex Go - masofa va to'lov")
print("=" * 50)

X_km = np.array([[2], [5], [8], [10]])
Y_som = np.array([8000, 17000, 26000, 32000])

model3 = LinearRegression()
model3.fit(X_km, Y_som)
y_pred3 = model3.predict(X_km)

print(f"Formula: to'lov = {model3.coef_[0]:.2f} * km + {model3.intercept_:.2f}")
print(f"R2 score: {r2_score(Y_som, y_pred3):.4f}")
print()

for km in [3, 6, 12, 15]:
    bashorat = model3.predict([[km]])[0]
    print(f"{km} km uchun to'lov: {bashorat:,.0f} so'm")

plt.figure(figsize=(6, 4))
plt.scatter(X_km, Y_som, color='blue', label="Haqiqiy to'lov")
plt.plot(X_km, y_pred3, color='red', linewidth=2, label='Bashorat')
plt.xlabel('Masofa (km)')
plt.ylabel("To'lov (so'm)")
plt.title("Topshiriq 3: Yandex Go regressiyasi")
plt.legend()
plt.tight_layout()
plt.show()

# ============================================================
# TOPSHIRIQ 4: Telefon quvvati - o'chish vaqtini bashorat
# ============================================================
print("\n" + "=" * 50)
print("TOPSHIRIQ 4: Telefon quvvati bashorati")
print("=" * 50)

# Vaqt (soat) va quvvat (%) kuzatuvlari
X_soat = np.array([[0], [1], [2], [3], [4], [5]])
Y_quvvat = np.array([100, 88, 74, 61, 47, 35])

model4 = LinearRegression()
model4.fit(X_soat, Y_quvvat)

print(f"Formula: quvvat = {model4.coef_[0]:.2f} * soat + {model4.intercept_:.2f}")
print(f"R2 score: {r2_score(Y_quvvat, model4.predict(X_soat)):.4f}")

# 0% bo'lishi uchun: 0 = coef * t + intercept → t = -intercept / coef
ochish_vaqti = -model4.intercept_ / model4.coef_[0]
print(f"\nTelefon taxminan {ochish_vaqti:.1f} soatdan keyin o'chadi.")

# Grafik uchun vaqt oralig'i
X_line = np.linspace(0, ochish_vaqti + 1, 100).reshape(-1, 1)
Y_line = model4.predict(X_line)

plt.figure(figsize=(6, 4))
plt.scatter(X_soat, Y_quvvat, color='blue', label="Kuzatilgan quvvat")
plt.plot(X_line, Y_line, color='red', linewidth=2, label='Bashorat')
plt.axhline(0, color='black', linestyle='--', linewidth=1)
plt.axvline(ochish_vaqti, color='green', linestyle='--', label=f"O'chish: {ochish_vaqti:.1f} soat")
plt.xlabel('Vaqt (soat)')
plt.ylabel('Quvvat (%)')
plt.title("Topshiriq 4: Telefon quvvati bashorati")
plt.legend()
plt.tight_layout()
plt.show()