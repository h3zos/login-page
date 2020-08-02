#coding: utf-8

from .connexion import ConnexionDatabase

class RegisterUser:
    def register(self, name, mail, password, birthday):
        connexion = ConnexionDatabase()
        db = connexion.get_connection()
        cursor = db.cursor()
        cursor.execute("INSERT INTO `users`(`name`, `mail`, `password`, `birthday`) VALUES (%s, %s, %s, %s)",(name, mail, password, birthday))
        db.commit()
