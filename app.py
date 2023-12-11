from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/display_message', methods=['POST'])
def display_message():
    if request.method == 'POST':
        return render_template('message.html')
    else:
        return 'Invalid request method'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
