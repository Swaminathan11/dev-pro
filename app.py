from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Let's try to deploy via helm now. not workingggggg!!!"

if __name__ == '__main__':
    app.run(host='0.0.0.0') 
