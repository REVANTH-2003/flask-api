from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__, template_folder='templates/')
app.config['SECRET_KEY'] = '@rm7676@'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:revan143rm@localhost:3306/flaskapi'
db = SQLAlchemy(app)

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100))

app.app_context().push()
db.create_all()

admin = Admin(app)
admin.add_view(ModelView(Word, db.session))

@app.route('/getword', methods=['GET'])
def get_word():
    word = Word.query.first()
    if word:
        return render_template('response.html', result_word = word.text)
    return render_template('response.html', result_word = "Word not found")

@app.route('/testcase', methods=['GET'])
def test():
    return render_template('testcase.html')

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()
