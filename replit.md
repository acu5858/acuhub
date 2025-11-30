# ACU.HUB | Simulation Admin Panel

## Proje Özeti
Türkiye simülasyonunda hayatta kalanlar için geliştirilmiş Pastel tema web portalı. 15 pratik araç ve 10 kişilik testi içerir.

## Teknoloji Stack
- **Backend:** Python 3.11, Flask
- **Frontend:** HTML5, CSS3 (CSS Variables, Grid, Flexbox), Vanilla JavaScript (ES6+)
- **Templating:** Jinja2
- **Font:** JetBrains Mono (Google Fonts)
- **Theme:** Pastel (Soft Green #9dd89d, Light Gray #fafafa)

## Dosya Yapısı
```
├── main.py              # Flask routes ve API endpoints
├── logic.py             # 12 aracın iş mantığı
├── tests_data.py        # 10 testin soruları ve sonuçları
├── templates/
│   ├── base.html        # Ana şablon (navbar, footer)
│   ├── dashboard.html   # Ana sayfa (Bento Grid)
│   ├── tool.html        # Araç detay sayfası
│   ├── tests.html       # Test listesi
│   ├── test_detail.html # Test çözme sayfası
│   └── 404.html         # Hata sayfası
├── static/
│   ├── css/
│   │   └── style.css    # Matrix/Cyberpunk tema
│   └── js/
│       └── script.js    # Frontend mantığı
└── attached_assets/     # Ekli dosyalar
```

## Araçlar (15 Adet)
1. **Vize-Final Hesaplayıcı** - Finalden kaç alman gerektiğini hesaplar
2. **KYK/Enflasyon Bütçesi** - Makarna diyeti başlangıç günü
3. **Yalan Dedektörü** - Kolpa analizi (random)
4. **GitHub Readme Generator** - Havalı profil oluşturucu
5. **Kaos Seviyesi Ölçer** - Bugün dışarı çıkmalı mısın?
6. **Kurumsal Çevirici** - Beyaz yaka dili
7. **Bahane Üretici PRO** - Teknik bahaneler
8. **Yemek Çarkı** - Rastgele yemek seçici
9. **Pomodoro Timer** - Zamanlayıcı
10. **Şifre Güçlendirici** - Şifre analizi ve öneri
11. **Döviz Ağlama Duvarı** - Kur takibi (simüle)
12. **Mühendislik Alanı Seçici** - Rastgele mühendislik dalı
13. **Renk Seçici** - Rastgele pastel renk üretici
14. **Metin Kasa** - Base64/ROT13 şifreleme
15. **GNO Hesaplayıcı** - Not ortalaması hesaplayıcı

## Testler (10 Adet)
1. Ruhun Hangi 'Dayı' Tipi?
2. Hangi İstanbul Toplu Taşıma Aracısın?
3. Mental Çöküşe Ne Kadar Kaldı?
4. Hangi Yazılım Hatasısın?
5. Sosyal Pilin Kaç mAh?
6. Hangi Türk Dizisi Karakterisin?
7. Gelecekteki Gerçekçi Mesleğin?
8. Hangi Sokak Lezzetisin?
9. Sabır Seviyen Nedir?
10. Simülasyondaki Rolün Ne?

## API Endpoints
### Araçlar
- `POST /api/vize-final` - Vize-final hesaplama
- `POST /api/kyk-butce` - Bütçe hesaplama
- `POST /api/yalan-dedektor` - Kolpa analizi
- `POST /api/github-readme` - README üretme
- `POST /api/kaos-olcer` - Kaos seviyesi
- `POST /api/kurumsal-cevirici` - Kurumsal çeviri
- `POST /api/bahane-uretici` - Bahane üretme
- `POST /api/yemek-carki` - Yemek seçimi
- `POST /api/pomodoro` - Pomodoro ayarları
- `POST /api/sifre-guc` - Şifre analizi
- `POST /api/doviz-duvari` - Döviz kurları
- `POST /api/muhendislik-secici` - Mühendislik seçimi
- `POST /api/renk-secici` - Pastel renk üretme
- `POST /api/metin-kasa` - Base64/ROT13 şifreleme
- `POST /api/gno-hesap` - GNO hesaplama

### Testler
- `POST /api/test-result` - Test sonucu hesaplama

## Tasarım Sistemi
- **Tema:** Pastel, Soft & Aesthetic
- **Arka plan:** #fafafa (Açık gri)
- **Accent:** #9dd89d (Pastel yeşil)
- **Secondary:** #f0f0f0 (Açık gri-2)
- **Layout:** Bento Grid
- **Efektler:** Soft shadows, gentle transitions
- **Responsive:** 4→3→2→1 sütun
- **Features:** Arama çubuğu, kategori filtreleme

## Yeni Özellikler
- **Arama Motoru:** Araçları isimle ara
- **Kategori Tabs:** Araçları kategoriye göre filtrele (akademik, tech, finans, etc.)

## Çalıştırma
```bash
python main.py
```
Server 0.0.0.0:5000 portunda çalışır.

## Önemli Notlar
- Romantik içerik YOK (eski sevgili, aşk analizi gibi modüller çıkarıldı)
- Tamamen hayat, kaos, okul ve kariyer odaklı
- Onedio tarzı testler ama daha Z kuşağı ve mizahi
