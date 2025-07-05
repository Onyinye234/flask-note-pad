from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
db = SQLAlchemy(app)


class Notes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    content = db.Column(db.String(5000), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f"Note {self.id}"

@app.route('/', methods= ['POST', 'GET'])


def index():
    db.create_all()
    
    if request.method == 'POST':
        note_title = request.form['title']
        note_content = request.form['content']

        new_note = Notes(title = note_title, content = note_content)

        try:
            db.session.add(new_note)
            db.session.commit()
            return redirect('/')

        except:
            return "Error occurred while creating note"
    else:
        all_notes = Notes.query.order_by(Notes.date_created).all()
        return render_template('index.html', notes = all_notes)


@app.route('/view/<int:id>', methods=['GET'])
def view(id):
 note_to_get = Notes.query.get_or_404(id)

 return render_template('view.html', note = note_to_get)


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    note_to_update = Notes.query.get_or_404(id)
    if request.method == 'POST':
        note_to_update.title = request.form['title']
        note_to_update.content = request.form['content']

    

        try:
            db.session.commit()
            return redirect('/')
        except:
            return "Error occurred while editing note"


    else:
        return render_template('update.html', note=note_to_update)
    

@app.route('/delete/<int:id>', methods=['POST','GET'])
def delete(id):
    task_to_delete = Notes.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "Error occurred while deleting note"
    

if __name__ == "__main__":
    app.run(debug=True)
