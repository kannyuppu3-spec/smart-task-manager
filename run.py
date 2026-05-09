from app import create_app, db, socketio

app = create_app()

with app.app_context():
    db.create_all()

@app.route('/')

def home():

    return "Smart Task Manager API Running Successfully"
from flask import render_template

@app.route('/dashboard')

def dashboard():

    return render_template('dashboard.html')
if __name__ == "__main__":

    import os

socketio.run(

    app,

    host='0.0.0.0',

    port=int(os.environ.get('PORT', 5000)),

    debug=True
)