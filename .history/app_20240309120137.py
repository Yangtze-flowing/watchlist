from flask import Flask

app = Flask(__name__)#和文件名称应当一致

@app.route('/')
def hello():
    return 'Welcome to My Watchlist!'

# if __name__ == '__main__':
#     app.run()