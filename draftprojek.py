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
    ll.tampil()


if __name__ == "__main__":
    main()