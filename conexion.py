import mysql.connector
from mysql.connector import Error


class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='123456',
                db='basedatos'
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def listarley(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM leyes ")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def registrarley(self, leyes):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO leyes (Numero_Registro, Numero_Normativa, Tipo_Normativa) VALUES ('{0}', '{1}', {2})"
                cursor.execute(sql.format(leyes[0], leyes[1], leyes[2]))
                self.conexion.commit()
                print("La Ley fue registrada\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def actualizarley(self, leyes):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE leyes SET Numero_Registro,= '{0}', Numero_Normativa = {1} WHERE Tipo_Normativa) = '{2}'"
                cursor.execute(sql.format(leyes[1], leyes[2], leyes[0]))
                self.conexion.commit()
                print("La ley fue actualizada\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def eliminarley(self, codigoleyEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM leyes WHERE Numero_Normativa = '{0}'"
                cursor.execute(sql.format(codigoleyEliminar))
                self.conexion.commit()
                print("La ley fue eliminada\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))