# =================================================================
# BURSA TEKNİK ÜNİVERSİTESİ - Bilgisayar Mühendisliği Bölümü
# BLM101 - Bilgisayar Mühendisliğine Giriş Dersi Dönem Projesi
# Proje Konusu: Python ile HTML Sayfası Oluşturucu
# =================================================================

def html_sayfasi_olustur():
    """
    Bu fonksiyon, kullanıcıdan aldığı bilgilerle özelleştirilmiş
    bir HTML dosyası (index.html) oluşturur.
    """

    # Adım 1: KULLANICIDAN VERİ ALMA (INPUT)
    # Program konsolda kullanıcıya sorular sorarak bilgileri toplar.
    print("--- Kişisel Web Sayfası Oluşturucu ---")

    # Kullanıcının adını ve soyadını alır
    ad_soyad = input("Lütfen Adınızı ve Soyadınızı giriniz: ")

    # Kullanıcının biyografi metnini alır
    biyografi = input("Kısaca biyografinizden bahsediniz: ")

    # Kullanıcının aldığı dersleri virgülle ayrılmış şekilde alır
    dersler_ham_metin = input("Aldığınız dersleri aralarına virgül koyarak yazınız: ")

    # Adım 2: VERİ İŞLEME
    # Alınan ders metni split() fonksiyonu ile bir listeye dönüştürülür.
    # Her bir dersin başındaki ve sonundaki boşluklar strip() ile temizlenir.
    ders_listesi = [ders.strip() for ders in dersler_ham_metin.split(",")]

    # HTML içerisinde liste yapısı oluşturmak için bir string döngüsü kuruyoruz.
    # Her ders, HTML'deki <li> (list item) etiketleri arasına yerleştirilir.
    html_liste_elemanlari = ""
    for ders in ders_listesi:
        html_liste_elemanlari += f"            <li>{ders}</li>\n"

    # Adım 3: HTML VE CSS ŞABLONU OLUŞTURMA
    # Python'un f-string özelliği kullanılarak HTML kodları bir metin değişkenine atanır.
    # İçerisinde basit CSS renklendirmesi ve yapısal etiketler bulunur.
    html_sablonu = f"""
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{ad_soyad} - Kişisel Sayfa</title>
    <style>
        /* CSS ile Görsel Düzenleme */
        body {{ 
            font-family: 'Arial', sans-serif; 
            background-color: #e9ecef; 
            display: flex; 
            justify-content: center; 
            padding: 40px; 
        }}
        .konteynir {{ 
            background: white; 
            padding: 30px; 
            border-radius: 8px; 
            box-shadow: 0 0 10px rgba(0,0,0,0.1); 
            width: 100%; 
            max-width: 600px; 
        }}
        h1 {{ color: #004a99; border-bottom: 2px solid #004a99; }}
        .biyo-baslik {{ font-weight: bold; color: #333; }}
        ul {{ color: #555; }}
    </style>
</head>
<body>
    <div class="konteynir">
        <h1>{ad_soyad}</h1>
        <p class="biyo-baslik">Hakkımda:</p>
        <p>{biyografi}</p>
        <hr>
        <h3>Aldığım Dersler:</h3>
        <ul>
{html_liste_elemanlari}
        </ul>
    </div>
</body>
</html>
"""

    # Adım 4: DOSYA YAZMA İŞLEMİ
    # "with open" yapısı kullanılarak index.html dosyası oluşturulur ve yazılır.
    try:
        # 'w' modu (write) dosya yoksa oluşturur, varsa üzerine yazar.
        # encoding="utf-8" Türkçe karakterlerin doğru görünmesini sağlar.
        with open("index.html", "w", encoding="utf-8") as html_dosyasi:
            html_dosyasi.write(html_sablonu)

        print("\n" + "=" * 40)
        print("[BAŞARILI] index.html dosyası başarıyla oluşturuldu!")
        print("Klasörünüzdeki dosyayı tarayıcı ile açabilirsiniz.")
        print("=" * 40)

    except Exception as hata:
        # Dosya yazma sırasında oluşabilecek hataları yakalar ve ekrana basar.
        print(f"Hata oluştu: {hata}")


# --- PROGRAMIN ÇALIŞTIRILMASI ---
# Eğer bu dosya doğrudan çalıştırılırsa fonksiyonu çağırır.
if __name__ == "__main__":
    html_sayfasi_olustur()