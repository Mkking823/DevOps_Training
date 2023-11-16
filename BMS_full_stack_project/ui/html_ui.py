from flask import Flask, render_template
from flask_cors import CORS
#here
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    CORS(app)
    app.run(debug=True,port=5002)
