from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World! This is the index page.'

if __name__ == '__main__':
    app.run(debug=True)