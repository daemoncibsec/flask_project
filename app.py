from flask import Flask, render_template, abort, redirect, request
import json

app = Flask(__name__)

def owasp10():
    with open("data/owasp.json", encoding='utf-8') as file:
        return json.load(file)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/xxxs', methods=['GET', 'POST'])
def xxxs():
    resultados = []
    datos = owasp10()
    if request.method == 'POST':
        termino = request.form.get('nombre_xxx', '').lower()
        if termino:
            resultados = [v for v in datos if v['nombre'].lower().startswith(termino)]
        else:
            resultados = datos
    return render_template('xxxs.html', resultados=resultados)

@app.route('/xxx?=<identificador>')
def detalle_xxx(identificador):
    datos = owasp10()
    item = next((v for v in datos if v['id'] == identificador), None)
    if item is None:
        error()
    return render_template('detalle_xxx.html', item=item)

@app.route('/error')
def error():
    return abort(404)

app.run("0.0.0.0",5000,debug=True)
