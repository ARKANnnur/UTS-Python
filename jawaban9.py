transaksi = [("Senin", 50000), ("Selasa", -20000), ("Rabu", 0), ("Kamis", 100000)]

def hitungSaldo(transaksiList):
    return sum(nominal for hari, nominal in transaksiList)

def hariPengeluaranTerbesar(transaksiList):
    pengeluaran = [(hari, abs(nominal)) for hari, nominal in transaksiList if nominal < 0]
    if not pengeluaran:
        return "Tidak ada pengeluaran"
    hariTerbesar = max(pengeluaran, key=lambda x: x[1])
    return hariTerbesar[0]

def hariTanpaTransaksi(transaksiList):
    return [hari for hari, nominal in transaksiList if nominal == 0]

saldoAkhir = hitungSaldo(transaksi)
hariPengeluaran = hariPengeluaranTerbesar(transaksi)
hariTanpa = hariTanpaTransaksi(transaksi)

print(f"Saldo akhir: {saldoAkhir}")
print(f"Hari pengeluaran terbesar: {hariPengeluaran}")
print(f"Hari tanpa transaksi: {', '.join(hariTanpa) if hariTanpa else 'Tidak ada'}")
