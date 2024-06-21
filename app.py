from flask import *
import pymysql
app = Flask(__name__)

# Routes Here
@app.route('/')
def home():
     return render_template('home.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    # Check if form was posted by user
    if request.method == 'POST':
            return render_template('signup.html', msg='Application Made Successfully')
    else:
        # Form not posted, display the form to allow user Post something
        return render_template('signup.html')

app.run(debug=True)