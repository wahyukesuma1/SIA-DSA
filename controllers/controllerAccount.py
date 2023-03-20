# Library database untuk bisa melakukan aksi pada database
from database.database import Database

# Object untuk Account
class AccountController(Database):
    # Method untuk melakukan login
    def __init__(self, data):
        # Inisialisasi object database(parent) agar bisa mengakses method parent
        Database.__init__(self)
        self.data = {
            "username"  : data[0],
            "password"  : data[1],
        }
        # data untuk mengechek role account
        self.privilige = self.Privilige(self.data)
    
    # Method untuk mengechek role account
    def Privilige(self, data):
        # Query untuk mengambil role account
        sql = "SELECT privilege FROM account WHERE username = '{}' AND password = '{}'".format(self.data["username"], self.data["password"])
        self._cursor.execute(sql)
        result = self._cursor.fetchone()
        if result:
            # Format untuk menghilangkan petik pada string
            finalResult = result[0].replace("'", "")
            # Mengembalikan nilai role account
            return finalResult
        else:
            # apabila tidak ada data yang ditemukan maka akan mengembalikan nilai False
            return False