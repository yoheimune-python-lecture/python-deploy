# python-deploy

## 注意
本サンプルは、製作時から時間経過することで古くなっていたり、個々人のローカル環境によって、エラーが発生する可能性があります。  
エラーとなった場合には、エラーメッセージなど確認しつつ、対処してみてください。

## 準備
以下のコマンドでDockerコンテナのビルドと起動を行います.
```shell
docker compose build
docker compose up
```

## CGIのサンプル.
上記でコンテナを起動後、下記でアクセスできます。
```text
http://localhost:8889/cgi-sample.py
```

## WSGIのサンプル
下記より起動できます（これはDockerコンテナ内ではなく、個々人のPC上で実行します）.  
Pythonは3系であることを想定します.
```shell
cd server
python wsgi-sample.py
```
以下よりアクセスできます。
```text
http://0.0.0.0:8880
```

## Flaskアプリケーション（サンプルアプリ）の起動
下記より起動できます（これはDockerコンテナ内ではなく、個々人のPC上で実行します）.  
Pythonは3系であることを想定します.
```shell
cd server/app-flask
pip install -r requirements.txt
python myapp.py
```
以下よりアクセスできます。
```text
http://0.0.0.0:5001
```

## gunicornによるFlask起動
下記より起動できます（これはDockerコンテナ内ではなく、個々人のPC上で実行します）.  
Pythonは3系であることを想定します.
```shell
cd server/app-flask
pip install -r requirements.txt
gunicorn app:app
```

## FYI
* OS : CentOS7.8
* Python version : 3.11.1
* Pythonパス : /usr/local/bin/python3
* Apache : 2.4

## References
* [WSGIとは - Wikipedia](https://ja.wikipedia.org/wiki/Web_Server_Gateway_Interface)
* [Gunicorn公式サイト](https://gunicorn.org/)