from werkzeug.utils import secure_filename
import uuid  
from conexion.conexionBD import connectionBD  
import datetime
import re
import os
from os import remove  
from os import path  
import openpyxl  
from flask import send_file


def procesar_form_estudiante(dataForm):
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as cursor:

                sql = "INSERT INTO tbl_solicitud (num_doc, tipo_doc, p_nombre, s_nombre, p_apellido, s_apellido, id_ficha, id_comite,fecha_asig, observacion, id_estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"


                valores = (dataForm['documento_aprendiz'], dataForm['tipo_doc'], dataForm['p_nombre'],
                           dataForm['s_nombre'], dataForm['p_apellido'], dataForm['s_apellido'],
                            dataForm['ficha'], dataForm['comite'], dataForm['fecha_comite'], dataForm['observacion'], dataForm['estado'])
                cursor.execute(sql, valores)

                conexion_MySQLdb.commit()
                resultado_insert = cursor.rowcount
                return resultado_insert

    except Exception as e:
        return f'Se produjo un error en procesar_form_estudiante: {str(e)}'

def sql_lista_estudiantesBD():
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as cursor:
                querySQL = (f"""
                    SELECT 
                        e.num_doc,
                        e.p_nombre, 
                        e.p_apellido,
                        e.id_ficha,
                        e.id_comite,
                        CASE
                            WHEN e.id_estado=  1 THEN 'Inactivo'
                            WHEN e.id_estado = 2 THEN 'En proceso'
                            WHEN e.id_estado = 3 THEN 'Finalizado'
                        END AS id_estado
                    FROM tbl_solicitud AS e
                    ORDER BY e.num_doc DESC
                    """)
                cursor.execute(querySQL,)
                estudiantesBD = cursor.fetchall()
        return estudiantesBD
    except Exception as e:
        print(
            f"Errro en la función sql_lista_estudiantesBD: {e}")
        return None

def sql_detalles_estudiantesBD(idestudiante):
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as cursor:
                querySQL = ("""
                    SELECT 
                        e.tipo_doc,
                        e.num_doc,
                        e.p_nombre, 
                        e.s_nombre,
                        e.p_apellido,
                        e.s_apellido,
                        e.id_ficha,
                        e.id_comite,
                        CASE
                            WHEN e.id_estado = 1 THEN 'Inactivo'
                            WHEN e.id_estado = 2 THEN 'En proceso'
                            WHEN e.id_estado = 3 THEN 'Finalizado'
                        END AS id_estado,
                        e.observacion, 
                        e.fecha_asig,
                        DATE_FORMAT(e.fecha_registro, '%Y-%m-%d %h:%i %p') AS fecha_registro
                    FROM tbl_solicitud AS e
                    WHERE num_doc =%s
                    ORDER BY e.num_doc DESC
                    """)
                cursor.execute(querySQL, (idestudiante,))
                estudiantesBD = cursor.fetchone()
        return estudiantesBD
    except Exception as e:
        print(
            f"Errro en la función sql_detalles_estudiantesBD: {e}")
        return None

def buscarestudianteBD(search):
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as mycursor:
                querySQL = ("""
                        SELECT 
                        e.tipo_doc,
                        e.num_doc,
                        e.p_nombre, 
                        e.s_nombre,
                        e.p_apellido,
                        e.s_apellido,
                        e.id_ficha,
                        e.id_comite,
                        CASE
                            WHEN e.id_estado = 1 THEN 'Inactivo'
                            WHEN e.id_estado = 2 THEN 'En proceso'
                            WHEN e.id_estado = 3 THEN 'Finalizado'
                        END AS id_estado,
                        e.observacion, 
                        e.fecha_asig
                        FROM tbl_solicitud AS e
                        WHERE e.num_doc LIKE %s 
                        ORDER BY e.num_doc DESC
                    """)
                search_pattern = f"%{search}%" 
                mycursor.execute(querySQL, (search_pattern,))
                resultado_busqueda = mycursor.fetchall()
                return resultado_busqueda

    except Exception as e:
        print(f"Ocurrió un error en def buscarestudianteBD: {e}")
        return []
    
def buscarestudianteUnico(id):
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as mycursor:
                querySQL = ("""
                        SELECT 
                           *
                        FROM tbl_solicitud AS e
                        WHERE e.num_doc =%s LIMIT 1
                    """)
                mycursor.execute(querySQL, (id,))
                estudiante = mycursor.fetchone()
                return estudiante

    except Exception as e:
        print(f"Ocurrió un error en def buscarestudianteUnico: {e}")
        return []
def procesar_actualizacion_form(data):
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as cursor:
                num_doc = data.form['num_doc']
                tipo_doc = data.form['tipo_doc']
                p_nombre = data.form['p_nombre']
                s_nombre = data.form['s_nombre']
                p_apellido = data.form['p_apellido']
                s_apellido = data.form['s_apellido']
                id_ficha = data.form['id_ficha']
                id_comite = data.form['id_comite']
                fecha_asig = data.form['fecha_asig']
                observacion = data.form['observacion']
                id_estado = data.form['id_estado']
                querySQL = """
                        UPDATE tbl_solicitud
                        SET 
                            num_doc = %s,
                            tipo_doc = %s,
                            p_nombre = %s,
                            s_nombre = %s,
                            p_apellido = %s,
                            s_apellido = %s,
                            id_ficha = %s,
                            id_comite = %s,
                            fecha_asig = %s,
                            observacion = %s,
                            id_estado = %s
                        WHERE num_doc = %s
                    """
                values = (num_doc, tipo_doc,p_nombre, s_nombre, p_apellido,
                              s_apellido, id_ficha, id_comite,
                              fecha_asig, observacion, id_estado)
                cursor.execute(querySQL, values)
                conexion_MySQLdb.commit()

        return cursor.rowcount or []
    except Exception as e:
        print(f"Ocurrió un error en procesar_actualizacion_form: {e}")
        return None

def lista_usuariosBD():
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as cursor:
                querySQL = "SELECT id, name_surname, email_user, created_user FROM users"
                cursor.execute(querySQL,)
                usuariosBD = cursor.fetchall()
        return usuariosBD
    except Exception as e:
        print(f"Error en lista_usuariosBD : {e}")
        return []

def eliminarestudiante(id_estudiante):
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as cursor:
                querySQL = "DELETE FROM tbl_solicitud WHERE num_doc=%s"
                cursor.execute(querySQL, (id_estudiante))
                conexion_MySQLdb.commit()
                resultado_eliminar = cursor.rowcount

        return resultado_eliminar
    except Exception as e:
        print(f"Error en eliminarestudiante : {e}")
        return []

def eliminarUsuario(id):
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as cursor:
                querySQL = "DELETE FROM users WHERE id=%s"
                cursor.execute(querySQL, (id,))
                conexion_MySQLdb.commit()
                resultado_eliminar = cursor.rowcount

        return resultado_eliminar
    except Exception as e:
        print(f"Error al eliminar Usuario : {e}")
        return []
