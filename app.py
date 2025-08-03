from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de tareas (cada una es un diccionario con id y texto)
tareas = []
contador_id = 1

@app.route('/')
def index():
    return render_template('index.html', tareas=tareas)

@app.route('/add', methods=['GET', 'POST'])
def add():
    global contador_id
    if request.method == 'POST':
        texto = request.form.get('tarea', '').strip()
        if texto:
            tarea = {'id': contador_id, 'texto': texto}
            tareas.append(tarea)
            contador_id += 1
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    tarea = next((t for t in tareas if t['id'] == id), None)
    if not tarea:
        return "Tarea no encontrada", 404

    if request.method == 'POST':
        nuevo_texto = request.form.get('tarea', '').strip()
        if nuevo_texto:
            tarea['texto'] = nuevo_texto
        return redirect(url_for('index'))

    return render_template('edit.html', tarea=tarea)

@app.route('/delete/<int:id>')
def delete(id):
    global tareas
    tareas = [t for t in tareas if t['id'] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
