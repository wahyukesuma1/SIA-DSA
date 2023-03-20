import os
import time
import pwinput
from turtle import left, update
os.system('cls')
# Library prettytable
from prettytable import PrettyTable
# Library datetime untuk format tanggal
from datetime import datetime
# Library/Path: controllers/controllerMahasiswa.py agar bisa akses fungsi-fungsi di sini
from controllers.controllerAccount import AccountController
# Library/Path: controllers/controllerMahasiswa.py agar bisa akses fungsi-fungsi di sini
from controllers.controllerMahasiswa import MahasiswaController


def convertData(data):
    # Error handling
    try:
        data[0] = int(data[0])
        return data
    except:
        print("Inputan harus berupa angka")
        return False

# Menu
def menu(privilege):
    if privilege == 'admin':
        table = PrettyTable(["No", "Menu"])
        table.title = "Menu Admin"   
        table.align = 'l'
        table.add_row([1, "Insert Data"])
        table.add_row([2, "Update Data"])
        table.add_row([3, "Delete Data"])
        table.add_row([4, "Search Data"])
        table.add_row([5, "Print Data"])
        table.add_row([6, "Sort Data"])
        table.add_row([7, "Reset Data"])
        table.add_row([8, "Show Data Based On Queue"])
        table.add_row([9, "Back To Login Page"])
        table.add_row([10, "Exit"])
        print(table)
    elif privilege == 'guest':
        table = PrettyTable(["No", "Menu"])
        table.title = "Menu Guest"
        table.add_row([1, "Search Data"])
        table.add_row([2, "Print Data"])
        table.add_row([3, "Sort Data"])
        table.add_row([4, "Exit"])
        print(table)

def add():

    def inputNim():
        try:
            nimBaru = int(input("Masukkan NIM \n> "))
            data.append(nimBaru)
        except ValueError:
            print("Mohon Masukkan NIM Dengan Benar")
            inputNim()
    while True:
        try:
            inputNim()
            namaBaru = input("Masukkan Nama \n> ")
            data.append(namaBaru)
            prodiBaru = input("Masukkan Prodi \n> ")
            data.append(prodiBaru)
            kelasBaru = input("Masukkan Kelas \n> ")
            data.append(kelasBaru)
            break
        except ValueError:
            print("Mohon Masukkan Data Yang Sesuai")
            True

    choice = input("Masukkan Data Tersebut Ke Database? (y/n) \n> ")
    if choice.lower() == 'y':
        # Insert data ke linkedlist -> ControllerMahasiswa
        mahasiswa.insertList(convertData(data))
        print("Data Berhasil Ditambahkan..")

        # Insert data ke database -> QueueMahasiswa
        mahasiswa.InsertData(data)
    else:
        mahasiswa.insertList(convertData(data))

def update():
    data.append(int(input("Masukkan NIM Mahasiswa \n> ")))
    data.append(input("Masukkan Nama Baru \n> "))
    data.append(input("Masukkan Prodi Baru \n> "))
    data.append(input("Masukkan Kelas Baru \n> "))

        
    choice = input("Simpan Perubahan Pada Database? (y/n) \n> ")
    if choice.lower() == 'y':
        # Update data ke linkedlist -> ControllerMahasiswa
        mahasiswa.updateList(convertData(data))
        # Update data ke database -> QueueMahasisw
        mahasiswa.UpdateData(convertData(data))                        
    else:
        mahasiswa.updateList(convertData(data))

def dels():
    try:
        data.append(input("Masukkan NIM Mahasiswa Yang Mau Dihapus \n> "))
        choice = input("Delete Include Database? (y/n): ")
        if choice.lower() == 'y':
            # Delete data ke linkedlist -> ControllerMahasiswa
            mahasiswa.deleteList(convertData(data))
            # Delete data ke database -> QueueMahasiswa
            mahasiswa.DeleteData(convertData(data))
        else:
            mahasiswa.deleteList(convertData(data))
    except AttributeError:
        print('Data Tersebut Tidak Ada')


def main():
    while True:
        tabelLogin = PrettyTable()
        tabelLogin.title = "Login Page"
        print(tabelLogin)
        print("="*5, "LINKED LIST MAHASISWA".center(40), "="*5)
        username = input("Input Your Username Below \n> ")
        password = pwinput.pwinput(prompt ="Input Your Password Below \n> ")
        # Inisialisasi Object AccountController -> ControllerAccount
        account = AccountController([username, password])
        username = username.capitalize()
        if account.privilige == 'admin':
            print("You Are Logged In As Admin")
            print(f"> Welcome Back, {username} < \n")
            print("Login Success... Please Wait")
            time.sleep(2.3)
            # Inisialisasi Object MahasiswaController -> ControllerMahasiswa
            global mahasiswa
            mahasiswa = MahasiswaController()
            while True:
                global data
                data = []
                menu(account.privilige)
                mahasiswa.refreshList()
                choice = input("Choice: ")
                if choice == '1':
                    mahasiswa.refreshList()
                    add()      
                elif choice == '2': update()  
                elif choice == '3': dels()
                elif choice == '4':
                    data.append(input("Cari Mahasiswa Berdasarkan NIM \n> "))
                    # Search data ke linkedlist -> ControllerMahasiswa
                    mahasiswa.searchList(convertData(data))
                elif choice == '5':
                    mahasiswa.refreshList()
                    # Print data ke linkedlist -> ControllerMahasiswa
                    mahasiswa.printList()
                elif choice == '6':
                    # Sort data ke linkedlist -> ControllerMahasiswa
                    mahasiswa.sortList()                                                         
                elif choice == '8':
                    # mahasiswa.refreshList()
                    # Print insert history -> QueueMahasiswa
                    mahasiswa.PrintQueue()                    
                elif choice == '9':
                    break
                else:
                    print("No Option, Please Try Again...")

        elif account.privilige == 'guest':
            print("You Are Logged In As Guest")
            print(f"> Hello, {username} < \n")
            print("Login Success... Please Wait")
            time.sleep(2.3)
            os.system("cls")
            mahasiswa = MahasiswaController()
            while True:
                data = []
                menu(account.privilige)
                mahasiswa.refreshList()
                choice = input("Choice: ")
                if choice == '1':
                    data.append(input("Search Mahasiswa Order By They NIM \n> "))
                    mahasiswa.searchList(convertData(data))
                elif choice == '2': mahasiswa.printList()
                elif choice == '3': mahasiswa.sortList()
                elif choice == '4': break
                else:
                    print("No Option, Please Try Again...")
        else:
            print("Invalid username or password")
        print("\n")
        
        if input("Press To Continue... "):
            break
main()
