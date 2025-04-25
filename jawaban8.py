def hitungKarakter(text):
    vokal = "aiueoAIUEO"
    jumlahVokal = 0
    jumlahKonsonan = 0

    for char in text:
        if char.isalpha():
            if char in vokal:
                jumlahVokal += 1
            else:
                jumlahKonsonan += 1

    jumlahKata = len(text.split())

    return jumlahVokal, jumlahKonsonan, jumlahKata


kalimat = input("Masukkan kalimat: ")

vokal, konsonan, kata = hitungKarakter(kalimat)

print(f"Jumlah huruf vokal: {vokal}")
print(f"Jumlah huruf konsonan: {konsonan}")
print(f"Jumlah kata: {kata}")
