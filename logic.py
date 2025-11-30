"""
ACU.HUB | Simulation Admin Panel - Business Logic
Türkiye simülasyonunda hayatta kalmak için gerekli araçlar.
"""

import random
from datetime import datetime
from typing import Dict, Any, List

# ============================================================================
# 1. VİZE-FİNAL HESAPLAYICI
# ============================================================================

def calculate_grade(vize: float, vize_weight: int = 40) -> Dict[str, Any]:
    """
    Finalden kaç alman gerektiğini hesaplar.
    """
    if not (0 <= vize <= 100):
        return {"success": False, "error": "Vize notu 0-100 arasında olmalı!"}
    
    final_weight = 100 - vize_weight
    vize_contribution = (vize * vize_weight) / 100
    
    needed_for_50 = max(0, (50 - vize_contribution) * 100 / final_weight)
    needed_for_60 = max(0, (60 - vize_contribution) * 100 / final_weight)
    needed_for_70 = max(0, (70 - vize_contribution) * 100 / final_weight)
    
    if needed_for_50 > 100:
        verdict = "Seneye görüşürüz kardeşim. 🪦"
        status = "FAILED"
        emoji = "💀"
    elif needed_for_50 > 85:
        verdict = "Mucize lazım. Hocaya yalvarmayı düşün."
        status = "CRITICAL"
        emoji = "🆘"
    elif needed_for_50 > 70:
        verdict = "Zor ama imkansız değil. Tüm geceleri sat."
        status = "HARD"
        emoji = "😰"
    elif needed_for_50 > 50:
        verdict = "Makul bir şans var. Çalış."
        status = "POSSIBLE"
        emoji = "📚"
    else:
        verdict = "Rahat geçersin. Ama gevşeme."
        status = "SAFE"
        emoji = "😎"
    
    return {
        "success": True,
        "vize": vize,
        "vize_weight": vize_weight,
        "needed_for_50": round(needed_for_50, 1),
        "needed_for_60": round(needed_for_60, 1),
        "needed_for_70": round(needed_for_70, 1),
        "verdict": verdict,
        "status": status,
        "emoji": emoji
    }


# ============================================================================
# 2. KYK / ENFLASYON BÜTÇESİ
# ============================================================================

EXPENSE_CATEGORIES = [
    {"name": "Yurt/Kira", "min": 2000, "max": 8000},
    {"name": "Yemek", "min": 2500, "max": 5000},
    {"name": "Ulaşım", "min": 500, "max": 1500},
    {"name": "Telefon/İnternet", "min": 200, "max": 500},
    {"name": "Sosyal Aktivite", "min": 0, "max": 1000},
]

def calculate_kyk_budget(income: float, rent: float = 0) -> Dict[str, Any]:
    """
    KYK bütçesi hesaplar, hangi gün makarna diyetine başlayacağını söyler.
    """
    if income <= 0:
        return {"success": False, "error": "Gelir 0'dan büyük olmalı!"}
    
    daily_budget = income / 30
    
    min_daily_expense = 120
    
    if daily_budget >= 300:
        diet_day = 0
        status = "ZENGIN"
        comment = "Sen öğrenci misin yoksa startup kurucusu mu?"
        emoji = "💰"
    elif daily_budget >= 150:
        diet_day = 20
        status = "ORTA"
        comment = "Ayın 20'sinden sonra sıkıntı başlar."
        emoji = "😐"
    elif daily_budget >= 100:
        diet_day = 15
        status = "DAR"
        comment = "Ayın yarısından sonra makarna festivali."
        emoji = "🍝"
    elif daily_budget >= 70:
        diet_day = 10
        status = "KRİTİK"
        comment = "10'undan sonra sadece çay-simit."
        emoji = "🥯"
    else:
        diet_day = 5
        status = "HAYATTA KALMA"
        comment = "5'inden sonra aile desteği şart."
        emoji = "💀"
    
    survival_tips = []
    if daily_budget < 150:
        survival_tips = [
            "Yemekhaneden çıkma",
            "Kahve almayı unut, evde nescafe yap",
            "Toplu taşıma kartını doldur, taksi lüks",
            "Spotify'ı iptal et, YouTube'dan dinle"
        ]
    
    return {
        "success": True,
        "income": income,
        "daily_budget": round(daily_budget, 2),
        "diet_start_day": diet_day,
        "status": status,
        "comment": comment,
        "emoji": emoji,
        "survival_tips": survival_tips
    }


# ============================================================================
# 3. YALAN DEDEKTÖRÜ (Bullshit Detector)
# ============================================================================

BULLSHIT_INDICATORS = [
    "kesinlikle", "yüzde yüz", "inan bana", "yemin ederim",
    "vallahi", "billahi", "cidden", "harbiden", 
    "bir dakika", "hemen", "yarın", "söz veriyorum"
]

BULLSHIT_RESULTS = [
    {"percent": 95, "verdict": "KOLPA ALARM! 🚨", "comment": "Bunu annem de yemez."},
    {"percent": 87, "verdict": "YÜKSEK KOLPA", "comment": "Güvenme, planını değiştir."},
    {"percent": 72, "verdict": "ŞÜPHELİ", "comment": "Bir kere daha sor."},
    {"percent": 45, "verdict": "BELKİ DOĞRU", "comment": "Ama yine de dikkat et."},
    {"percent": 23, "verdict": "MUHTEMELEN DOĞRU", "comment": "Nadir görülen dürüstlük."},
    {"percent": 8, "verdict": "DOĞRU SÖYLÜYOR", "comment": "Şok! Bu kadar dürüstlük görülmedi."},
]

def detect_bullshit(text: str) -> Dict[str, Any]:
    """
    Girilen metnin kolpa olma ihtimalini 'analiz' eder.
    """
    if not text or not text.strip():
        return {"success": False, "error": "Analiz edilecek metin girin!"}
    
    text_lower = text.lower()
    indicator_count = sum(1 for word in BULLSHIT_INDICATORS if word in text_lower)
    
    if indicator_count >= 3:
        result = BULLSHIT_RESULTS[0]
    elif indicator_count >= 2:
        result = BULLSHIT_RESULTS[1]
    else:
        result = random.choice(BULLSHIT_RESULTS)
    
    return {
        "success": True,
        "text": text,
        "percent": result["percent"],
        "verdict": result["verdict"],
        "comment": result["comment"],
        "indicators_found": indicator_count
    }


# ============================================================================
# 4. GITHUB README OLUŞTURUCU
# ============================================================================

TECH_STACKS = [
    ["Python", "Django", "PostgreSQL", "Docker"],
    ["JavaScript", "React", "Node.js", "MongoDB"],
    ["TypeScript", "Next.js", "Prisma", "Vercel"],
    ["Go", "Kubernetes", "Redis", "gRPC"],
    ["Rust", "WebAssembly", "Linux", "Vim"],
    ["Java", "Spring Boot", "AWS", "Jenkins"],
]

HOBBIES = [
    "Kahve içmek ☕", "Bug avlamak 🐛", "Stack Overflow'da yaşamak",
    "Açık kaynak projelere contribute etmek", "Yeni framework denemek",
    "Kod yazmak yerine tweet atmak", "10x developer olmaya çalışmak"
]

def generate_github_readme(name: str, username: str = "") -> Dict[str, Any]:
    """
    Havalı bir GitHub README profili oluşturur.
    """
    if not name or not name.strip():
        return {"success": False, "error": "İsim girin!"}
    
    if not username:
        username = name.lower().replace(" ", "").replace("ı", "i").replace("ö", "o").replace("ü", "u").replace("ş", "s").replace("ğ", "g").replace("ç", "c")
    
    stack = random.choice(TECH_STACKS)
    hobby = random.sample(HOBBIES, 3)
    
    readme = f"""# Merhaba, ben {name}! 👋

## 🚀 Hakkımda
```python
class Developer:
    def __init__(self):
        self.name = "{name}"
        self.role = "Full Stack Developer"
        self.language_spoken = ["tr_TR", "en_US"]
        self.code = ["{stack[0]}", "{stack[1]}", "{stack[2]}"]
        
    def say_hi(self):
        print("Kod yazmayı bırakamam, bu bir yaşam tarzı!")

me = Developer()
me.say_hi()
```

## 🛠️ Tech Stack
![{stack[0]}](https://img.shields.io/badge/-{stack[0]}-black?style=flat-square&logo={stack[0].lower()})
![{stack[1]}](https://img.shields.io/badge/-{stack[1]}-black?style=flat-square&logo={stack[1].lower()})
![{stack[2]}](https://img.shields.io/badge/-{stack[2]}-black?style=flat-square&logo={stack[2].lower()})
![{stack[3]}](https://img.shields.io/badge/-{stack[3]}-black?style=flat-square&logo={stack[3].lower()})

## 📊 GitHub Stats
![GitHub Stats](https://github-readme-stats.vercel.app/api?username={username}&show_icons=true&theme=radical)

## 🎯 Hobiler
- {hobby[0]}
- {hobby[1]}
- {hobby[2]}

## 📫 İletişim
- LinkedIn: linkedin.com/in/{username}
- Twitter: @{username}

---
*"İyi kod, kendini açıklayan koddur."* - Probably someone on Stack Overflow
"""
    
    return {
        "success": True,
        "name": name,
        "username": username,
        "readme": readme,
        "stack": stack
    }


# ============================================================================
# 5. KAOS SEVİYESİ ÖLÇER
# ============================================================================

CHAOS_FACTORS = {
    "trafik": {"weight": 20, "name": "Trafik Cehennemi"},
    "sinav": {"weight": 35, "name": "Sınav Stresi"},
    "uykusuzluk": {"weight": 25, "name": "Uykusuzluk"},
    "deadline": {"weight": 30, "name": "Deadline Paniği"},
    "ekonomi": {"weight": 40, "name": "Ekonomi Haberleri"},
    "aile": {"weight": 15, "name": "Aile Ziyareti"},
    "komsu": {"weight": 10, "name": "Gürültücü Komşu"},
    "internet": {"weight": 20, "name": "İnternet Kesintisi"},
}

def calculate_chaos_level(factors: List[str]) -> Dict[str, Any]:
    """
    Seçilen faktörlere göre kaos seviyesi hesaplar.
    """
    if not factors:
        return {
            "success": True,
            "level": 0,
            "status": "ZEN MASTER",
            "emoji": "🧘",
            "advice": "Bugün her şey yolunda. Nadir bir gün, tadını çıkar!",
            "can_go_out": True
        }
    
    total = sum(CHAOS_FACTORS.get(f, {}).get("weight", 0) for f in factors)
    total = min(100, total)
    
    if total >= 80:
        status = "DEFCON 1"
        emoji = "💥"
        advice = "EVDEN ÇIKMA! Battaniyeye sarıl ve bekle."
        can_go_out = False
    elif total >= 60:
        status = "KRİTİK"
        emoji = "🔥"
        advice = "Sadece zorunlu işler için dışarı çık."
        can_go_out = False
    elif total >= 40:
        status = "YÜKSEK"
        emoji = "⚠️"
        advice = "Dikkatli ol, sinirlerine hakim ol."
        can_go_out = True
    elif total >= 20:
        status = "ORTA"
        emoji = "😤"
        advice = "İdare eder, ama sakin kal."
        can_go_out = True
    else:
        status = "DÜŞÜK"
        emoji = "😌"
        advice = "Rahat bir gün, değerlendir."
        can_go_out = True
    
    return {
        "success": True,
        "level": total,
        "status": status,
        "emoji": emoji,
        "advice": advice,
        "can_go_out": can_go_out,
        "factors": [CHAOS_FACTORS[f]["name"] for f in factors if f in CHAOS_FACTORS]
    }


# ============================================================================
# 6. KURUMSAL ÇEVİRİCİ
# ============================================================================

CORPORATE_TRANSLATIONS = [
    "Bu konuda farklı bir bakış açısı geliştirebiliriz.",
    "Önerinizi değerlendirmek için ek veri analizi yapmamız gerekiyor.",
    "Bu yaklaşımın alternatif çözüm yollarını keşfetmeliyiz.",
    "Fikirleriniz değerli, ancak mevcut KPI'larımızla uyumlu değil.",
    "Bu konuyu bir sonraki sprint'te ele almayı planlıyoruz.",
    "Stakeholder'larla alignment sağlamamız öncelikli.",
    "Bu önerinin ROI'sini hesaplamamız gerekiyor.",
    "Agile metodolojimiz gereği önce backlog'a ekleyelim.",
    "Synergy yaratmak adına cross-functional bir meeting ayarlayalım.",
    "Bu feedback'i iterate etmemiz için zaman gerekiyor."
]

CORPORATE_PREFIXES = [
    "Değerli katkılarınız için teşekkür ederim. ",
    "Bu perspektifi paylaştığınız için memnunum. ",
    "Input'unuz için minnettarız. ",
    "Constructive yaklaşımınızı takdir ediyorum. "
]

def translate_to_corporate(text: str) -> Dict[str, Any]:
    """
    Normal/kaba metni kurumsal dile çevirir.
    """
    if not text or not text.strip():
        return {"success": False, "error": "Çevrilecek metin girin!"}
    
    prefix = random.choice(CORPORATE_PREFIXES)
    translation = random.choice(CORPORATE_TRANSLATIONS)
    
    return {
        "success": True,
        "original": text,
        "translated": prefix + translation,
        "corporate_level": random.randint(85, 100),
        "buzzword_count": random.randint(3, 7)
    }


# ============================================================================
# 7. BAHANE ÜRETİCİ (PRO)
# ============================================================================

TECH_EXCUSES = [
    "Sunucular beklenmedik bir şekilde çöktü, DevOps ekibi müdahale ediyor.",
    "Production'da kritik bir bug tespit ettik, hotfix hazırlanıyor.",
    "CI/CD pipeline'ında beklenmedik bir hata oluştu.",
    "Docker container'ları restart edilmesi gerekti.",
    "Database migration'ı beklenenden uzun sürdü.",
    "Git merge conflict'leri çözülüyor.",
    "AWS'de regional outage yaşandı.",
    "Kubernetes pod'ları crashloop'a girdi.",
    "NPM paketlerinde güvenlik açığı tespit edildi, update gerekti.",
    "Memory leak tespit edildi, profiling yapılıyor.",
    "SSL sertifikası expire olmuş, yenileniyordu.",
    "Load balancer yapılandırması güncellenmesi gerekti.",
    "Redis cache invalidation sorunu yaşandı.",
    "Elasticsearch cluster'ı senkronize ediliyordu.",
    "Microservice'ler arası iletişimde latency sorunu vardı."
]

EXCUSE_TIPS = [
    "Bu bahaneyi kullanırken teknik terimler ekle.",
    "Ekran paylaşımı yapma, 'şu an düzeliyor' de.",
    "Çok detaya girme, karmaşık tutarsan sormazlar.",
    "Son çare: 'Ben de anlamadım, araştırıyorum' de."
]

def generate_tech_excuse() -> Dict[str, Any]:
    """
    Profesyonel teknik bahane üretir.
    """
    excuse = random.choice(TECH_EXCUSES)
    tip = random.choice(EXCUSE_TIPS)
    
    return {
        "success": True,
        "excuse": excuse,
        "tip": tip,
        "credibility": random.randint(70, 95),
        "technical_level": random.randint(1, 5)
    }


# ============================================================================
# 8. YEMEK ÇARKI (RNG)
# ============================================================================

FOOD_OPTIONS = [
    {"name": "Döner", "emoji": "🥙", "risk": "Düşük", "price": "60-80 TL"},
    {"name": "Simit + Çay", "emoji": "🥯", "risk": "Yok", "price": "20-30 TL"},
    {"name": "Kumpir", "emoji": "🥔", "risk": "Düşük", "price": "70-100 TL"},
    {"name": "Lahmacun", "emoji": "🫓", "risk": "Düşük", "price": "40-60 TL"},
    {"name": "Tantuni", "emoji": "🌯", "risk": "Orta", "price": "50-70 TL"},
    {"name": "Pilav Üstü", "emoji": "🍚", "risk": "Düşük", "price": "50-70 TL"},
    {"name": "Köfte Ekmek", "emoji": "🥪", "risk": "Düşük", "price": "60-80 TL"},
    {"name": "Midye", "emoji": "🦪", "risk": "YÜKSEK ⚠️", "price": "30-50 TL"},
    {"name": "Kokoreç", "emoji": "🫕", "risk": "Orta-Yüksek", "price": "70-100 TL"},
    {"name": "Islak Hamburger", "emoji": "🍔", "risk": "Orta", "price": "30-50 TL"},
    {"name": "Martı Eti (Şaka)", "emoji": "🐦", "risk": "???", "price": "Priceless"},
    {"name": "Ev Yemeği (Annenin)", "emoji": "🏠", "risk": "Negatif", "price": "Bedava + Sevgi"}
]

def spin_food_wheel() -> Dict[str, Any]:
    """
    Yemek çarkını döndürür.
    """
    selected = random.choice(FOOD_OPTIONS)
    
    return {
        "success": True,
        "selected": selected,
        "alternatives": random.sample([f for f in FOOD_OPTIONS if f != selected], 2),
        "advice": f"Bugün {selected['name']} ye! Risk seviyesi: {selected['risk']}"
    }


# ============================================================================
# 9. POMODORO TIMER (Matrix Style)
# ============================================================================

def get_pomodoro_settings(mode: str = "work") -> Dict[str, Any]:
    """
    Pomodoro timer ayarlarını döndürür.
    """
    settings = {
        "work": {"duration": 25, "label": "WORK_MODE", "next": "break"},
        "break": {"duration": 5, "label": "BREAK_MODE", "next": "work"},
        "long_break": {"duration": 15, "label": "LONG_BREAK", "next": "work"}
    }
    
    current = settings.get(mode, settings["work"])
    
    return {
        "success": True,
        "mode": mode,
        "duration_minutes": current["duration"],
        "duration_seconds": current["duration"] * 60,
        "label": current["label"],
        "next_mode": current["next"]
    }


# ============================================================================
# 10. ŞİFRE GÜÇLENDİRİCİ
# ============================================================================

WEAK_PASSWORD_ROASTS = [
    "Bunu babam da kırar.",
    "2 saniyede hacklenirsin.",
    "Bu şifre değil, davetiye.",
    "Hacker'lar teşekkür eder.",
    "Password123 bile bundan iyi."
]

def analyze_and_strengthen_password(password: str) -> Dict[str, Any]:
    """
    Şifreyi analiz eder ve güçlendirilmiş versiyon önerir.
    """
    if not password:
        return {"success": False, "error": "Şifre girin!"}
    
    score = 0
    issues = []
    
    if len(password) >= 8:
        score += 20
    else:
        issues.append("En az 8 karakter olmalı")
    
    if len(password) >= 12:
        score += 10
    
    if any(c.isupper() for c in password):
        score += 20
    else:
        issues.append("Büyük harf ekle")
    
    if any(c.islower() for c in password):
        score += 10
    else:
        issues.append("Küçük harf ekle")
    
    if any(c.isdigit() for c in password):
        score += 20
    else:
        issues.append("Rakam ekle")
    
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        score += 20
    else:
        issues.append("Özel karakter ekle (!@#$%)")
    
    common_passwords = ["123456", "password", "qwerty", "abc123", "111111", "admin"]
    if password.lower() in common_passwords:
        score = 0
        issues = ["Bu şifre çok yaygın, herkes biliyor!"]
    
    if score < 30:
        strength = "ÇOK ZAYIF"
        roast = random.choice(WEAK_PASSWORD_ROASTS)
        emoji = "💀"
    elif score < 50:
        strength = "ZAYIF"
        roast = "Biraz daha çaba lazım."
        emoji = "😰"
    elif score < 70:
        strength = "ORTA"
        roast = "İdare eder ama geliştirebilirsin."
        emoji = "😐"
    elif score < 90:
        strength = "GÜÇLÜ"
        roast = "Fena değil, kullanabilirsin."
        emoji = "💪"
    else:
        strength = "ÇOK GÜÇLÜ"
        roast = "CIA bile kıramaz. Sadece unutma!"
        emoji = "🔒"
    
    import string
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    strong_password = ''.join(random.choice(chars) for _ in range(16))
    
    return {
        "success": True,
        "original": password,
        "score": score,
        "strength": strength,
        "roast": roast,
        "emoji": emoji,
        "issues": issues,
        "suggested": strong_password
    }


# ============================================================================
# 11. DOLAR/EURO AĞLAMA DUVARI
# ============================================================================

def get_currency_wall() -> Dict[str, Any]:
    """
    Döviz kurlarını gösterir (simüle edilmiş).
    """
    usd = round(random.uniform(32.5, 35.5), 2)
    eur = round(random.uniform(35.0, 38.5), 2)
    gbp = round(random.uniform(40.0, 44.0), 2)
    
    sad_comments = [
        "PC toplamak hayal oldu.",
        "Steam indirimlerinin anlamı kalmadı.",
        "Amazon'a bakmak artık eziyet.",
        "Dolar mı, rüya mı belli değil.",
        "iPhone almak: Böbrek + Karaciğer",
        "PS5 = 2 aylık maaş"
    ]
    
    return {
        "success": True,
        "rates": {
            "USD": {"value": usd, "emoji": "🇺🇸"},
            "EUR": {"value": eur, "emoji": "🇪🇺"},
            "GBP": {"value": gbp, "emoji": "🇬🇧"}
        },
        "sad_comment": random.choice(sad_comments),
        "pc_dream_status": "CANCELLED",
        "timestamp": datetime.now().strftime("%H:%M:%S")
    }


# ============================================================================
# 12. MÜHENDİSLİK ALANI SEÇİCİ
# ============================================================================

ENGINEERING_FIELDS = [
    {"name": "Yazılım Mühendisliği", "salary": "25.000 - 80.000 TL", "stress": "Yüksek", "job": "Bol", "emoji": "💻"},
    {"name": "Makine Mühendisliği", "salary": "20.000 - 45.000 TL", "stress": "Orta", "job": "Orta", "emoji": "⚙️"},
    {"name": "Elektrik Mühendisliği", "salary": "22.000 - 50.000 TL", "stress": "Orta", "job": "Orta", "emoji": "⚡"},
    {"name": "İnşaat Mühendisliği", "salary": "20.000 - 40.000 TL", "stress": "Yüksek", "job": "Değişken", "emoji": "🏗️"},
    {"name": "Endüstri Mühendisliği", "salary": "22.000 - 55.000 TL", "stress": "Orta", "job": "Bol", "emoji": "📊"},
    {"name": "Biyomedikal Mühendisliği", "salary": "20.000 - 45.000 TL", "stress": "Orta", "job": "Az", "emoji": "🏥"},
    {"name": "Gıda Mühendisliği", "salary": "18.000 - 35.000 TL", "stress": "Düşük", "job": "Az", "emoji": "🍕"},
    {"name": "Çevre Mühendisliği", "salary": "18.000 - 35.000 TL", "stress": "Düşük", "job": "Az", "emoji": "🌿"},
    {"name": "Tesisat Mühendisliği", "salary": "20.000 - 38.000 TL", "stress": "Düşük", "job": "Gizli İmkan", "emoji": "🔧"},
    {"name": "Uzay Mühendisliği", "salary": "25.000 - 60.000 TL", "stress": "Çok Yüksek", "job": "Nadir", "emoji": "🚀"},
]

SOUL_COMMENTS = [
    "Senin ruhun tam bu alana uygun!",
    "Kader seni buraya yönlendirdi.",
    "Simülasyon sana bunu uygun gördü.",
    "Başka seçeneğin yok, kabullen.",
    "DNA'nda bu yazıyormuş."
]

def select_engineering_field() -> Dict[str, Any]:
    """
    Rastgele mühendislik alanı seçer.
    """
    field = random.choice(ENGINEERING_FIELDS)
    
    return {
        "success": True,
        "field": field,
        "soul_comment": random.choice(SOUL_COMMENTS),
        "reality_check": "Ama sonuçta hepsi mühendislik, iş bulursan şanslısın."
    }


# ============================================================================
# 13. RENK SEÇİCİ
# ============================================================================

def generate_random_color() -> Dict[str, Any]:
    """
    Rastgele pastel renk üretir.
    """
    import colorsys
    hue = random.random()
    sat = random.uniform(0.3, 0.5)
    val = random.uniform(0.85, 0.95)
    
    r, g, b = colorsys.hsv_to_rgb(hue, sat, val)
    hex_color = '#{:02x}{:02x}{:02x}'.format(int(r*255), int(g*255), int(b*255))
    rgb_color = f'rgb({int(r*255)}, {int(g*255)}, {int(b*255)})'
    
    color_names = ["Pastel Yeşil", "Pastel Pembe", "Pastel Mavi", "Pastel Sarı", "Pastel Turuncu"]
    
    return {
        "success": True,
        "hex": hex_color,
        "rgb": rgb_color,
        "color_name": random.choice(color_names),
        "hsl": f"hsl({int(hue*360)}, {int(sat*100)}%, {int(val*100)}%)"
    }


# ============================================================================
# 14. METIN KASA (Base64 / ROT13)
# ============================================================================

import base64

def encode_text(text: str, method: str = "base64") -> Dict[str, Any]:
    """
    Metni şifreler (Base64 veya Rot13).
    """
    if not text:
        return {"success": False, "error": "Metin girin!"}
    
    if method == "base64":
        try:
            encoded = base64.b64encode(text.encode()).decode()
            return {
                "success": True,
                "original": text,
                "encoded": encoded,
                "method": "Base64",
                "tip": "Copy et, başkasına gönder, o decode etsin."
            }
        except:
            return {"success": False, "error": "Kodlama başarısız!"}
    
    elif method == "rot13":
        import codecs
        encoded = codecs.encode(text, 'rot_13')
        return {
            "success": True,
            "original": text,
            "encoded": encoded,
            "method": "ROT13",
            "tip": "ROT13'ü iki kez uygula = orijinal metin."
        }
    
    return {"success": False, "error": "Bilinmeyen method!"}


# ============================================================================
# 15. GNO HESAPLAYICI (Öğrenci Versiyonu)
# ============================================================================

def calculate_gno(current_gno: float, new_grade: float, weight: float = 0.2) -> Dict[str, Any]:
    """
    Yeni bir dersin GNO'yu nasıl etkileyeceğini hesaplar.
    """
    if not (0 <= current_gno <= 4) or not (0 <= new_grade <= 4):
        return {"success": False, "error": "GNO ve not 0-4 arasında olmalı!"}
    
    new_gno = (current_gno * (1 - weight)) + (new_grade * weight)
    difference = new_gno - current_gno
    
    if difference > 0:
        impact = "YUKARI"
        emoji = "📈"
    elif difference < 0:
        impact = "AŞAĞI"
        emoji = "📉"
    else:
        impact = "SABIT"
        emoji = "➡️"
    
    return {
        "success": True,
        "current_gno": round(current_gno, 2),
        "new_grade": round(new_grade, 2),
        "new_gno": round(new_gno, 2),
        "difference": round(difference, 2),
        "impact": impact,
        "emoji": emoji,
        "message": f"GNO'n {round(abs(difference), 2)} puan {impact.lower()} gidecek."
    }
