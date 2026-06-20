## 📈 Basit Doğrusal Regresyon (Simple Linear Regression)

İki değişken arasındaki ilişkiyi bir doğru denklemiyle modelleyip
tahmin yapmamızı sağlar.

**Formül:**
y = mx + b  →  m: eğim, b: sabit (intercept)

**Kodda ne yaptım?**
1. Rastgele bir x verisi ve buna bağımlı (gürültülü) bir y verisi oluşturdum
2. scipy ile eğim, sabit, R² ve p değerini hesapladım
3. Bulduğum denklemle yeni bir x değeri için tahmin yaptım 🔮

**Önemli Kavramlar:**
- **Eğim (m)** → X bir birim artınca Y'nin ne kadar değiştiği
- **Sabit (b)** → Doğrunun Y eksenini kestiği nokta
- **R²** → Modelin veriyi ne kadar iyi açıkladığı (0-1 arası)
- **P Değeri** → İlişkinin istatistiksel olarak anlamlı olup olmadığı

**Kullanılan kütüphaneler:** `numpy`, `pandas`, `scipy`
