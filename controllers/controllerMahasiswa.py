import os
# Library prettytable untuk membuat tabel
from prettytable import PrettyTable
# Library / Path: controllers/controllerMahasiswa.py agar bisa akses fungsi-fungsi di sini
from controllers.queueMahasiswa import QueueMahasiswa
# Library / Path untuk Node LL disini
from models.mahasiswa import Mahasiswa

os.system('cls')

# Object untuk LL
class MahasiswaController(QueueMahasiswa):
    def __init__(self):
        # Inisialisasi object QueueMahasiswa(Parent) agar bisa menggunakan method-method yang ada di QueueMahasiswa
        super().__init__()
        # Property object/wadah LL
        self.head = None
    
    # Method untuk menambahkan data ke dalam LL
    def insertList(self, data):
        # Pengechekan apakah list kosong
        if self.head == None:
            # Jika list kosong, maka buat node baru dan set headnya menjadi node baru
            self.head = Mahasiswa(data)
        else:
            # Jika list tidak kosong, maka buat node baru dan set headnya menjadi node baru
            current = self.head
            while current.next != None:
                # Jika ada data/nim yang sama, maka tidak akan di insert
                if current.data["nim"] == data[0]:
                    print("Data sudah ada")
                    break
                else:
                    # Untuk meneruskan LL hingga ke node terakhir
                    current = current.next
            current.next = Mahasiswa(data)
    
    # Method untuk memasukan data dari DB ke dalam LL
    def refreshList(self):
        self.resetList()
        # GetData() method -> QueueMahasiswa, untuk mengambil data dari DB
        result = self.GetData()
        for i in result:
            # Memasukan data ke dalam LL
            self.insertList(i)

    # Method untuk menampilkan data dari LL
    def printList(self):
        os.system('cls')
        # Pengechekan apakah list kosong
        if self.head == None:
            print("List kosong")
        else:

            # current adalah wadah untuk LL
            current = self.head
            # Membuat tabel
            table = PrettyTable(["NIM", "Nama", "Prodi", "Kelas"])
            table.title = "DATA MAHASISWA"
            global judul
            judul = table.title
            while current != None:
                # Menambahkan data ke dalam tabel
                table.add_row([current.data["nim"], current.data["nama"], current.data["prodi"], current.data["kelas"]])
                # Meneruskan LL
                current = current.next
            # Menampilkan tabel
            print(table)
    
    # Method untuk melakukan fibonacci search
    def fibonacciSearch(self, dataArray, data, lenArray):
        # index pertama
        fibMMm2 = 0
        # index kedua
        fibMMm1 = 1 
        # index ketiga
        fibM = fibMMm2 + fibMMm1

        # Ketika index ketiga lebih besar dari panjang array, maka melakukan perhitungan fibonacci
        while (fibM < lenArray):
            fibMMm2 = fibMMm1
            fibMMm1 = fibM
            fibM = fibMMm2 + fibMMm1

        # Offset untuk mencari index yang akan dicari
        offset = -1
        # Mencari index yang akan dicari
        while (fibM > 1):
            # Lokasi index yang akan dicari
            i = min(offset+fibMMm2, lenArray-1)

            # Jika data yang dicari lebih besar dari data pada index i, maka offset bertambah
            if (dataArray[i]["nim"] < data):
                fibM = fibMMm1
                fibMMm1 = fibMMm2
                fibMMm2 = fibM - fibMMm1
                offset = i
            # Jika data yang dicari lebih kecil dari data pada index i, maka offset berkurang
            elif (dataArray[i]["nim"] > data):
                fibM = fibMMm2
                fibMMm1 = fibMMm1 - fibMMm2
                fibMMm2 = fibM - fibMMm1
            # Jika data yang dicari sama dengan data maka mengembalikan index i
            else:
                return i
        # Jika data tidak ditemukan, maka panjang array akan dikurangi 1
        if(fibMMm1 and dataArray[lenArray - 1]["nim"] == data):
            return lenArray - 1

        # Jika data tidak ditemukan, maka mengembalikan -1
        return -1

    # Method untuk mencari data pada LL
    def searchList(self, data):
        # Pengechekan apakah list kosong
        if self.head == None:
            print("List kosong")
        else:
            # dataArray adalah warung array yang akan di search
            dataArray = self.convertArray()
            # lenArray adalah panjang array
            lenArray  = len(dataArray)
            # Mencari index yang akan dicari dengan method fibonacciSearch
            dataFound = self.fibonacciSearch(dataArray, data[0], lenArray)
            # Membuat tabel
            table = PrettyTable(["NIM", "Nama", "Prodi", "Kelas"])

            # Jika data ditemukan maka akan diprint dengan table
            if dataFound >= 0:
                print("Data ditemukan")
                table.add_row([dataArray[dataFound]["nim"], dataArray[dataFound]["nama"], dataArray[dataFound]["prodi"], dataArray[dataFound]["kelas"]])
                print(table)
            else:
                print("Data tidak ditemukan")
    
    # Method untuk mengedit data pada LL
    def updateList(self, data):
        # Pengechekan apakah list kosong
        if self.head == None:
            print("List kosong")
        else:
            # current adalah wadah untuk LL
            current = self.head
            while current != None:
                if current.data["nim"] == data[0]:
                    current.data["nama"] = data[1]
                    current.data["prodi"] = data[2]
                    current.data["kelas"] = data[3]
                    break
                current = current.next

    # Method untuk mensorting data pada LL
    def mergeSort(self, data):
        # Pengecheckan panjang array
        if len(data) > 1:
            # Membagi array menjadi 2 bagian
            mid = len(data) // 2
            left = data[:mid]
            right = data[mid:]

            # Mengurutkan bagian kiri
            self.mergeSort(left)

            # Mengurutkan bagian kanan
            self.mergeSort(right)

            # Menggabungkan kedua bagian
            # i adalah index untuk left
            # j adalah index untuk right
            # k adalah index untuk data
            i = 0
            j = 0
            k = 0
            # Mereplace data pada array
            while i < len(left) and j < len(right):
                if left[i]["nim"] < right[j]["nim"]:
                    data[k] = left[i]
                    i += 1
                else:
                    data[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                data[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                data[k] = right[j]
                j += 1
                k += 1
        else:
            return data

    # Method untuk mensort data pada LL
    def sortList(self):
        # Pengechekan apakah list kosong
        if self.head == None:
            print("List kosong")
        else:
            # Data adalah array yang akan di sort
            data = self.convertArray()
            # Menjalankan method mergeSort untuk mengsorting data
            self.mergeSort(data)
            # setelah data di sort, maka akan dimasukan ke dalam LL
            self.convertList(data)
            print("Data berhasil di sort")

    # Method untuk mengubah data pada LL menjadi array
    def convertArray(self):
        # Pengechekan apakah list kosong
        if self.head == None:
            return []
        else:
            # current adalah wadah untuk LL
            current = self.head
            # result adalah wadah array
            result = []
            # Memasukan data LL ke dalam array 1 per 1
            while current != None:
                result.append(current.data)
                # Meneruskan data LL hingga habis/None
                current = current.next
            # Mengembalikan array
            return result
    
    # Method untuk mengubah data array menjadi LL
    def convertList(self, data):
        # Melakukan reset LL agar tidak terjadi duplicate data
        self.resetList()
        # Memasukan data array ke dalam LL 1 per 1
        for i in range(len(data)):
            # temp adalah wadah untuk menyimpan data array agar bisa menjadi single array
            # dan dimasukan ke loop agar reset setiap looping
            temp = []
            temp.append(data[i]["nim"])
            temp.append(data[i]["nama"])
            temp.append(data[i]["prodi"])
            temp.append(data[i]["kelas"])
            self.insertList(temp)

    # Method untuk menghapus data pada LL
    def deleteList(self, data):
        # Pengechekan apakah list kosong
        if self.head == None:
            print("List kosong")
        else:
            # current adalah wadah untuk LL
            current = self.head
            # Ketika data yang ingin dihapus berada di index pertama pada LL maka langsung dihapus
            if current.data["nim"] == data[0]:
                self.head = current.next
            # Ketika data yang ingin dihapus tidak berada di index pertama pada LL
            else:
                # Mencari data yang ingin dihapus
                while current != None:
                    # Ketika next dari current adalah data yang ingin dihapus maka 
                    # data tersebut direplace dengan next dari current
                    if current.next.data["nim"] == data[0]:
                        current.next = current.next.next
                        break
                    # Meneruskan data LL hingga habis/None
                    current = current.next

    # Method untuk menghapus seluruh data pada LL
    def resetList(self):
        # Mengembalikan self.head/wadah LL menjadi None
        self.head = None