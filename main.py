# MID_TERM
# Kontaktlar kitobchasi


def tilni_tanlash():
    global joriy_til
    print("\n" + "="*30)
    print("🌐  Tilni tanlang / Выберите язык / Select language:")
    print("1. O'zbekcha")
    print("2. Русский")
    print("3. English")
    tanlov = input("   ➤  Tanlang : ")
    joriy_til = {"1": "uz", "2": "ru", "3": "en"}.get(tanlov, "uz")
    if tanlov not in ["1", "2", "3"]:
        print("   ⚠️  Noto'g'ri tanlov! Default til sifatida O'zbekcha bo'lib qoladi !")

def bosh_menu():
    print("\n" + "="*30)
    print(t("Menyu:") + "\n")
    print("1. 📝  " + t("Yangi kontakt qo'shish"))
    print("2. ✏️  " + t("Kontaktni yangilash"))
    print("3. 🗑  " + t("Kontaktni o'chirish"))
    print("4. 🔍  " + t("Kontaktni qidirish"))
    print("5. 🗃  " + t("Barcha kontaktlarni ko'rsatish"))
    print("6. ❌  " + t("Chiqish"))
    print("="*30)

kontaktlar = []

tillar = {
    "uz": {
        "Menyu:": "🌐 Menyu:",
        "Yangi kontakt qo'shish": "Yangi kontakt qo'shish",
        "Kontaktni yangilash": "Kontaktni yangilash",
        "Kontaktni o'chirish": "Kontaktni o'chirish",
        "Kontaktni qidirish": "Kontaktni qidirish",
        "Barcha kontaktlarni ko'rsatish": "Barcha kontaktlarni ko'rsatish",
        "Chiqish": "Chiqish",
        "Ism yoki telefon raqami": "Ism yoki telefon raqami",
        "Ism": "Ism",
        "Telefon raqami": "Telefon raqami",
        "Email manzili": "Email manzili",
        "Manzil": "Manzil",
        "Kontakt qo'shildi": "Kontakt qo'shildi",
        "Kontakt topilmadi": "Kontakt topilmadi",
        "Kontakt o'chirildi": "Kontakt o'chirildi",
        "Kontakt yangilandi": "Kontakt yangilandi",
        "Kontaktlar ro'yxati bo'sh": "Kontaktlar ro'yxati bo'sh",
        "Tanlang": "Tanlang",
        "Noto'g'ri tanlov!": "Noto'g'ri tanlov!",
    },
    "ru": {
        "Menyu:": "🌐 Меню:",
        "Yangi kontakt qo'shish": "Добавить новый контакт",
        "Kontaktni yangilash": " Обновить контакт",
        "Kontaktni o'chirish": " Удалить контакт",
        "Kontaktni qidirish": "Поиск контакта",
        "Barcha kontaktlarni ko'rsatish": " Показать все контакты",
        "Chiqish": "Выход",
        "Ism yoki telefon raqami": "Имя или Номер телефона",
        "Yangi ism": "Новое имя",
        "Yangi telefon raqami": "Новый номер телефона",
        "Yangi email manzili": "Новый адрес электронной почты",
        "Yangi manzil": "Новый адрес",
        "Ism": "Имя",
        "Telefon raqami": "Номер телефона",
        "Email manzili": "Электронная почта",
        "Manzil": "Адрес",
        "Kontakt qo'shildi": "Контакт добавлен",
        "Kontakt topilmadi": "Контакт не найден",
        "Kontakt o'chirildi": "Контакт удален",
        "Kontakt yangilandi": "Контакт обновлен",
        "Kontaktlar ro'yxati bo'sh": "Список контактов пуст",
        "Tanlang": "Выберите",
        "Noto'g'ri tanlov!": "Неверный выбор!",
    },
    "en": {
        "Menyu:": "🌐 Menu:",
        "Yangi kontakt qo'shish": "Add new contact",
        "Kontaktni yangilash": " Update contact",
        "Kontaktni o'chirish": " Delete contact",
        "Kontaktni qidirish": "Search contact",
        "Barcha kontaktlarni ko'rsatish": " Show all contacts",
        "Chiqish": "Exit",
        "Ism yoki telefon raqami": "Name or phone number",
        "Yangi ism": "New name",
        "Yangi telefon raqami": "New phone number",
        "Yangi email manzili": "New email address",
        "Yangi manzil": "New address",
        "Ism": "Name",
        "Telefon raqami": "Phone number",
        "Email manzili": "Email address",
        "Manzil": "Address",
        "Kontakt qo'shildi": "Contact added",
        "Kontakt topilmadi": "Contact not found",
        "Kontakt o'chirildi": " Contact deleted",
        "Kontakt yangilandi": "Contact updated",
        "Kontaktlar ro'yxati bo'sh": "Contact list is empty",
        "Tanlang": "Select",
        "Noto'g'ri tanlov!": "Invalid choice!",
    }
}

joriy_til = "uz"

def t(matn):
    return tillar[joriy_til].get(matn, matn)

def yangi_kontakt():
    kontaktlar.append({
        "ism": input(f"💡  {t('Ism')}: "),
        "telefon": input(f"📞  {t('Telefon raqami')}: "),
        "email": input(f"📧  {t('Email manzili')}: "),
        "manzil": input(f"🏠  {t('Manzil')}: ")
    })
    print(f"✔️  {t('Kontakt qo\'shildi')}")

def kontaktni_yangilash():
    qidiruv = input(f"🔍  {t('Ism yoki telefon raqami')}: ")
    for kontakt in kontaktlar:
        if kontakt["ism"] == qidiruv or kontakt["telefon"] == qidiruv:
            kontakt["ism"] = input(f"✏️  {t('Yangi ism')}: ") or kontakt["ism"]
            kontakt["telefon"] = input(f"✏️  {t('Yangi telefon raqami')}: ") or kontakt["telefon"]
            kontakt["email"] = input(f"✏️  {t('Yangi email manzili')}: ") or kontakt["email"]
            kontakt["manzil"] = input(f"✏️  {t('Yangi manzil')}: ") or kontakt["manzil"]
            print(f"✔️  {t('Kontakt yangilandi')}")
            return
    print(f"❌  {t('Kontakt topilmadi')}")

def kontaktni_ochirish():
    qidiruv = input(f"🔍  {t('Ism yoki telefon raqami')}: ")
    for kontakt in kontaktlar:
        if kontakt["ism"] == qidiruv or kontakt["telefon"] == qidiruv:
            kontaktlar.remove(kontakt)
            print(f"🗑  {t('Kontakt o\'chirildi')}")
            return
    print(f"❌  {t('Kontakt topilmadi')}")

def kontaktni_qidirish():
    qidiruv = input(f"🔍  {t('Ism yoki telefon raqami')}: ")
    found = False
    for kontakt in kontaktlar:
        if kontakt["ism"].startswith(qidiruv[:2]) or kontakt["telefon"].endswith(qidiruv[-4:]):
            print("\n", kontakt, "\n")
            found = True
    if not found:
        print(f"❌  {t('Kontakt topilmadi')}")

def barcha_kontaktlar():
    if not kontaktlar:
        print(f"⚠️  {t('Kontaktlar ro\'yxati bo\'sh')}")
    else:
        print("\n" + "📜  " + t("Barcha kontaktlar") + ":")
        for kontakt in kontaktlar:
            print("  ➤", kontakt)

def asosiy_dastur():
    while True:
        bosh_menu()
        tanlov = {
            "1": yangi_kontakt,
            "2": kontaktni_yangilash,
            "3": kontaktni_ochirish,
            "4": kontaktni_qidirish,
            "5": barcha_kontaktlar,
            "6": lambda: print(f"❌  {t('Chiqish')}") or exit()
        }.get(input(f"   ➤ {t('Tanlang')}: "), lambda: print(f"⚠️  {t('Noto\'g\'ri tanlov!')}"))
        tanlov()

if __name__ == "__main__":
    tilni_tanlash()
    asosiy_dastur()
