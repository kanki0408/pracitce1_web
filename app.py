#flaskモジュールのFlaskクラスをインポートする。
from flask import Flask
import mysql.connector
from datetime import datetime as dt
import json

#appにflaskアプリの核を代入している
app = Flask(__name__)

#指定したURLにアクセスした際に、次の段落の物を実行する
@app.route('/')
def hello():
    # MySQLの接続設定
    config = {
        'user': 'your_user',       # MySQLのユーザー名
        'password': 'your_user_password',   # MySQLのパスワード
        'host': 'mysql',           # ホスト名
        'database': 'your_database',   # 使用するデータベース名
    }

    try:
        # データベースに接続
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # データの挿入
        '''
        insert_query = "INSERT INTO sample_table (name, age) VALUES (%s, %s)"
        data_to_insert = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
        cursor.executemany(insert_query, data_to_insert)
        connection.commit()  # 変更を保存
        '''

        # データの取得
        select_query = "SELECT * FROM posts"
        cursor.execute(select_query)
        results = cursor.fetchall()
        results[3]=results[3].strftime('%Y/%m/%d')
        return results
        '''
        # 取得したデータの表示
        for row in results:
            row[3]
            return json.dumps(row[0])
        '''

    except mysql.connector.Error as err:
        print(f"エラーが発生しました: {err}")

    finally:
        # 接続を閉じる
        if cursor:
            cursor.close()
        if connection:
            connection.close()


#app.pyを実行する時、__name__は__main__が代入される
if __name__ == '__main__':
    app.run()
