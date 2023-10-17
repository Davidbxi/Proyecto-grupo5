from app import app
from flask import render_template, request, flash, redirect, url_for, session,  jsonify
from mysql.connector.errors import Error


from controllers.funciones_home import *

PATH_URL = "public/novedades"

@app.route('/registrar-novedad', methods=['GET'])
def viewFormestudiante():
    if 'conectado' in session:
        return render_template(f'{PATH_URL}/form_estudiante.html')
    else:
        flash('primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))


@app.route('/form-registrar-aprendiz', methods=['POST'])
def formestudiante():
    if 'conectado' in session:
            resultado = procesar_form_estudiante(request.form)
            if resultado:
                return redirect(url_for('lista_estudiantes'))
            else:
                flash('El estudiante NO fue registrado.', 'error')
                return render_template(f'{PATH_URL}/form_estudiante.html')
    else:
        flash('primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))


@app.route('/lista-de-novedades', methods=['GET'])
def lista_estudiantes():
    if 'conectado' in session:
        return render_template(f'{PATH_URL}/lista_novedades.html', estudiantes=sql_lista_estudiantesBD())
    else:
        flash('primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))


@app.route("/detalles-novedad/", methods=['GET'])
@app.route("/detalles-novedad/<int:idestudiante>", methods=['GET'])
def detalleestudiante(idestudiante=None):
    if 'conectado' in session:
        if idestudiante is None:
            return redirect(url_for('inicio'))
        else:
            detalle_estudiante = sql_detalles_estudiantesBD(idestudiante) or []
            return render_template(f'{PATH_URL}/detalles_novedad.html', detalle_estudiante=detalle_estudiante)
    else:
        flash('Primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))

@app.route("/buscando-estudiante", methods=['POST'])
def viewBuscarestudianteBD():
    resultadoBusqueda = buscarestudianteBD(request.json['busqueda'])
    if resultadoBusqueda:
        return render_template(f'{PATH_URL}/resultado_busqueda_estudiante.html', dataBusqueda=resultadoBusqueda)
    else:
        return jsonify({'fin': 0})

@app.route("/editar-estudiante/<int:id>", methods=['GET'])
def viewEditarestudiante(id):
    if 'conectado' in session:
        respuestaestudiante = buscarestudianteUnico(id)
        if respuestaestudiante:
            return render_template(f'{PATH_URL}/form_estudiante_update.html', respuestaestudiante=respuestaestudiante)
        else:
            flash('El estudiante no existe.', 'error')
            return redirect(url_for('inicio'))
    else:
        flash('Primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))

@app.route('/actualizar-estudiante', methods=['POST'])
def actualizarestudiante():
    resultData = procesar_actualizacion_form(request)
    if resultData:
        return redirect(url_for('lista_estudiantes'))


@app.route("/lista-de-usuarios", methods=['GET'])
def usuarios():
    if 'conectado' in session:
        resp_usuariosBD = lista_usuariosBD()
        return render_template('public/usuarios/lista_usuarios.html', resp_usuariosBD=resp_usuariosBD)
    else:
        return redirect(url_for('inicioCpanel'))


@app.route('/borrar-usuario/<string:id>', methods=['GET'])
def borrarUsuario(id):
    resp = eliminarUsuario(id)
    if resp:
        flash('El Usuario fue eliminado correctamente', 'success')
        return redirect(url_for('usuarios'))


@app.route('/borrar-estudiante/<string:id_estudiante>', methods=['GET'])
def borrarestudiante(id_estudiante):
    resp = eliminarestudiante(id_estudiante)
    if resp:
        flash('El estudiante fue eliminado correctamente', 'success')
        return redirect(url_for('lista_estudiantes'))
