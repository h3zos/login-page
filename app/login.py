#coding: utf-8

from .connexion import ConnexionDatabase

class LoginUser:
    def login(self, name, password):
        connexion = ConnexionDatabase()
        db = connexion.get_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM `users`")
        users = cursor.fetchall()
        for user in users:
            if user[1] == name and user[3] == password:
                connexion.close(cursor, db)
                return True
            connexion.close(cursor, db)
        return False
