#flaskモジュールのFlaskクラスをインポートする。
from flask import Flask

#appにflaskアプリの核を代入している
app = Flask(__name__)

#指定したURLにアクセスした際に、次の段落の物を実行する
@app.route('/')
def hello():
    return "Hello, Flask!"

#app.pyを実行する時、__name__は__main__が代入される
if __name__ == '__main__':
    app.run()
