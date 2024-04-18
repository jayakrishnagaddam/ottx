from flask import Flask,render_template,flash,session,request,redirect,url_for
from flask_pymongo import PyMongo



app = Flask(__name__)
app.config['SECRET_KEY']="1234"
app.config['MONGO_URI']="mongodb+srv://2100090162:manigaddam@deepsheild.kzgpo9p.mongodb.net/ottx"  
mongo=PyMongo(app)

@app.route('/home')
def home():
    return render_template('home.html')



@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        id = request.form.get('id')
        password = request.form.get('password')

        user_data = mongo.db.users.find_one({'id': id, 'password': password})
        
        if user_data:
            return redirect(url_for('home'))
        else:
            error = 'Invalid username or password'

    return render_template('login.html', error=error)
 

if __name__=='__main__':
    app.run(host="0.0.0.0",debug=True)