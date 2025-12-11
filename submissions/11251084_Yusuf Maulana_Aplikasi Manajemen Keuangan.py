from datetime import datetime

def input_tanggal(tanggal):

    try:
        datetime.strptime(tanggal, "%d/%m/%Y")
        return True 
    except ValueError:
        return False 

data_keuangan = [
    ["01/12/2024", "Gaji Bulanan", "Pemasukan", 5000000],
    ["03/12/2024", "Makan Siang", "Pengeluaran", 35000],
    ["05/12/2024", "Bayar Wifi", "Pengeluaran", 200000],
    ["07/12/2024", "Freelance Design", "Pemasukan", 1500000],
    ["10/12/2024", "Beli Pulsa", "Pengeluaran", 50000],
    ["12/12/2024", "Bonus Kerja", "Pemasukan", 1000000],
    ["15/12/2024", "Ngopi Bareng Teman", "Pengeluaran", 45000],
    ["18/12/2024", "Top Up Game", "Pengeluaran", 120000],
    ["20/12/2024", "Jual Item Online", "Pemasukan", 300000],
    ["22/12/2024", "Transportasi", "Pengeluaran", 20000]
]


def total(data_keuangan):
    total_pemasukan = sum(item[3] for item in data_keuangan if item[2].lower() == "pemasukan")
    total_pengeluaran = sum(item[3] for item in data_keuangan if item[2].lower() == "pengeluaran")
    print(f"Total pemasukan dana: Rp{total_pemasukan}, Total pengeluaran dana: Rp{total_pengeluaran}\n")


def bubble_sort(ascending=True): 
    n = len(data_keuangan)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ascending:
                if data_keuangan[j][3] > data_keuangan[j + 1][3]:
                    data_keuangan[j], data_keuangan[j + 1] = data_keuangan[j + 1], data_keuangan[j]
            else:
                if data_keuangan[j][3] < data_keuangan[j + 1][3]:
                    data_keuangan[j], data_keuangan[j + 1] = data_keuangan[j + 1], data_keuangan[j]

    if ascending:
        print("\nData berhasil diurutkan (Ascending).\n")
    else:
        print("\nData berhasil diurutkan (Descending).\n")


def create(): 
    print("\n> Masukan Data Keuangan")
    while True:
        tanggal = input("Masukan tanggal (dd/mm/yyyy): ")
        if input_tanggal(tanggal):
            break
        else:
            print("Format salah!")
    keterangan = input("Masukan Keterangan: ")
    kategori = input("Kategori (Pemasukan/Pengeluaran): ")
    nominal = int(input("Masukan nominal uang: "))

    data_keuangan.append([tanggal, keterangan, kategori, nominal])
    print("Data berhasil ditambahkan!\n")


def read():
    total(data_keuangan)
    print("\n> Daftar Data Keuangan")

    if not data_keuangan:
        print("Belum ada data keuangan yang tersimpan.\n")
        return

    print("No | Tanggal     | Keterangan       | Kategori       | Nominal")
    print("-" * 65)
    for i, item in enumerate(data_keuangan):
        print(f"{i + 1}. |{item[0]:12} |{item[1]:15} |{item[2]:14} |Rp{item[3]}")


def update():
    read()

    if not data_keuangan:
        return

    try:
        index = int(input("Pilih nomor data yang ingin diperbarui: ")) - 1
    except ValueError:
        print("Input harus angka!\n")
        return

    if 0 <= index < len(data_keuangan):
        print("\nMasukan Data yang baru:")
        tanggal = input("Masukan Tanggal baru: ")
        keterangan = input("Masukan Keterangan baru: ")
        kategori = input("Masukan Kategori baru: ")
        nominal = int(input("Masukan Nominal baru: "))

        data_keuangan[index] = [tanggal, keterangan, kategori, nominal]
        print("Data berhasil diperbarui!\n")
    else:
        print("Nomor tidak valid!\n")


def delete():
    read()

    if not data_keuangan:
        return

    try:
        index = int(input("Pilih nomor data yang ingin dihapus: ")) - 1
    except ValueError:
        print("Input harus angka!")
        return

    if 0 <= index < len(data_keuangan):
        data_keuangan.pop(index)
        print("Data berhasil dihapus!\n")
    else:
        print("Nomor tidak valid!\n")


def search():
    keyword = input("\nMasukan keyword pencarian: ")
    print("\nHasil Pencarian:")

    found = False
    for item in data_keuangan:
        if keyword.lower() in item[1].lower():
            print(item)
            found = True

    if not found:
        print("Tidak ada data cocok.\n")


def sort_data():
    print("\n> Pilih opsi pengurutan:")
    print("1. Ascending (Terkecil → Terbesar)")
    print("2. Descending (Terbesar → Terkecil)")
    print("3. Kembali")

    try:
        pilihan = int(input("Masukkan pilihan: "))
    except ValueError:
        print("Input harus angka!\n")
        return

    if pilihan == 1:
        bubble_sort(True)
        read()
    elif pilihan == 2:
        bubble_sort(False)
        read()
    elif pilihan == 3:
        return
    else:
        print("Pilihan tidak valid!\n")


def menuUtama():
    print("===================================")
    print("=== Aplikasi Manajemen Keuangan ===")
    print("===      by Yusuf Maulana      ===")
    print("===================================")
    print("1. Tambah Pemasukan/Pengeluaran")
    print("2. Lihat kategori")
    print("3. Edit Pemasukan/Pengeluaran")
    print("4. Hapus item keuangan")
    print("5. Keluar")

    try:
        return int(input("Masukkan pilihan [1-5]: "))
    except ValueError:
        return 0


def main():
    pilihan = 0
    while pilihan != 5:
        pilihan = menuUtama()

        if pilihan == 1:
            create()

        elif pilihan == 2:
            read()
            print("\n1. Sort Data(nominal)")
            print("2. Search Data")
            print("3. Kembali")
            try:
                fitur = int(input("Pilih opsi (1/2 untuk sort/seacrh): "))
            except ValueError:
                print("Input harus berupa angka!\n")
                continue

            if fitur == 1:
                sort_data()
            elif fitur == 2:
                search()

        elif pilihan == 3:
            update()

        elif pilihan == 4:
            delete()

        elif pilihan == 5:
            print("Terima kasih 😁!")

        else:
            print("Pilihan mu tidak valid 😡!\n")


main()
