from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Ciao mondo!'

if __name__ == '__main__':
    app.run()
