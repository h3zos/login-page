#coding: utf-8

import mysql.connector

class ConnexionDatabase:
    user = "root"
    password = "root"
    adress = "localhost"
    database = "login_db"
    def get_connection(self):
        connexion = mysql.connector.connect(host=self.adress,
                                            user=self.user,
                                            password=self.password,
                                            database=self.database
                                            )
        return connexion
    def close_connection(self, cursor, connexion):
       cursor.close()
       connexion.close()
