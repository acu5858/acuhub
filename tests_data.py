"""
ACU.HUB | Simulation Admin Panel - Tests Data
10 adet Onedio tarzı test için sorular ve sonuçlar.
"""

TESTS = {
    "dayi-tipi": {
        "id": "dayi-tipi",
        "title": "Ruhun Hangi 'Dayı' Tipi?",
        "description": "İçindeki dayıyı keşfet. Herkesin bir iç dayısı var.",
        "emoji": "👨‍🦳",
        "questions": [
            {
                "text": "Sabah kahvaltıda ne içersin?",
                "options": [
                    {"text": "Çay, demli olacak", "points": {"balikci": 3, "politik": 1}},
                    {"text": "Türk kahvesi, sade", "points": {"kahveci": 3, "muteahhit": 1}},
                    {"text": "Kahvaltı mı? Öğlene kadar uyurum", "points": {"politik": 2, "kahveci": 2}},
                    {"text": "Protein shake", "points": {"muteahhit": 3, "balikci": 1}}
                ]
            },
            {
                "text": "Tatil planın ne?",
                "options": [
                    {"text": "Sahilde balık tutmak", "points": {"balikci": 4}},
                    {"text": "Haber kanalları izlemek", "points": {"politik": 4}},
                    {"text": "Kahvede okey/tavla", "points": {"kahveci": 4}},
                    {"text": "Yeni arsa bakmak", "points": {"muteahhit": 4}}
                ]
            },
            {
                "text": "En çok hangi konuda fikir belirtirsin?",
                "options": [
                    {"text": "Hava durumu ve mevsimler", "points": {"balikci": 3, "kahveci": 1}},
                    {"text": "Ekonomi ve siyaset", "points": {"politik": 4}},
                    {"text": "Mahalle dedikodları", "points": {"kahveci": 3, "politik": 1}},
                    {"text": "Yatırım fırsatları", "points": {"muteahhit": 4}}
                ]
            },
            {
                "text": "Cep telefonunu ne için kullanırsın?",
                "options": [
                    {"text": "Sadece arama", "points": {"balikci": 3, "kahveci": 1}},
                    {"text": "Twitter ve haber siteleri", "points": {"politik": 4}},
                    {"text": "WhatsApp grupları", "points": {"kahveci": 3, "politik": 1}},
                    {"text": "Sahibinden ve emlak siteleri", "points": {"muteahhit": 4}}
                ]
            },
            {
                "text": "Hayat motton ne?",
                "options": [
                    {"text": "Sabır her şeyin başı", "points": {"balikci": 4}},
                    {"text": "Bu millet uyanmalı", "points": {"politik": 4}},
                    {"text": "Otur, çay iç, geçer", "points": {"kahveci": 4}},
                    {"text": "Para kazanmayan uyusun", "points": {"muteahhit": 4}}
                ]
            }
        ],
        "results": {
            "balikci": {
                "title": "Balıkçı Dayı 🎣",
                "description": "Sabırlısın, doğayla barışıksın. Sabah 4'te kalkıp oltanı atarsın. Teknolojiden uzak, huzura yakınsın.",
                "traits": ["Sabırlı", "Doğa sever", "Erken kalkar", "Felsefik"]
            },
            "politik": {
                "title": "Politik Dayı 📺",
                "description": "Her konuda bir fikrin var. Haberleri kaçırmazsın. Sofra sohbetlerinin vazgeçilmezi ekonomi ve siyaset.",
                "traits": ["Bilgili", "Tartışmacı", "Gündem takipçisi", "Karamsar"]
            },
            "kahveci": {
                "title": "Kahveci Dayı ☕",
                "description": "Sosyal çevren geniş. Herkesin derdini bilirsin. Okey/tavla olmadan gün geçmez.",
                "traits": ["Sosyal", "Dedikodu meraklısı", "Rahat", "Misafirperver"]
            },
            "muteahhit": {
                "title": "Zengin Müteahhit Dayı 🏗️",
                "description": "Para konuşur. Her yerde bir fırsat görürsün. 'Buraya 5 katlı dikerim' dersin sürekli.",
                "traits": ["Hırslı", "Pratik", "Zengin", "Materialist"]
            }
        }
    },
    
    "toplu-tasima": {
        "id": "toplu-tasima",
        "title": "Hangi İstanbul Toplu Taşıma Aracısın?",
        "description": "Karakterin hangi ulaşım aracıyla örtüşüyor?",
        "emoji": "🚇",
        "questions": [
            {
                "text": "Sabahları nasıl uyanırsın?",
                "options": [
                    {"text": "Alarm çalar, hemen fırlarsın", "points": {"metrobus": 3, "marmaray": 1}},
                    {"text": "Yavaş yavaş, acele yok", "points": {"tramvay": 4}},
                    {"text": "Geç kalırsın genelde", "points": {"marmaray": 3, "metrobus": 1}},
                    {"text": "Uyanmak mı? Gece çalışırım", "points": {"vapur": 4}}
                ]
            },
            {
                "text": "Stresle nasıl başa çıkarsın?",
                "options": [
                    {"text": "Daha hızlı çalışırım", "points": {"metrobus": 4}},
                    {"text": "Sakin kalır, beklerim", "points": {"tramvay": 3, "vapur": 1}},
                    {"text": "Çökerim ara ara", "points": {"marmaray": 4}},
                    {"text": "Denizi seyrederim", "points": {"vapur": 4}}
                ]
            },
            {
                "text": "İnsanlarla ilişkin nasıl?",
                "options": [
                    {"text": "Kalabalık severim", "points": {"metrobus": 4}},
                    {"text": "Az ama öz arkadaş", "points": {"tramvay": 3, "vapur": 1}},
                    {"text": "Bazen ghost olurum", "points": {"marmaray": 4}},
                    {"text": "Romantik buluşmalar", "points": {"vapur": 4}}
                ]
            },
            {
                "text": "Tempo tercihin?",
                "options": [
                    {"text": "Hızlı ve yoğun", "points": {"metrobus": 4}},
                    {"text": "Sabit ve güvenilir", "points": {"tramvay": 4}},
                    {"text": "Değişken, bazen durur", "points": {"marmaray": 4}},
                    {"text": "Yavaş ve keyifli", "points": {"vapur": 4}}
                ]
            },
            {
                "text": "Hayatta en çok ne değer?",
                "options": [
                    {"text": "Verimlilik", "points": {"metrobus": 4}},
                    {"text": "Gelenek", "points": {"tramvay": 4}},
                    {"text": "Teknoloji", "points": {"marmaray": 4}},
                    {"text": "Huzur", "points": {"vapur": 4}}
                ]
            }
        ],
        "results": {
            "metrobus": {
                "title": "Agresif Metrobüs 🚌",
                "description": "Hızlı, yoğun, kaotik. Her gün bir savaş alanı ama durmak yok. Kalabalıkta bile yol bulursun.",
                "traits": ["Hızlı", "Dayanıklı", "Kalabalık sever", "Stresli"]
            },
            "tramvay": {
                "title": "Nostaljik Tramvay 🚋",
                "description": "Klasik, güvenilir, romantik. Yavaş ama emin adımlarla ilerlersin. Geleneklere bağlısın.",
                "traits": ["Nostaljik", "Güvenilir", "Yavaş", "Romantik"]
            },
            "marmaray": {
                "title": "Bozuk Marmaray 🚇",
                "description": "Potansiyelin yüksek ama bazen çökersin. Teknik aksaklıklar yaşarsın. Ama çalışınca efsane.",
                "traits": ["Potansiyelli", "Sorunlu", "Modern", "Güvenilmez"]
            },
            "vapur": {
                "title": "Romantik Vapur ⛴️",
                "description": "Yavaş ama keyifli. Strese tahammülün yok. Denizi, martıları seversin. Şehrin kaosu sana göre değil.",
                "traits": ["Huzurlu", "Romantik", "Yavaş", "Doğa sever"]
            }
        }
    },
    
    "mental-cokus": {
        "id": "mental-cokus",
        "title": "Mental Çöküşe Ne Kadar Kaldı?",
        "description": "Psikolojik dayanıklılık testi. Sonuçlar sadece eğlence amaçlıdır.",
        "emoji": "🧠",
        "questions": [
            {
                "text": "Son 1 haftada kaç saat uyudun (günlük ortalama)?",
                "options": [
                    {"text": "7-8 saat, kraliçe gibi", "points": {"tas": 4}},
                    {"text": "5-6 saat, idare eder", "points": {"yakinda": 2, "tas": 2}},
                    {"text": "3-4 saat, kahveyle ayaktayım", "points": {"yakinda": 4}},
                    {"text": "Uyku mu o da ne?", "points": {"zaten": 4}}
                ]
            },
            {
                "text": "Telefonundaki okunmamış mesaj sayısı?",
                "options": [
                    {"text": "0, hepsine cevap veririm", "points": {"tas": 4}},
                    {"text": "5-10 arası", "points": {"yakinda": 2, "tas": 2}},
                    {"text": "50+, bakmaya korkuyorum", "points": {"yakinda": 4}},
                    {"text": "Bildirimleri kapattım", "points": {"zaten": 4}}
                ]
            },
            {
                "text": "Son ne zaman hobi yaptın?",
                "options": [
                    {"text": "Bu hafta", "points": {"tas": 4}},
                    {"text": "Bu ay içinde", "points": {"yakinda": 2, "tas": 2}},
                    {"text": "Hatırlamıyorum", "points": {"yakinda": 4}},
                    {"text": "Hobi mi? Lüks.", "points": {"zaten": 4}}
                ]
            },
            {
                "text": "Kahve/çay günlük tüketimin?",
                "options": [
                    {"text": "1-2 fincan", "points": {"tas": 4}},
                    {"text": "3-4 fincan", "points": {"yakinda": 2, "tas": 2}},
                    {"text": "5+ fincan", "points": {"yakinda": 4}},
                    {"text": "Damardan alıyorum artık", "points": {"zaten": 4}}
                ]
            },
            {
                "text": "Geleceği düşününce ne hissedersin?",
                "options": [
                    {"text": "Heyecan ve umut", "points": {"tas": 4}},
                    {"text": "Biraz endişe ama idare eder", "points": {"yakinda": 2, "tas": 2}},
                    {"text": "Panik atak geliyor", "points": {"yakinda": 4}},
                    {"text": "Gelecek mi? Bugünü atlatmaya çalışıyorum.", "points": {"zaten": 4}}
                ]
            }
        ],
        "results": {
            "zaten": {
                "title": "Zaten Çökmüşsün 💀",
                "description": "Kardeşim sen hallice durumdasın. Acil tatil lazım. Veya terapi. Veya ikisi birden.",
                "traits": ["Yorgun", "Tükenmiş", "Kahve bağımlısı", "Zombi mod"]
            },
            "yakinda": {
                "title": "3 Vakte Kadar ⏰",
                "description": "Şu an ayaktasın ama çatlaklar var. Kendine biraz zaman ayır yoksa yakında crash.",
                "traits": ["Stresli", "Dengelemeye çalışan", "Kahve sever", "Uykusuz"]
            },
            "tas": {
                "title": "Taş Gibisin 💪",
                "description": "Mental sağlık mı? Sende var! Ya çok şanslısın ya da çok iyi yönetiyorsun. Paylaş bize de.",
                "traits": ["Dengeli", "Sağlıklı", "Organize", "Şanslı"]
            }
        }
    },
    
    "yazilim-hatasi": {
        "id": "yazilim-hatasi",
        "title": "Hangi Yazılım Hatasısın?",
        "description": "Bug mu, feature mı belli değil. Sen hangi hatasın?",
        "emoji": "🐛",
        "questions": [
            {
                "text": "Bir projede çalışırken...",
                "options": [
                    {"text": "Başlayamıyorum bile, nereden başlasam?", "points": {"404": 4}},
                    {"text": "Başlarım ama bitiremem, döngüye girerim", "points": {"loop": 4}},
                    {"text": "Küçük hatalarla takılırım", "points": {"syntax": 4}},
                    {"text": "Her şey patlıyor birden", "points": {"bsod": 4}}
                ]
            },
            {
                "text": "Sosyal ortamlarda...",
                "options": [
                    {"text": "Kayboluyorum, bulamıyorlar", "points": {"404": 4}},
                    {"text": "Aynı hikayeleri anlatıyorum", "points": {"loop": 4}},
                    {"text": "Yanlış şeyler söylüyorum sürekli", "points": {"syntax": 4}},
                    {"text": "Aniden donuyorum", "points": {"bsod": 4}}
                ]
            },
            {
                "text": "Planların genelde...",
                "options": [
                    {"text": "Hiç olmaz, bulunamaz", "points": {"404": 4}},
                    {"text": "Sürekli değişir, aynı yerde dönerim", "points": {"loop": 4}},
                    {"text": "Küçük detaylarda aksar", "points": {"syntax": 4}},
                    {"text": "Tamamen çöker", "points": {"bsod": 4}}
                ]
            },
            {
                "text": "Stres altında...",
                "options": [
                    {"text": "Ortadan kayboluyorum", "points": {"404": 4}},
                    {"text": "Aynı şeyleri tekrarlıyorum", "points": {"loop": 4}},
                    {"text": "Basit hatalar yapıyorum", "points": {"syntax": 4}},
                    {"text": "Tamamen kitleniyorum", "points": {"bsod": 4}}
                ]
            },
            {
                "text": "İnsanlar seni nasıl tanımlar?",
                "options": [
                    {"text": "Gizemli, nerede olduğu belirsiz", "points": {"404": 4}},
                    {"text": "Tutarlı ama tekrarcı", "points": {"loop": 4}},
                    {"text": "Zeki ama dalgın", "points": {"syntax": 4}},
                    {"text": "Bazen harika, bazen felaket", "points": {"bsod": 4}}
                ]
            }
        ],
        "results": {
            "404": {
                "title": "404 Not Found 🔍",
                "description": "Seni arıyorlar ama bulamıyorlar. Gizemlisin, belirsizsin. Bazen kayıplara karışırsın.",
                "traits": ["Gizemli", "Bulunamaz", "Introvert", "Ghost"]
            },
            "loop": {
                "title": "Infinite Loop ♾️",
                "description": "Döngüden çıkamıyorsun. Aynı hataları, aynı hikayeleri, aynı alışkanlıkları tekrarlıyorsun.",
                "traits": ["Tutarlı", "Tekrarcı", "Kararlı", "Takıntılı"]
            },
            "syntax": {
                "title": "Syntax Error ⚠️",
                "description": "Küçük detaylarda takılıyorsun. Potansiyelin var ama ufak hatalar seni engelliyor.",
                "traits": ["Detaycı", "Dalgın", "Akıllı", "Hata yapan"]
            },
            "bsod": {
                "title": "Blue Screen of Death 💀",
                "description": "Her şey güzel giderken birden crash. Dramatik, beklenmedik, yıkıcı.",
                "traits": ["Dramatik", "Beklenmedik", "Şok edici", "Yıkıcı"]
            }
        }
    },
    
    "sosyal-pil": {
        "id": "sosyal-pil",
        "title": "Sosyal Pilin Kaç mAh?",
        "description": "Sosyal enerjin ne kadar dayanıyor?",
        "emoji": "🔋",
        "questions": [
            {
                "text": "Parti davetine tepkin?",
                "options": [
                    {"text": "EVEEET! Nereye gidiyoruz?", "points": {"nokia": 4}},
                    {"text": "Tamam ama erken giderim", "points": {"samsung": 3, "nokia": 1}},
                    {"text": "Hmm, düşüneyim...", "points": {"iphone": 3, "samsung": 1}},
                    {"text": "Bahane uydurup kaçarım", "points": {"iphone": 4}}
                ]
            },
            {
                "text": "Bir arkadaş grubuyla tatile gideceksin, ideal süre?",
                "options": [
                    {"text": "Hafta sonu yeterli", "points": {"iphone": 4}},
                    {"text": "3-4 gün ideal", "points": {"samsung": 4}},
                    {"text": "1 hafta olsun", "points": {"nokia": 3, "samsung": 1}},
                    {"text": "Ne kadar uzun o kadar iyi!", "points": {"nokia": 4}}
                ]
            },
            {
                "text": "Video görüşme mi yoksa mesaj mı?",
                "options": [
                    {"text": "Video, yüz yüze gibisi yok", "points": {"nokia": 4}},
                    {"text": "Telefon görüşmesi yeterli", "points": {"samsung": 4}},
                    {"text": "Mesaj atarım", "points": {"iphone": 3, "samsung": 1}},
                    {"text": "Emoji bile yoruyor", "points": {"iphone": 4}}
                ]
            },
            {
                "text": "Sosyalleştikten sonra...",
                "options": [
                    {"text": "Daha da enerji dolu olurum", "points": {"nokia": 4}},
                    {"text": "İyi hissederim ama yorulmuşumdur", "points": {"samsung": 4}},
                    {"text": "Şarj olmam lazım", "points": {"iphone": 4}},
                    {"text": "3 gün inzivaya çekilirim", "points": {"iphone": 4}}
                ]
            },
            {
                "text": "İdeal hafta sonu planın?",
                "options": [
                    {"text": "Arkadaşlarla dolu dolu", "points": {"nokia": 4}},
                    {"text": "Bir aktivite + dinlenme", "points": {"samsung": 4}},
                    {"text": "Evde Netflix", "points": {"iphone": 4}},
                    {"text": "Kimseyi görmeden geçmek", "points": {"iphone": 4}}
                ]
            }
        ],
        "results": {
            "nokia": {
                "title": "Nokia 3310 📱",
                "description": "Pil bitmiyor! Sosyal enerjin sınırsız. Herkesle konuşur, her yere gidersin. Extrovert of extroverts.",
                "traits": ["Sosyal", "Enerjik", "Dayanıklı", "Extrovert"]
            },
            "samsung": {
                "title": "Orta Segment Samsung 📲",
                "description": "Dengeli bir pil. Sosyal de olursun, yalnız da kalabilirsin. Ambivert moddasın.",
                "traits": ["Dengeli", "Esnek", "Adaptif", "Ambivert"]
            },
            "iphone": {
                "title": "iPhone 5 (Eski Model) 🪫",
                "description": "Günde 3 kez şarj lazım! Sosyalleşmek yoruyor. Küçük dozlarda insan. Introvert gang.",
                "traits": ["İçe dönük", "Yorgun", "Seçici", "İntrovert"]
            }
        }
    },
    
    "turk-dizisi": {
        "id": "turk-dizisi",
        "title": "Hangi Türk Dizisi Karakterisin?",
        "description": "Dizilerdeki arketiplerden hangisisin?",
        "emoji": "📺",
        "questions": [
            {
                "text": "Bir ihanet öğrendin, tepkin?",
                "options": [
                    {"text": "Plan yaparım, intikam!", "points": {"kotu": 4}},
                    {"text": "Patrona söylerim", "points": {"yanci": 4}},
                    {"text": "Ağlarım ama af ederim", "points": {"masum": 4}},
                    {"text": "Arkamı döner giderim", "points": {"gizemli": 4}}
                ]
            },
            {
                "text": "Düğün sahnelerinde sen...",
                "options": [
                    {"text": "Düğünü basarım", "points": {"kotu": 4}},
                    {"text": "Dedikodu yaparım", "points": {"yanci": 4}},
                    {"text": "Gelinliğime odaklanırım", "points": {"masum": 4}},
                    {"text": "Gelmem bile", "points": {"gizemli": 4}}
                ]
            },
            {
                "text": "Patron seni azarladı...",
                "options": [
                    {"text": "Şirketini ele geçiririm", "points": {"kotu": 4}},
                    {"text": "'Haklısınız' derim", "points": {"yanci": 4}},
                    {"text": "Ağlayarak tuvalete giderim", "points": {"masum": 4}},
                    {"text": "İstifa edip Karadeniz'e yerleşirim", "points": {"gizemli": 4}}
                ]
            },
            {
                "text": "Aşk üçgeninde rolün?",
                "options": [
                    {"text": "Ayıran", "points": {"kotu": 4}},
                    {"text": "Ayıranlara yardım eden", "points": {"yanci": 4}},
                    {"text": "Ayrılan", "points": {"masum": 4}},
                    {"text": "Uzaktan izleyen", "points": {"gizemli": 4}}
                ]
            },
            {
                "text": "Final bölümünde sen...",
                "options": [
                    {"text": "Hapse girerim", "points": {"kotu": 4}},
                    {"text": "Affedilirim", "points": {"yanci": 4}},
                    {"text": "Mutlu evliliğim olur", "points": {"masum": 4}},
                    {"text": "Nereye gittiğim belirsiz", "points": {"gizemli": 4}}
                ]
            }
        ],
        "results": {
            "kotu": {
                "title": "Kaotik Kötü 😈",
                "description": "Planlar, entrikalar, intikamlar. Sen olmadan dizi yürümez. Villain energy max.",
                "traits": ["Hesapçı", "Karizmatik", "Acımasız", "Planlı"]
            },
            "yanci": {
                "title": "Sinsi Yancı 🐍",
                "description": "Her patronun yanında bir sen varsın. Dedikodu, muhbirlik, fırsatçılık. İkinci adam sendromu.",
                "traits": ["Fırsatçı", "Sinsi", "Sadık(?)", "Survivalist"]
            },
            "masum": {
                "title": "Masum Köylü 🌾",
                "description": "Herkes seni kullanıyor ama sen hala iyi niyetlisin. Ağlama sahnelerin efsane. Pure soul.",
                "traits": ["Masum", "İyi niyetli", "Duygusal", "Kurban"]
            },
            "gizemli": {
                "title": "Gizemli Yabancı 🎭",
                "description": "Nereden geldin, nereye gideceksin belli değil. Ana karakterleri etkilersin ama merkeze geçmezsin.",
                "traits": ["Gizemli", "Bağımsız", "Cool", "Öngörülemez"]
            }
        }
    },
    
    "gercekci-meslek": {
        "id": "gercekci-meslek",
        "title": "Gelecekteki Gerçekçi Mesleğin?",
        "description": "Hayaller değil, Türkiye gerçekleri. Sen ne olacaksın?",
        "emoji": "💼",
        "questions": [
            {
                "text": "Şu anki hayalin?",
                "options": [
                    {"text": "Pasif gelir ve erken emeklilik", "points": {"kripto": 4}},
                    {"text": "Viral olmak", "points": {"youtuber": 4}},
                    {"text": "Stabil bir maaş", "points": {"beyazyaka": 4}},
                    {"text": "Doğaya dönmek", "points": {"koy": 4}}
                ]
            },
            {
                "text": "Para yönetimin nasıl?",
                "options": [
                    {"text": "YOLO, hepsini yatırıma", "points": {"kripto": 4}},
                    {"text": "Sponsorlar halleder", "points": {"youtuber": 4}},
                    {"text": "Bütçe yapıyorum", "points": {"beyazyaka": 4}},
                    {"text": "Para mı? Takas yaparız", "points": {"koy": 4}}
                ]
            },
            {
                "text": "İş stresiyle nasıl başa çıkarsın?",
                "options": [
                    {"text": "Grafiklere bakarım", "points": {"kripto": 4}},
                    {"text": "Vlog çekerim", "points": {"youtuber": 4}},
                    {"text": "Kahve molası", "points": {"beyazyaka": 4}},
                    {"text": "Bahçeyle uğraşırım", "points": {"koy": 4}}
                ]
            },
            {
                "text": "10 yıl sonra nerede görüyorsun kendini?",
                "options": [
                    {"text": "Ya zengin ya metelik", "points": {"kripto": 4}},
                    {"text": "1M subscriber", "points": {"youtuber": 4}},
                    {"text": "Terfi almış, evlenmiş", "points": {"beyazyaka": 4}},
                    {"text": "Köyde kendi sebzemi yetiştiriyor", "points": {"koy": 4}}
                ]
            },
            {
                "text": "Toplumsal statü senin için...",
                "options": [
                    {"text": "Lambo ile kanıtlanır", "points": {"kripto": 4}},
                    {"text": "Takipçi sayısı belirler", "points": {"youtuber": 4}},
                    {"text": "Pozisyon ve maaş önemli", "points": {"beyazyaka": 4}},
                    {"text": "Hiç önemli değil", "points": {"koy": 4}}
                ]
            }
        ],
        "results": {
            "kripto": {
                "title": "Kripto Batığı 📉",
                "description": "To the moon diyordun, yere çakıldın. Ama 'buy the dip' mantrasını bırakmıyorsun.",
                "traits": ["Riskçi", "Hayalperest", "YOLO", "Kayıp"]
            },
            "youtuber": {
                "title": "YouTuber/İnfluencer 📱",
                "description": "Her anı içerik. 'Abone olmayı unutma' ağzından düşmüyor. Sponsorlar inşallah.",
                "traits": ["Kreatif", "Sosyal", "Trend takipçisi", "Egoist"]
            },
            "beyazyaka": {
                "title": "Beyaz Yaka Kölesi 👔",
                "description": "9-6 çalış, toplantıya gir, email at. Maaşın yeter de artmaz. Stabilite mi esaret mi?",
                "traits": ["Stabil", "Güvenilir", "Sıkıcı", "Sistematik"]
            },
            "koy": {
                "title": "Köyüne Dönen Mühendis 🌿",
                "description": "Corporate hayattan kaçtın. Şimdi domates yetiştiriyorsun. Aslında en akıllısı sensin.",
                "traits": ["Huzurlu", "Özgür", "Minimalist", "Kaçkın"]
            }
        }
    },
    
    "sokak-lezzeti": {
        "id": "sokak-lezzeti",
        "title": "Hangi Sokak Lezzetisin?",
        "description": "Kişiliğin hangi sokak yemeğiyle eşleşiyor?",
        "emoji": "🥙",
        "questions": [
            {
                "text": "Risk almayı sever misin?",
                "options": [
                    {"text": "Risk benim göbek adım", "points": {"midye": 4}},
                    {"text": "Hesaplı risk alırım", "points": {"islak": 3, "midye": 1}},
                    {"text": "Güvenli olanı tercih ederim", "points": {"halka": 4}},
                    {"text": "Hiç risk almam", "points": {"simit": 4}}
                ]
            },
            {
                "text": "Gece hayatın nasıl?",
                "options": [
                    {"text": "Sabaha kadar sokaktayım", "points": {"midye": 4}},
                    {"text": "Taksim Meydanı'ndayım gece 2'de", "points": {"islak": 4}},
                    {"text": "Sahil kenarında gezerim", "points": {"halka": 4}},
                    {"text": "Erken yatarım", "points": {"simit": 4}}
                ]
            },
            {
                "text": "Bütçen genelde...",
                "options": [
                    {"text": "Hesapsız harcarım", "points": {"midye": 4}},
                    {"text": "Geceleri savurganım", "points": {"islak": 4}},
                    {"text": "Ekonomik takılırım", "points": {"halka": 4}},
                    {"text": "Minimum harcama", "points": {"simit": 4}}
                ]
            },
            {
                "text": "Arkadaş ortamında sen...",
                "options": [
                    {"text": "Tehlikeli önerileri yapan", "points": {"midye": 4}},
                    {"text": "Gece 3'te yemek turu organize eden", "points": {"islak": 4}},
                    {"text": "Sahil yürüyüşü önerenin", "points": {"halka": 4}},
                    {"text": "Erken giden", "points": {"simit": 4}}
                ]
            },
            {
                "text": "Hayat motton?",
                "options": [
                    {"text": "YOLO!", "points": {"midye": 4}},
                    {"text": "Gece gündüz yaşa", "points": {"islak": 4}},
                    {"text": "Basit ama güzel", "points": {"halka": 4}},
                    {"text": "Sağlık her şeyden önemli", "points": {"simit": 4}}
                ]
            }
        ],
        "results": {
            "midye": {
                "title": "Riskli Midye 🦪",
                "description": "Tehlike senin göbek adın. Kuralları çiğner, sınırları test edersin. Ya efsane ya felaket.",
                "traits": ["Riskçi", "Cesaretli", "Tehlikeli", "YOLO"]
            },
            "islak": {
                "title": "Islak Hamburger 🍔",
                "description": "Gece kuşusun. Taksim'de sabah 4'te, elinde ıslak hamburger. Kaotik ama eğlenceli.",
                "traits": ["Gece kuşu", "Sosyal", "Kaotik", "Eğlenceli"]
            },
            "halka": {
                "title": "Ekonomik Halka Tatlısı 🍩",
                "description": "Tatlı, ekonomik, sahil kenarı. Bütçe dostu mutluluğu bilirsin. Huzur arayanlar.",
                "traits": ["Ekonomik", "Tatlı", "Huzurlu", "Basit"]
            },
            "simit": {
                "title": "Klasik Simit 🥯",
                "description": "Güvenilir, sade, her zaman orada. Risk almaz, sabahları erken kalkar, çay içersin.",
                "traits": ["Güvenilir", "Sade", "Geleneksel", "Sağlıklı"]
            }
        }
    },
    
    "sabir-seviyesi": {
        "id": "sabir-seviyesi",
        "title": "Sabır Seviyen Nedir?",
        "description": "Ne kadar dayanabilirsin?",
        "emoji": "🧘",
        "questions": [
            {
                "text": "Trafik sıkışık, tepkin?",
                "options": [
                    {"text": "Müzik açar beklerim", "points": {"celik": 4}},
                    {"text": "Biraz sinirlenrim ama idare ederim", "points": {"pamuk": 2, "celik": 2}},
                    {"text": "Korna çalmaya başlarım", "points": {"pamuk": 4}},
                    {"text": "Arabayı bırakıp yürürüm", "points": {"yok": 4}}
                ]
            },
            {
                "text": "İnternet yavaş...",
                "options": [
                    {"text": "Beklerim, acele ne", "points": {"celik": 4}},
                    {"text": "Birkaç kez deneyip beklerim", "points": {"pamuk": 2, "celik": 2}},
                    {"text": "Router'ı resetlerim sinirle", "points": {"pamuk": 4}},
                    {"text": "Laptop'u fırlatırım", "points": {"yok": 4}}
                ]
            },
            {
                "text": "Biri seni yarım saat bekletiyor...",
                "options": [
                    {"text": "Sorun değil, beklerim", "points": {"celik": 4}},
                    {"text": "Mesaj atarım, 'neredesin?'", "points": {"pamuk": 2, "celik": 2}},
                    {"text": "10 dk daha bekleyip giderim", "points": {"pamuk": 4}},
                    {"text": "5 dk sonra patlarım", "points": {"yok": 4}}
                ]
            },
            {
                "text": "Uzun bir kuyrukta...",
                "options": [
                    {"text": "Telefona bakar beklerim", "points": {"celik": 4}},
                    {"text": "Sabrederim ama sıkılırım", "points": {"pamuk": 2, "celik": 2}},
                    {"text": "'Bu kadar da olmaz' diye söylenirim", "points": {"pamuk": 4}},
                    {"text": "Kuyruktan çıkarım", "points": {"yok": 4}}
                ]
            },
            {
                "text": "Bir öğrenmek için...",
                "options": [
                    {"text": "Aylarca çalışabilirim", "points": {"celik": 4}},
                    {"text": "Birkaç hafta deneyebilirim", "points": {"pamuk": 2, "celik": 2}},
                    {"text": "Çabuk sonuç istiyorum", "points": {"pamuk": 4}},
                    {"text": "Hemen olmazsa bırakırım", "points": {"yok": 4}}
                ]
            }
        ],
        "results": {
            "celik": {
                "title": "Çelik Halat 🔗",
                "description": "Seni kırmak imkansız. Sabrın sonsuz, dayanıklılığın efsane. Budist keşişler bile kıskansın.",
                "traits": ["Sabırlı", "Dayanıklı", "Sakin", "Zen"]
            },
            "pamuk": {
                "title": "Pamuk İpliği 🧵",
                "description": "Var ama ince. Biraz zorlarsan kopar. Ortalama sabır, idare eder seviye.",
                "traits": ["Orta", "Kırılgan", "Normal", "İnsan"]
            },
            "yok": {
                "title": "Sabır Yok Hükmünde 💥",
                "description": "0 tolerans. Sabır sende bir dakika bile yok. Her şey HEMEN olmalı. Burnundan soluyorsun.",
                "traits": ["Sabırsız", "Sinirli", "Hızlı", "Patlayıcı"]
            }
        }
    },
    
    "simulasyon-rol": {
        "id": "simulasyon-rol",
        "title": "Simülasyondaki Rolün Ne?",
        "description": "Matrix'teysen, sen hangi karaktersin?",
        "emoji": "🎮",
        "questions": [
            {
                "text": "Hayatta büyük kararlar verirken...",
                "options": [
                    {"text": "Akışa bırakırım", "points": {"npc": 4}},
                    {"text": "Her şeyi planlı yaparım", "points": {"ana": 4}},
                    {"text": "Beklenmedik hareket ederim", "points": {"bug": 4}},
                    {"text": "Kuralları ben koyarım", "points": {"admin": 4}}
                ]
            },
            {
                "text": "İnsanlar seni nasıl tanımlar?",
                "options": [
                    {"text": "Sıradan, sessiz", "points": {"npc": 4}},
                    {"text": "İlgi çekici, özel", "points": {"ana": 4}},
                    {"text": "Garip, beklenmedik", "points": {"bug": 4}},
                    {"text": "Lider, kontrollü", "points": {"admin": 4}}
                ]
            },
            {
                "text": "Bir sorunla karşılaştığında...",
                "options": [
                    {"text": "Başkası çözer diye beklerim", "points": {"npc": 4}},
                    {"text": "Ben çözerim", "points": {"ana": 4}},
                    {"text": "Sorunu daha da karıştırırım", "points": {"bug": 4}},
                    {"text": "Sistem seviyesinde müdahale ederim", "points": {"admin": 4}}
                ]
            },
            {
                "text": "Hayattaki amacın?",
                "options": [
                    {"text": "Günü geçirmek", "points": {"npc": 4}},
                    {"text": "İz bırakmak", "points": {"ana": 4}},
                    {"text": "Kaos yaratmak", "points": {"bug": 4}},
                    {"text": "Sistemi yönetmek", "points": {"admin": 4}}
                ]
            },
            {
                "text": "Eğer bu bir oyun olsaydı, sen...",
                "options": [
                    {"text": "Arka plandaki karakter", "points": {"npc": 4}},
                    {"text": "Ana hikayenin kahramanı", "points": {"ana": 4}},
                    {"text": "Oyundaki bug", "points": {"bug": 4}},
                    {"text": "Oyunu tasarlayan", "points": {"admin": 4}}
                ]
            }
        ],
        "results": {
            "npc": {
                "title": "NPC (Non-Player Character) 🚶",
                "description": "Arka planda sessizce yaşıyorsun. Ana karakterlerin hikayesinde yan rolsün. Sakin ve sade hayat.",
                "traits": ["Sade", "Sessiz", "Rutin", "Arkada"]
            },
            "ana": {
                "title": "Ana Karakter 🦸",
                "description": "Hikaye senin etrafında dönüyor. Önemli olaylar sana oluyor. Protagonist energy.",
                "traits": ["Özel", "Önemli", "Merkez", "Kahraman"]
            },
            "bug": {
                "title": "Bug 🐛",
                "description": "Sistem seni anlamıyor. Beklenmedik hareketlerinle herkesi şaşırtıyorsun. Glitch in the matrix.",
                "traits": ["Beklenmedik", "Kaotik", "Garip", "Öngörülemez"]
            },
            "admin": {
                "title": "Admin 👑",
                "description": "Sen kuralları koyarsın. Sistem senin elinde. Matrix'in mimarı. God mode activated.",
                "traits": ["Güçlü", "Kontrollü", "Lider", "Tanrısal"]
            }
        }
    }
}

def get_test_by_id(test_id: str) -> dict:
    """Test ID'sine göre test verisini döndürür."""
    return TESTS.get(test_id)

def get_all_tests() -> list:
    """Tüm testlerin özet listesini döndürür."""
    return [
        {
            "id": test["id"],
            "title": test["title"],
            "description": test["description"],
            "emoji": test["emoji"],
            "question_count": len(test["questions"])
        }
        for test in TESTS.values()
    ]

def calculate_test_result(test_id: str, answers: list) -> dict:
    """
    Verilen cevaplara göre test sonucunu hesaplar.
    
    Args:
        test_id: Test ID'si
        answers: Her soru için seçilen option index'leri listesi
        
    Returns:
        Sonuç dict'i
    """
    test = TESTS.get(test_id)
    if not test:
        return {"success": False, "error": "Test bulunamadı!"}
    
    points = {}
    
    for i, answer_idx in enumerate(answers):
        if i < len(test["questions"]):
            question = test["questions"][i]
            if 0 <= answer_idx < len(question["options"]):
                option = question["options"][answer_idx]
                for result_key, point_value in option.get("points", {}).items():
                    points[result_key] = points.get(result_key, 0) + point_value
    
    if not points:
        return {"success": False, "error": "Cevap bulunamadı!"}
    
    winner = max(points, key=points.get)
    result_data = test["results"].get(winner, {})
    
    return {
        "success": True,
        "test_id": test_id,
        "test_title": test["title"],
        "result_key": winner,
        "result": result_data,
        "all_points": points
    }
