def kategoriUsia(usia):
    if usia < 12:
        return "Anak-anak"
    elif 12 <= usia <= 17:
        return "Remaja"
    elif 18 <= usia <= 59:
        return "Dewasa"
    else:
        return "Lansia"
