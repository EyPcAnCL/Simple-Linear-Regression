import numpy as np
import pandas as pd
from scipy import stats

# Her çalıştırmada farklı veri!
n = np.random.randint(20, 50)
x = np.random.randint(1, 100, size=n)
# y'yi x'e bağımlı ama biraz gürültülü (noise) üretiyoruz
gercek_egim = round(np.random.uniform(0.5, 3), 2)
gercek_sabit = np.random.randint(5, 50)
gurultu = np.random.normal(0, 10, size=n)
y = gercek_egim * x + gercek_sabit + gurultu

x = pd.Series(x)
y = pd.Series(y)

# Regresyon hesabı
egim, sabit, r_degeri, p_deger, std_hata = stats.linregress(x, y)

# Tahmin fonksiyonu
def tahmin_et(x_yeni):
    return egim * x_yeni + sabit

# Örnek tahmin
yeni_x = np.random.randint(1, 100)
tahmini_y = tahmin_et(yeni_x)

print("=" * 48)
print("📌 BASİT DOĞRUSAL REGRESYON")
print("=" * 48)
print(f"Örneklem Büyüklüğü (n)  : {n}")
print(f"X Verisi (ilk 5)        : {x[:5].tolist()}")
print(f"Y Verisi (ilk 5)        : {[round(v,1) for v in y[:5].tolist()]}")
print("-" * 48)
print(f"Regresyon Denklemi      : y = {egim:.2f}x + {sabit:.2f}")
print("-" * 48)
print(f"Eğim (Slope)            : {egim:.4f}")
print(f"Sabit (Intercept)       : {sabit:.4f}")
print(f"R Değeri (Korelasyon)   : {r_degeri:.4f}")
print(f"R² Değeri (Açıklayıcılık): {r_degeri**2:.4f}")
print(f"P Değeri                : {p_deger:.4f}")
print(f"Standart Hata           : {std_hata:.4f}")
print("-" * 48)
print(f"🔮 Tahmin: x = {yeni_x} için y = {tahmini_y:.2f}")
print("=" * 48)

if p_deger < 0.05:
    print("✅ X ve Y arasında anlamlı bir doğrusal ilişki var!")
else:
    print("❌ X ve Y arasında anlamlı bir ilişki bulunamadı.")
print("=" * 48)
