# MaxWay Food Delivery Management System

Professional Django-based administration and public portal for food delivery.

## 🚀 Tehnologiyalar
- **Backend:** Django 4.2.3 (Python)
- **Frontend:** HTML5, CSS3, JavaScript (Glassmorphism UI)
- **Ma'lumotlar bazasi:** SQLite (Development) / PostgreSQL (Production ready)
- **Kutubxonalar:** Pillow (Rasmlar), OpenPyXL (Excel Export)

## ✨ Asosiy Imkoniyatlar
1. **RBAC (Rollar tizimi):** Admin (To'liq), Manager (Filial/Mahsulotlar), Cashier (Faqat Buyurtmalar).
2. **Dashboard:** Real-time sotuvlar grafigi va statuslar.
3. **Audit Log:** Barcha o'zgarishlar tarixi (Kim, Qachon, Nima o'zgartirdi).
4. **Excel Export:** Buyurtmalarni filtrlangan holda Excelga yuklash.
5. **Maps Integratsiyasi:** Filiallar uchun Google Maps (Latitude/Longitude) va jonli preview.

## 📂 Loyiha Strukturasi
- `adminapp/`: Asosiy biznes mantiqi, modellar va viewlar.
- `templates/`: Premium dizayndagi HTML andozalar.
- `static/`: CSS, JS va media fayllar.
- `maxway/`: Loyiha sozlamalari (settings, urls).

## 🛠 O'rnatish tartibi
1. Pip paketlarni o'rnating: `pip install -r requirements.txt`
2. Migratsiyalarni amalga oshiring: `python manage.py migrate`
3. Serverni yuklang: `python manage.py runserver`

## 🔑 Admin Kirish
- **URL:** `http://127.0.0.1:8000/login/`
- **Sinov uchun Manager:** username: `manager_test`, parol: `pass1234`
- **Sinov uchun Cashier:** username: `cashier_test`, parol: `pass1234`
# 🍔 MaxWay - Oziq-ovqat Yetkazib Berish Tizimi 🛵

Bu loyiha MaxWay fast-food tarmog'i web-ilovasi bo'lib, o'zida Mijozlarga Buyurtma Qilish sahifasi (Frontend) va Boshqaruv (Admin Dashboard) tizimlarini jamlagan.
Tizim eng zamonaviy funksiyalar bilan jihozlandi: xarita (Yandex Map API), Filiallarni avto qo'shish, to'lov turlari va yetkazib berish (Delivery/Takeaway) funksiyalari.

---

## 🚀 1. Loyihani Ishga Tushirish (Dasturlash muhiti)
Loyihani kompyuteringizda to'liq ishga tushirish uchun quyidagi buyruqlarni Terminal (CMD/PowerShell) da bering:

### 1-Qadam: Muhit (Virtual Environment) va Kutubxonalar o'rnatish
`python -m venv venv`
`.\venv\Scripts\activate`
`pip install -r requirements.txt`

### 2-Qadam: Ma'lumotlar Bazasini tayyorlash (Migrations)
`python manage.py makemigrations`
`python manage.py migrate`

### 3-Qadam: Admin (SuperUser) Yaratish
`python manage.py createsuperuser`
*(O'zingiz uchun yangi Admin akkaunt yaratasiz. Masalan: Login: admin, Parol: 1)*

### 4-Qadam: Serverni Ishga tushirish
`python manage.py runserver 8001`

---

## 🌍 2. Saytga Kirish (Linklar)

**🛒 1. Mijozlar qismi (Katalog va Buyurtmalar):**  
Sayt web-manzili: **[http://127.0.0.1:8001/](http://127.0.0.1:8001/)**
- *Imkoniyatlar:* Mahsulot ko'rish, savatga yig'ish, "Filialdan olib ketish" (Admin paneldan kiritilgan filiallar chiqadi) yoki "Yetkazib berish" (Avto-xarita bilan izlash) orqali kuryer buyurtma qilish.

**🛠️ 2. Boshqaruv Paneli (Django Admin/Dashboard):**  
Sayt web-manzili: **[http://127.0.0.1:8001/admin/](http://127.0.0.1:8001/admin/)**

---

## ⚙️ 3. Tizimni Boshqarish (Admin Qo'llanma)

Boshqaruv paneliga kirganingizdan so'ng 3 ta asosiy bo'limdan foydalanasiz:

### 📍 Filiallar (Branches)
1. "ADD BRANCH" tugmasi orqali yangi filial oching.
2. Formada sizga Maxsus **Yandex Map Xaritasi** ko'rinadi.
3. **Xaritadan** filial joylashgan binoni aniqlasangiz, Kenglik va Uzunlik raqamlari hamda Manzil Matnini **Admin panel o'zi avtomatik** topib to'ldiradi! (Reverse Geocoding). Shunchaki "Saqlash"ni bossangiz -  Mijozlar buyurtma sahifasiga o'zi qo'shiladi!

### 🍔 Kategoriya va Mahsulotlar (Categories & Products)
- Agar maxsulot turi (Misol uchun "Ichimliklar") ochmoqchi bo'lsangiz: **Category** bo'limidan yozasiz.
- Ularning ostiga ovqatlarni (surati, tavsifi va narxi bilan) kiritish **Product** bo'limi orqali amalga oshadi.

### 📦 Buyurtmalar (Orders)
- Mijoz sizga yuborgan buyurtmalar (korzinasi) **Order** modulida aks etadi. Bu yerda xaridorning Yetkazib berish (Qavati, uyi, Izoh xabarlari bilan) to'liq shaklda qabul qilinadi.
