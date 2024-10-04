from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'テスト成功！平松'

if __name__ == '__main__':
    app.run(debug=True)
