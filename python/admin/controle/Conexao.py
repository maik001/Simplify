'''
@author: jefferson Oliveira, Gabriele Rocha, José Maik
'''

import mysql.connector


class Conexao:
    __con = ""

    def getCon(self):
        return self.__con
    def setCon(self,data):
        self.__con = data
    def __init__(self):
        try:
            usr = "root" 
            senha = '123456'
            hst = "localhost"
            bd =  "simplify"
            self.setCon(mysql.connector.connect(user=usr,password=senha,database=bd,host=hst))

        except mysql.connector.Error as e:
            print("Erro ao conectar com o banco: ", str(e))
        except Exception as e:
            print("Erro geral:" , str(e))

