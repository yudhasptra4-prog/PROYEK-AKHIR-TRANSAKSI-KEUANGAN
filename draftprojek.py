# ===================================================================
# JUDUL PROGRAM  : Sistem Riwayat Transaksi Rekening
# MATA KULIAH    : Algoritma & Struktur Data    
# KELAS          : TPL-B
# KELOMPOK       : 16
#
# ANGGOTA KELOMPOK:
# 1. Muhammad Ibnu Akbar       (J0403251028)
# 2. Yudha Saputra             (J0403251119)
# 3. Muhammad Ridzqi Badarudin (J0403251146)
#
# DESKRIPSI:
# Program ini digunakan untuk mencatat riwayat transaksi rekening.
# Data disimpan menggunakan file CSV (file handling).
# Struktur data yang digunakan adalah Linked List dan Array (List).
# ===================================================================

import csv
import os

FILE_NAME = "transaksi.csv"

# =========================
# STRUKTUR DATA: LINKED LIST
# =========================

# Node untuk menyimpan satu data transaksi
class Node:
    def __init__(self, data):
        self.data = data      # menyimpan data transaksi
        self.next = None      # menunjuk ke data berikutnya


# Linked List untuk menyimpan banyak data
class LinkedList:
    def __init__(self):
        self.head = None  # awal linked list

    # Fungsi untuk menambah data ke linked list
    def tambah(self, data):
        node_baru = Node(data)
        if self.head is None:
            self.head = node_baru
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node_baru

    # Fungsi untuk menampilkan data
    def tampil(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    # Fungsi untuk mengubah linked list menjadi array (list)
    def ke_list(self):
        hasil = []
        temp = self.head
        while temp:
            hasil.append(temp.data)
            temp = temp.next
        return hasil


# =========================
# FILE HANDLING
# =========================

# Fungsi untuk membuat file CSV jika belum ada
def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["tanggal", "keterangan", "tipe", "jumlah"])


# Fungsi untuk membaca file CSV ke Linked List
def baca_file(linked_list):
    with open(FILE_NAME, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            linked_list.tambah(row)


# Fungsi untuk menyimpan data dari Linked List ke CSV
def simpan_file(linked_list):
    with open(FILE_NAME, 'w', newline='') as f:
        writer = csv.writer(f)

        # menulis header
        writer.writerow(["tanggal", "keterangan", "tipe", "jumlah"])

        # menulis isi data
        temp = linked_list.head
        while temp:
            data = temp.data
            writer.writerow([
                data["tanggal"],
                data["keterangan"],
                data["tipe"],
                data["jumlah"]
            ])
            temp = temp.next


# ===========================
# CEK JALANKAN PROGRAM UTAMA 
# ===========================

def main():
    ll = LinkedList()

    init_file()      # membuat file jika belum ada
    baca_file(ll)    # membaca data dari file

    # misal tambah data
    data_baru = {
        "tanggal": "2026-04-14",
        "keterangan": "Jajan",
        "tipe": "debit",
        "jumlah": "15000"
    }

    ll.tambah(data_baru)

    simpan_file(ll)  # menyimpan ke file

    print("Data transaksi:")
# ===========================
# FUNGSI BANTUAN
# ===========================

def validasi_tanggal(tanggal):
    try:
        tahun, bulan, hari = map(int, tanggal.split("-"))
        return 1 <= bulan <= 12 and 1 <= hari <= 31 and len(str(tahun)) == 4
    except Exception:
        return False

def input_transaksi():
    while True:
        tanggal = input("Masukkan tanggal (YYYY-MM-DD): ").strip()
        if validasi_tanggal(tanggal):
            break
        print("Format tanggal tidak valid. Gunakan format YYYY-MM-DD.")

    keterangan = input("Masukkan keterangan transaksi: ").strip()
    while not keterangan:
        print("Keterangan tidak boleh kosong.")
        keterangan = input("Masukkan keterangan transaksi: ").strip()

    tipe = input("Masukkan tipe transaksi (debit/kredit): ").strip().lower()
    while tipe not in ["debit", "kredit"]:
        print("Tipe harus 'debit' atau 'kredit'.")
        tipe = input("Masukkan tipe transaksi (debit/kredit): ").strip().lower()

    while True:
        jumlah = input("Masukkan jumlah transaksi: ").strip()
        if jumlah.isdigit() and int(jumlah) > 0:
            break
        print("Jumlah harus berupa angka positif.")

    return {
        "tanggal": tanggal,
        "keterangan": keterangan,
        "tipe": tipe,
        "jumlah": jumlah
    }

def hitung_saldo(linked_list):
    saldo = 0
    temp = linked_list.head
    while temp:
        jumlah = int(temp.data["jumlah"])
        if temp.data["tipe"] == "kredit":
            saldo += jumlah
        else:
            saldo -= jumlah
        temp = temp.next
    return saldo

def tampilkan_daftar(linked_list):
    if linked_list.head is None:
        print("Tidak ada transaksi.")
        return

    print("{:3} | {:10} | {:20} | {:6} | {:10}".format("No", "Tanggal", "Keterangan", "Tipe", "Jumlah"))
    print("-" * 60)
    index = 1
    temp = linked_list.head
    while temp:
        data = temp.data
        print("{:3} | {:10} | {:20} | {:6} | {:10}".format(
            index,
            data["tanggal"],
            data["keterangan"],
            data["tipe"],
            data["jumlah"]
        ))
        temp = temp.next
        index += 1
    print("-" * 60)
    print(f"Saldo akhir: {hitung_saldo(linked_list)}")

def cari_transaksi(linked_list):
    if linked_list.head is None:
        print("Tidak ada transaksi untuk dicari.")
        return

    kata = input("Masukkan kata kunci untuk mencari (tanggal/keterangan/tipe): ").strip().lower()
    if not kata:
        print("Kata kunci tidak boleh kosong.")
        return

    ditemukan = False
    index = 1
    temp = linked_list.head
    while temp:
        data = temp.data
        if kata in data["tanggal"].lower() or kata in data["keterangan"].lower() or kata in data["tipe"].lower():
            if not ditemukan:
                print("Hasil pencarian:")
                print("{:3} | {:10} | {:20} | {:6} | {:10}".format("No", "Tanggal", "Keterangan", "Tipe", "Jumlah"))
                print("-" * 60)
            print("{:3} | {:10} | {:20} | {:6} | {:10}".format(
                index,
                data["tanggal"],
                data["keterangan"],
                data["tipe"],
                data["jumlah"]
            ))
            ditemukan = True
        temp = temp.next
        index += 1

    if not ditemukan:
        print("Transaksi tidak ditemukan.")

def hapus_transaksi(linked_list):
    if linked_list.head is None:
        print("Tidak ada transaksi untuk dihapus.")
        return

    tampilkan_daftar(linked_list)
    pilihan = input("Masukkan nomor transaksi yang akan dihapus: ").strip()
    if not pilihan.isdigit():
        print("Masukan harus angka.")
        return

    nomor = int(pilihan)
    if nomor < 1:
        print("Nomor transaksi tidak valid.")
        return

    prev = None
    temp = linked_list.head
    index = 1
    while temp and index < nomor:
        prev = temp
        temp = temp.next
        index += 1

    if temp is None:
        print("Nomor transaksi tidak ditemukan.")
        return

    if prev is None:
        linked_list.head = temp.next
    else:
        prev.next = temp.next

    print("Transaksi berhasil dihapus.")

def menu():
    print("\\n=== SISTEM RIWAYAT TRANSAKSI REKENING ===")
    print("1. Lihat semua transaksi")
    print("2. Tambah transaksi")
    print("3. Cari transaksi")
    print("4. Hapus transaksi")
    print("5. Keluar")
    return input("Pilih menu (1-5): ").strip()

def main():
    ll = LinkedList()
    init_file()
    baca_file(ll)

    while True:
        pilihan = menu()
        if pilihan == "1":
            tampilkan_daftar(ll)
        elif pilihan == "2":
            transaksi = input_transaksi()
            ll.tambah(transaksi)
            simpan_file(ll)
            print("Transaksi berhasil ditambahkan.")
        elif pilihan == "3":
            cari_transaksi(ll)
        elif pilihan == "4":
            hapus_transaksi(ll)
            simpan_file(ll)
        elif pilihan == "5":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1 sampai 5.")

if __name__ == "__main__":
    main()
   