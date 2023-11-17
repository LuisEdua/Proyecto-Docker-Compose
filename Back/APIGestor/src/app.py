from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from config import config
import os
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(config['development'])
CORS(app)

db = SQLAlchemy(app)

class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    fecha = db.Column(db.String(15), nullable=False)
    status = db.Column(db.Boolean, nullable=False)

def crear_tabla():
    with app.app_context():
        db.create_all()

@app.route('/', methods=['GET'])
def listar_tareas():
    try:
        tareas = Tarea.query.all()
        datos = [{'id':tarea.id, 'title': tarea.title, 'fecha': tarea.fecha, 'status': tarea.status} for tarea in tareas]
        return datos
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/', methods=['POST'])
def crear_tarea():
    try:
        data = request.json
        tarea = Tarea(title=data['title'], fecha=data['fecha'], status=data['status'])
        db.session.add(tarea)
        db.session.commit()
        return listar_tareas()
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/<int:id>', methods=['PUT'])
def editar_tarea(id):
    try:
        data = request.json
        tarea = Tarea.query.get(id)
        tarea.title = data['actividad']
        tarea.fecha = data['fechaLimite']
        tarea.status = data['terminado']
        db.session.commit()
        return listar_tareas
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/<int:id>', methods=['DELETE'])
def borrar_tarea(id):
    try:
        tarea = Tarea.query.get(id)
        db.session.delete(tarea)
        db.session.commit()
        return jsonify({'message': 'Tarea borrada correctamente'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    host = os.environ.get('FLASK_RUN_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_RUN_PORT', 5000))
    crear_tabla()
    app.run(host=host, port=port)
