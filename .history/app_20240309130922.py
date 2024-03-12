from flask import Flask

app = Flask(__name__)#和文件名称应当一致

@app.route('/')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'
# if __name__ == '__main__':
#     app.run()

@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'