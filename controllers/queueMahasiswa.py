# Library  untuk format tanggal
from datetime import datetime
# Library untuk membuat table
from prettytable import PrettyTable
# Library untuk membuat Queue
from queue import Queue
# Library / Path untuk mengakses fungsi dari file database/database.py
from database.database import Database

# Object untuk Queue
class QueueMahasiswa(Database):
    def __init__(self):
        # Inisialisasi object database(parent) agar bisa mengakses method parent
        super().__init__()
        # Inisialisasi object queue
        self.data = Queue()

    # Fungsi untuk menambahkan data ke queue dan database
    def InsertData(self, data):
        # Insert data ke queue
        self.data.put(data)
        # Validasi apakah data sudah ada di database
        if self.Validation(data):
            print("Data sudah ada")
        else:
            # Insert data ke database
            sql = "INSERT INTO mahasiswa (nim, nama, prodi, kelas) VALUES ('{}', '{}', '{}', '{}')".format(data[0], data[1], data[2], data[3])
            self._cursor.execute(sql)
            self._db.commit()

    # Method untuk mengambil data dari database agar bisa dimasukkan ke LL
    def GetData(self):
        # Query untuk mengambil data dari database
        sql = "SELECT * FROM mahasiswa ORDER BY nim ASC"
        self._cursor.execute(sql)
        data = self._cursor.fetchall()
        # Mengembalikan data dari database
        return data

    # Method untuk mengambil data dari database lalu ditampilkan ke layar
    def PrintData(self):
        # Query untuk mengambil data dari database
        sql = "SELECT * FROM mahasiswa"
        self._cursor.execute(sql)

        # Membuat table
        tables = PrettyTable(["NIM", "Nama", "Prodi", "Kelas"])
        for data in self._cursor:
            # Menambahkan data ke table
            tables.add_row(data)
        # Menampilkan table
        print(tables)

    # Method untuk mengedit / mengubah data pada database
    def UpdateData(self, data):
        # Validasi apakah data sudah ada di database
        if self.Validation(data):
            # Query untuk mengubah data pada database
            sql = "UPDATE mahasiswa SET nim = '{}', nama = '{}', prodi = '{}', kelas = '{}' WHERE nim = '{}'".format(data[0], data[1], data[2], data[3], data[0])
            self._cursor.execute(sql)
            self._db.commit()
        else:
            print("Data tidak ada")

    # Method untuk menghapus data pada database
    def DeleteData(self, data):
        # Validasi apakah data sudah ada di database
        if self.Validation(data):
            # Query untuk menghapus data pada database
            sql = "DELETE FROM mahasiswa WHERE nim = {}".format(data[0])
            self._cursor.execute(sql)
            self._db.commit()
        else:
            print("Data tidak ada")

    # Method untuk menampilkan data pada queue
    def PrintQueue(self):
        # Membuat table
        tables = PrettyTable(["NIM", "Nama", "Prodi", "Kelas"])
        temp = Queue()
        while not self.data.empty():
            data = self.data.get()
            tables.add_row(data)
            temp.put(data)       
        self.data = temp
        # Menampilkan table
        print(tables)
    
    # Method untuk menghapus seluruh data pada queue
    def ResetQueue(self):
        # Inisiialisasi object queue kembali ke kosong
        self.data = Queue()

    # Method untuk melakukan validasi apakah data sudah ada di database
    def Validation(self, data):
        # Query untuk mengecek apakah data sudah ada di database
        sql = "SELECT * FROM mahasiswa WHERE nim = {}".format(data[0])
        self._cursor.execute(sql)
        # data adalah wadah untuk menampung data yang dicari dari database
        data = self._cursor.fetchone()
        # Validasi apakah data ada atau tidak
        if data is None:
            return False
        else:
            return True