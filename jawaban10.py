todo = {
    "Belajar Python": "belum",
    "Cuci baju": "selesai"
}

def tambahTugas(todoDict):
    tugas = input("Masukkan nama tugas baru: ")
    if tugas in todoDict:
        print("Tugas sudah ada!")
    else:
        todoDict[tugas] = "belum"
        print(f"Tugas '{tugas}' berhasil ditambahkan.")

def ubahStatus(todoDict):
    if not todoDict:
        print("Belum ada tugas.")
        return

    print("\nDaftar Tugas:")
    for tugas, status in todoDict.items():
        print(f"- {tugas} ({status})")

    tugas = input("\nMasukkan nama tugas yang ingin diubah statusnya: ")
    if tugas not in todoDict:
        print("Tugas tidak ditemukan!")
        return

    newStatus = input("Masukkan status baru (selesai/belum): ").lower()
    if newStatus in {"selesai", "belum"}:
        todoDict[tugas] = newStatus
        print("Status berhasil diubah!")
    else:
        print("Status tidak valid!")

def tampilkanTugas(todoDict):
    if not todoDict:
        print("Tidak ada tugas.")
        return

    print("\nPilih filter status:")
    filterOptions = {
        "1": "semua",
        "2": "selesai",
        "3": "belum"
    }

    for key, val in filterOptions.items():
        print(f"{key}. {val.capitalize()}")

    pilihan = input("Pilihan (1/2/3): ")
    filterStatus = filterOptions.get(pilihan)

    if not filterStatus:
        print("Pilihan tidak valid!")
        return

    print("\n=== Daftar Tugas ===")
    for tugas, status in todoDict.items():
        if filterStatus == "semua" or status == filterStatus:
            print(f"- {tugas} ({status})")

def jalankanTodoList():
    while True:
        print("\n=== Menu To-Do List ===")
        print("1. Tambah Tugas Baru")
        print("2. Ubah Status Tugas")
        print("3. Tampilkan Tugas")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1-4): ")

        if pilihan == '1':
            tambahTugas(todo)
        elif pilihan == '2':
            ubahStatus(todo)
        elif pilihan == '3':
            tampilkanTugas(todo)
        elif pilihan == '4':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

jalankanTodoList()
