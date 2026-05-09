from app import socketio
from flask import Blueprint, request, jsonify

from app import db

from app.models.task_model import Task

task = Blueprint('task', __name__)
@task.route('/api/tasks', methods=['POST'])

def add_task():

    data = request.get_json()

    new_task = Task(

        title=data.get('title'),

        description=data.get('description'),

        priority=data.get('priority'),

        status=data.get('status')
    )

    db.session.add(new_task)

    db.session.commit()
    socketio.emit(

    'new_task',

    {

        'message': f"New Task Added: {new_task.title}"
    }
)

    return jsonify({
        "message": "Task added successfully"
    }), 201
@task.route('/api/tasks', methods=['GET'])

def get_tasks():

    tasks = Task.query.all()

    task_list = []

    for task_item in tasks:

        task_list.append({

            "id": task_item.id,

            "title": task_item.title,

            "description": task_item.description,

            "priority": task_item.priority,

            "status": task_item.status,

            "created_date": task_item.created_date
        })

    return jsonify(task_list)
@task.route('/api/tasks/<int:id>', methods=['PUT'])

def update_task(id):

    task_item = Task.query.get(id)

    if not task_item:

        return jsonify({
            "message": "Task not found"
        }), 404

    data = request.get_json()

    task_item.title = data.get('title')

    task_item.description = data.get('description')

    task_item.priority = data.get('priority')

    task_item.status = data.get('status')

    db.session.commit()

    return jsonify({
        "message": "Task updated successfully"
    })
@task.route('/api/tasks/<int:id>', methods=['DELETE'])

def delete_task(id):

    task_item = Task.query.get(id)

    if not task_item:

        return jsonify({
            "message": "Task not found"
        }), 404

    db.session.delete(task_item)

    db.session.commit()

    return jsonify({
        "message": "Task deleted successfully"
    })