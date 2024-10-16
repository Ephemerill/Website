from flask import Flask

app = Flask(__app__)

@app.route('/')
def home():
    return "<h1>Welcome to Your Flask Web Page!</h1>"

if __name__ == '__main__':
    app.run()
