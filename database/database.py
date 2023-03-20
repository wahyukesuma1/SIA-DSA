# Library python untuk bisa mengakses Database
import mysql.connector

class Database:
    def __init__(self):
        # Membuat konektor ke DB
        self._db = mysql.connector.connect(
            host        = "localhost",
            user        = "root",
            passwd      = "",
            database    = "pa_asd"
        )
        # pengecheckan apakah koneksi berhasil atau tidak
        try:
            # Membuat cursor untuk mengakses DB
            self._cursor = self._db.cursor()
        except mysql.connector.Error as err:
            print("Error Code : ", err.errno)
            print("Error Message : ", err.msg)
            exit()